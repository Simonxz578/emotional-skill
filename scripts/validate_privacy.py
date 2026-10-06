#!/usr/bin/env python3
"""Fail closed on private paths, common identifiers, overlay copies, or history leaks.

Scans Git index blobs (the actual commit candidate), working-tree counterparts,
all reachable commit trees and commit messages. Findings show locations/reasons,
never the matched private text. Heuristic scanning is not a privacy guarantee.
"""
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

EMAIL = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', re.I)
PHONE = re.compile(r'(?<![\w.])(?:\+?86[- ]?)?1[3-9]\d{9}(?![\w.])|(?<![\w.])(?:\+\d{1,3}[- .])?\(?\d{3}\)?[- .]\d{3}[- .]\d{4}(?![\w.])')
ADDRESS = re.compile(r'\b\d{1,5}\s+(?:[A-Za-z]+\s+){1,4}(?:Street|Road|Avenue|Boulevard|Lane|Drive)\b|[\u4e00-\u9fff]{2,}(?:路|街|大道)\d+号', re.I)
MARKER = 'PRIVATE' + '_USER_PROFILE'


def private_path(path):
    parts = PurePosixPath(path.replace('\\', '/')).parts
    return any(part.casefold() == 'private' for part in parts)


def scan_text(text, terms=(), fingerprints=()):
    found = []
    for label, pattern in [('email', EMAIL), ('phone', PHONE), ('precise address', ADDRESS)]:
        if pattern.search(text):
            found.append(label)
    if MARKER in text:
        found.append('private profile marker')
    for term in terms:
        if term and re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)', text, re.I):
            found.append('local private term')
            break
    if any(phrase in text for phrase in fingerprints):
        found.append('private overlay excerpt')
    return found


def git(root, *args):
    r = subprocess.run(['git', '-C', str(root), *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode:
        raise RuntimeError('Git inspection failed: ' + ' '.join(args[:2]))
    return r.stdout


def overlay_rules(root):
    private = root / 'private'
    terms_file = private / 'privacy-terms.json'
    terms = json.loads(terms_file.read_text()) if terms_file.exists() else []
    if not isinstance(terms, list) or any(not isinstance(t, str) for t in terms):
        raise ValueError('local privacy terms must be a JSON list of strings')
    excerpts = []
    if private.exists():
        for path in private.rglob('*.md'):
            for paragraph in re.split(r'\n\s*\n', path.read_text()):
                paragraph = paragraph.strip()
                if len(paragraph) >= 80 and not paragraph.startswith('#'):
                    excerpts.append(paragraph)
    return terms, excerpts


def validate_repo(root, include_history=True):
    root = Path(root).resolve()
    actual = Path(git(root, 'rev-parse', '--show-toplevel').decode().strip()).resolve()
    if actual != root:
        raise RuntimeError('Run in the skill repository, not a parent repository')
    terms, excerpts = overlay_rules(root)
    findings = []
    def check(path, data, location):
        if private_path(path):
            findings.append(f'{location}:{path}: private path tracked')
        # A public binary/symlink needs manual review rather than a silent skip.
        try:
            text = data.decode('utf-8')
        except UnicodeDecodeError:
            findings.append(f'{location}:{path}: non-text blob requires review')
            return
        for reason in scan_text(text, terms, excerpts):
            findings.append(f'{location}:{path}: {reason}')
    entries = git(root, 'ls-files', '--stage', '-z').split(b'\0')
    if not any(entries):
        raise RuntimeError('No indexed files: stage the public candidate before validation')
    for entry in entries:
        if not entry:
            continue
        info, rawpath = entry.split(b'\t', 1)
        mode, oid, stage = info.decode().split()
        path = rawpath.decode()
        if mode != '100644' and mode != '100755':
            findings.append(f'index:{path}: unsupported mode/symlink/submodule')
        if stage != '0':
            findings.append(f'index:{path}: unresolved merge stage')
        check(path, git(root, 'cat-file', 'blob', oid), 'index')
        disk = root / path
        if disk.is_file() and not disk.is_symlink():
            check(path, disk.read_bytes(), 'worktree')
        elif disk.is_symlink():
            findings.append(f'worktree:{path}: symlink requires review')
    if include_history:
        commits = git(root, 'rev-list', '--all').decode().splitlines()
        seen = set()
        for commit in commits:
            for reason in scan_text(git(root, 'show', '-s', '--format=%B', commit).decode(), terms, excerpts):
                findings.append(f'history:{commit[:12]}: commit message {reason}')
            for entry in git(root, 'ls-tree', '-r', '-z', commit).split(b'\0'):
                if not entry:
                    continue
                info, rawpath = entry.split(b'\t', 1)
                mode, kind, oid = info.decode().split()
                path = rawpath.decode()
                if private_path(path):
                    findings.append(f'history:{commit[:12]}:{path}: private path tracked')
                if kind != 'blob' or mode not in ('100644', '100755'):
                    findings.append(f'history:{commit[:12]}:{path}: unsupported tree entry')
                    continue
                if oid not in seen:
                    check(path, git(root, 'cat-file', 'blob', oid), f'history:{commit[:12]}')
                    seen.add(oid)
    return sorted(set(findings))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = p.parse_args()
    try:
        findings = validate_repo(args.root)
    except (ValueError, RuntimeError, OSError, json.JSONDecodeError) as exc:
        print(f'PRIVACY FAIL: {exc}')
        return 1
    if findings:
        print('PRIVACY FAIL\n' + '\n'.join(findings))
        return 1
    print('PRIVACY PASS: index, tracked worktree, and reachable history; no private paths or detected identifiers/overlay excerpts.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
