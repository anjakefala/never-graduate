'''
4.1 Computing the parity of a word

The parity of a binary word is 1 if the number of 1s in the wor is odd; otherwise, it is 0. For example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used to detect single bit errors in data storage and communication. It is fairly straightforward to write code that computes the parity of a single 64-bit word.

How would you compute the parity of a very large number of 64-bit words?

Hint: Use a lookup table, but don't use 2^64 entries!
'''

import unittest
from compute_parity import parity

class ParityTests(unittest.TestCase):

    def test_simple_parity_one(self):
        par = parity(11)
        self.assertEqual(par, 1)

    def test_simple_parity_zero(self):
        par = parity(136)
        self.assertEqual(par, 0)
