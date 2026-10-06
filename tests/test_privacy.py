from pathlib import Path
import subprocess
import tempfile
import unittest
from scripts.validate_privacy import validate_repo, scan_text, private_path


class PrivacyTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.git('init','-q')
        self.git('config','user.name','Test Contributor')
        self.git('config','user.email','test'+'@'+'example.invalid')

    def git(self,*args):
        return subprocess.run(['git','-C',str(self.root),*args],check=True,capture_output=True)

    def stage(self,path,content):
        p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
        self.git('add','--',path)

    def test_clean_public_repo(self):
        self.stage('README.md','Generic emotional reasoning.\n')
        self.assertEqual(validate_repo(self.root),[])

    def test_private_path(self):
        self.stage('private/profile.md','local only')
        self.assertTrue(any('private path' in x for x in validate_repo(self.root)))
        self.assertTrue(private_path('folder/private/profile.md'))
        self.assertFalse(private_path('references/privacy.md'))

    def test_pii_patterns(self):
        email='someone'+'@'+'example.invalid'
        phone='138'+'12345678'
        address='123'+' Fictional Street'
        for value,kind in [(email,'email'),(phone,'phone'),(address,'precise address')]:
            self.assertIn(kind,scan_text(value))
        self.assertIn('private profile marker',scan_text('PRIVATE'+'_USER_PROFILE'))

    def test_index_blob_cannot_be_hidden_by_clean_worktree(self):
        self.stage('README.md','someone'+'@'+'example.invalid')
        (self.root/'README.md').write_text('Clean now')
        self.assertTrue(any('index:' in x and 'email' in x for x in validate_repo(self.root)))

    def test_history_catches_deleted_private_file(self):
        self.stage('private/data.md','sensitive')
        self.git('commit','-qm','Initial')
        self.git('rm','private/data.md')
        self.stage('README.md','Generic')
        self.git('commit','-qm','Remove')
        self.assertTrue(any('history:' in x and 'private path' in x for x in validate_repo(self.root)))

    def test_history_catches_prior_pii(self):
        self.stage('README.md','someone'+'@'+'example.invalid')
        self.git('commit','-qm','Initial')
        self.stage('README.md','Clean now')
        self.git('commit','-qm','Update')
        self.assertTrue(any('history:' in x and 'email' in x for x in validate_repo(self.root)))

    def test_private_overlay_excerpt_and_terms(self):
        private=self.root/'private';private.mkdir()
        text='A confidential narrative detail should remain local rather than enter the general public skill repository.'
        (private/'user-profile.md').write_text(text)
        self.stage('references/example.md',text)
        self.assertTrue(any('overlay excerpt' in x for x in validate_repo(self.root)))

    def test_empty_index_fails_closed(self):
        with self.assertRaises(RuntimeError):validate_repo(self.root)
