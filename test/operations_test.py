from collections import deque
from fractions import Fraction
import unittest

from ratcode import memory
from ratcode import operations


class OperationsTest(unittest.TestCase):
    def setUp(self):
        self.registers = 256 * [Fraction()]
        self.memory = bytearray(256 * 256)

        self.files = [
            deque(), # stdin
            deque(), # stdout
            deque(), # stderr
            deque(), # exit code
        ]

    def test_add(self):
        self.registers[0] = Fraction(32009)
        self.registers[11] = Fraction(7492, -13438)
        self.registers[183] = Fraction(6406, -24330)

        self.memory[32010] = 11
        self.memory[32011] = 183

        operations.add(self.registers, self.memory, self.files)

        self.assertEqual(self.registers[11], Fraction(-268364188, 326946540))
        self.assertEqual(self.registers[0], Fraction(32012))

    def test_divide(self):
        self.registers[0] = Fraction(23436)
        self.registers[181] = Fraction(-33, -10499)
        self.registers[18] = Fraction(28809, -12127)

        self.memory[23437] = 181
        self.memory[23438] = 18

        operations.divide(self.registers, self.memory, self.files)

        self.assertEqual(self.registers[181], Fraction(400191, -302465691))
        self.assertEqual(self.registers[0], Fraction(23439))

    def test_load(self):
        self.registers[0] = Fraction(30652)
        self.registers[68] = Fraction(43718)

        self.memory[30653] = 68
        memory.store(self.memory, 43718, Fraction(-973431086, 1158190758))

        operations.load(self.registers, self.memory, self.files)

        self.assertEqual(self.registers[68], Fraction(-973431086, 1158190758))
        self.assertEqual(self.registers[0], Fraction(30654))

    def test_multiply(self):
        self.registers[0] = Fraction(2681)
        self.registers[148] = Fraction(-30224, -32476)
        self.registers[58] = Fraction(29053, -14473)

        self.memory[2682] = 148
        self.memory[2683] = 58

        operations.multiply(self.registers, self.memory, self.files)

        self.assertEqual(self.registers[148], Fraction(-878097872, 470025148))
        self.assertEqual(self.registers[0], Fraction(2684))

    def test_store(self):
        self.registers[0] = Fraction(7319)
        self.registers[5] = Fraction(54195)
        self.registers[234] = Fraction(-413722681, 525227274)

        self.memory[7320] = 5
        self.memory[7321] = 234

        operations.store(self.registers, self.memory, self.files)

        self.assertEqual(
            memory.load(self.memory, 54195), Fraction(-413722681, 525227274))

        self.assertEqual(self.registers[0], Fraction(7322))

    def test_subtract(self):
        self.registers[0] = Fraction(12771)
        self.registers[185] = Fraction(-9830, -10446)
        self.registers[214] = Fraction(-31594, 17238)

        self.memory[12772] = 185
        self.memory[12773] = 214

        operations.subtract(self.registers, self.memory, self.files)

        self.assertEqual(self.registers[185], Fraction(-499480464, -180068148))
        self.assertEqual(self.registers[0], Fraction(12774))


if __name__ == '__main__':
    unittest.main()
