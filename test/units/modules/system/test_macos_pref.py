
from ansible.compat.tests import unittest
from ansible.modules.system.macos_pref import CFPreferences


class TestCPreferences(unittest.TestCase):
    def test_read_nsglobaldomain(self):
        preferences = CFPreferences('NSGlobalDomain')
        out = preferences.read('Bool1')
        self.assertTrue(out is None)

    def test_read_anyuser(self):
        preferences = CFPreferences('com.ansible.osx_defaults', user='anyUser')
        out = preferences.read('SomeKey')
        self.assertTrue(out is None)

    def test_read_nsglobaldomain_anyuser(self):
        preferences = CFPreferences('NSGlobalDomain', user='anyUser')
        out = preferences.read('Bool1')
        self.assertTrue(out is None)

    def test_read_nonexistant_domain(self):
        preferences = CFPreferences('com.ansible.nonexistant_read')
        out = preferences.read('Bool1')
        self.assertTrue(out is None)

