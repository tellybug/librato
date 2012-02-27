# Copyright (c) 2012 Matt Millar http://tellybug.com
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""

to run the testcode create a file

acc_keys.py

with two lines

LibratoUsername = "email@example.com"
LibratoAPIKey = "APIUSERKEYHERE"

"""

import unittest
import sys

import os.path

# convoluted as we want the python path to include the parent directory
SOURCE_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(SOURCE_ROOT, os.path.pardir)))

from librato.connection import LibratoConnection
from librato import exceptions

from acc_keys import LibratoUsername, LibratoAPIKey

class TestLibratoAPI(unittest.TestCase):

    def setUp(self):
        # these are test account keys - replace with your own!
        self.libratoUser = LibratoUsername
        self.libratoAPIKey = LibratoAPIKey

    def test_create_gauge(self):
        connection = LibratoConnection(self.libratoUser,self.libratoAPIKey)
        gauge = connection.get_or_create_gauge("py-test-gauge","created by testcode")
        self.assertEquals(gauge.name,'py-test-gauge')
        connection.delete_gauge('py-test-gauge')
        self.assertRaises(exceptions.NotFound,lambda:connection.get_gauge('py-test-gauge'))

if __name__ == '__main__':
    unittest.main()