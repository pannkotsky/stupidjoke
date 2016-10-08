import mock
import unittest

from stupidjoke.cmd import stupid_joke


class TestCmd(unittest.TestCase):
    @mock.patch('stupidjoke.joke.joke')
    def test_stupid_joke(self, mock_joke):
        stupid_joke.main()
        mock_joke.assert_called_once()
