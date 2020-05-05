from django.test import TestCase


class DummyTest(TestCase):
    """
    Makes sure tests are running properly
    """
    def test(self):
        self.assertTrue(True)
    def test_fail(self):
        self.fail("This should fail")
