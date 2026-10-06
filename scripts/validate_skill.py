#!/usr/bin/env python3
"""Structural checks complement, but cannot replace, semantic acceptance review."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REFS = ['unified-relational-inference-theory','literature-review','formal-model','information-theory',
        'statistical-dynamics','probabilistic-pragmatics','reasoning-framework','evidence-model',
        'relationship-state-model','narrative-identity','psychology-lenses','astrology-mbti-policy',
        'existential-literary-lens','response-style','epistemic-boundaries','privacy','examples']
SCRIPTS = ['belief_update','information_metrics','state_dynamics','validate_privacy','validate_skill']
ASSETS = ['person-model','relationship-model','evidence-event','hypothesis-set']
TERMS = ['Bayesian','entropy','conditional entropy','mutual information','KL divergence',
         'maximum entropy','coarse-graining','microstate','macrostate','metastability','path dependence',
         'state-space','CAPS','Whole Trait Theory','narrative identity','partner responsiveness',
         'autonomy support','Rational Speech Act','falsifiability','limitations']


def validate():
    errors=[]
    required=['SKILL.md','README.md','LICENSE','.gitignore','assets/analysis-template.md',
              'tests/test_reasoning_contract.md','references/literature-metadata.json']
    required += [f'references/{name}.md' for name in REFS]
    required += [f'scripts/{name}.py' for name in SCRIPTS]
    required += [f'assets/{name}.schema.json' for name in ASSETS]
    required += [f'tests/test_{name}.py' for name in ['belief_update','information_metrics','state_dynamics','privacy']]
    for relative in required:
        p=ROOT/relative
        if not p.is_file() or not p.read_text().strip():errors.append('Missing/empty '+relative)
    skill=(ROOT/'SKILL.md').read_text()
    match=re.match(r'\A---\n(.*?)\n---\n',skill,re.S)
    if not match:
        errors.append('Missing YAML frontmatter')
    else:
        front=dict(line.split(':',1) for line in match.group(1).splitlines())
        if front.get('name','').strip()!='emotional-analysis':errors.append('Incorrect skill name')
        if not 20<len(front.get('description','').strip())<=1024:errors.append('Description length')
    if len(skill.splitlines())>500:errors.append('Entry point exceeds 500 lines')
    for path in ROOT.rglob('*.md'):
        if 'private' in path.relative_to(ROOT).parts:continue
        text=path.read_text()
        if re.search(r'\b(?:TODO|TBD|FIXME)\b',text):errors.append('Unfinished scaffold '+str(path.relative_to(ROOT)))
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
            if target.startswith(('https://','http://','#')):continue
            dest=(path.parent/target.split('#')[0]).resolve()
            if not dest.is_relative_to(ROOT) or not dest.exists():errors.append('Broken/escaping link '+target)
    theory=(ROOT/'references/unified-relational-inference-theory.md').read_text()
    for term in TERMS:
        lines=[line for line in theory.splitlines() if term.casefold() in line.casefold()]
        if not lines or not any(len(line.split())>=12 for line in lines):errors.append('Missing explanatory coverage: '+term)
    if not re.search(r'(?:neither|not) an empirically',theory) or 'countermodel' not in theory or 'contested' not in theory:
        errors.append('Missing epistemic boundaries')
    for name in ASSETS:
        obj=json.loads((ROOT/f'assets/{name}.schema.json').read_text())
        if obj.get('$schema')!='https://json-schema.org/draft/2020-12/schema':errors.append('Schema dialect '+name)
        if not set(obj.get('required',[]))<=set(obj.get('properties',{})):errors.append('Schema required fields '+name)
        if obj.get('additionalProperties') is not False:errors.append('Schema openness '+name)
    metadata=json.loads((ROOT/'references/literature-metadata.json').read_text())
    review=(ROOT/'references/literature-review.md').read_text()
    records=metadata['records']
    if len(records)<29:errors.append('Insufficient verified bibliography')
    for row in records:
        if not all(row.get(k) for k in ['doi','title','authors','year','journal','verified_at','verification_source']):
            errors.append('Incomplete bibliography record')
        if row['doi'] not in review:errors.append('Uncited verified DOI '+row['doi'])
    for doi in set(re.findall(r'https://doi.org/([^\s)]+)',review)):
        if doi not in {r['doi'] for r in records}:errors.append('Unverified cited DOI '+doi)
    contract=(ROOT/'tests/test_reasoning_contract.md').read_text()
    if len(re.findall(r'^\d+\.',contract,re.M))<25:errors.append('Insufficient semantic fixtures')
    if '/private/' not in (ROOT/'.gitignore').read_text().splitlines():errors.append('Private overlay not ignored')
    return errors


if __name__=='__main__':
    try:errors=validate()
    except (OSError,ValueError,KeyError) as exc:errors=[str(exc)]
    if errors:
        print('SKILL FAIL\n'+'\n'.join(errors));sys.exit(1)
    print('SKILL PASS: structure, local links, schemas, theory coverage and DOI provenance. Semantic review remains a human acceptance gate.')
