import unittest
import sys

import os.path

# convoluted as we want the python path to include the parent directory
SOURCE_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(SOURCE_ROOT, os.path.pardir)))

from librato.connection import LibratoConnection
from librato import exceptions

class TestLibratoAPI(unittest.TestCase):

    def setUp(self):
        # these are test account keys - replace with your own!
        self.libratoUser = "matt+test@tellybug.com"
        self.libratoAPIKey = "397e1696c87e35cb9b99bf557026ccdca3b1fe17f3ac94f669c8a051d7f7b8b7"

    def test_create_gauge(self):
        connection = LibratoConnection(self.libratoUser,self.libratoAPIKey)
        gauge = connection.get_or_create_gauge("py-test-gauge","created by testcode")
        self.assertEquals(gauge.name,'py-test-gauge')
        connection.delete_gauge('py-test-gauge')
        self.assertRaises(exceptions.NotFound,lambda:connection.get_gauge('py-test-gauge'))

if __name__ == '__main__':
    unittest.main()