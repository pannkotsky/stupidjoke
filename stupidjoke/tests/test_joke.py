import unittest

from stupidjoke import joke


class TestJoke(unittest.TestCase):
    def test_is_string(self):
        s = joke.joke()
        self.assertTrue(isinstance(s, basestring))
