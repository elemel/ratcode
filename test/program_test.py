import unittest

from ratcode import memory
from ratcode.operations import NAME_TO_OPCODE
from ratcode.program import Program


class ProgramTest(unittest.TestCase):
    def test_program(self):
        program = Program()

        program.memory[0] = NAME_TO_OPCODE['constant_integer_byte']
        program.memory[1] = 255
        program.memory[2] = 3

        program.memory[3] = NAME_TO_OPCODE['constant_integer_byte']
        program.memory[4] = 254
        program.memory[5] = 13

        program.memory[6] = NAME_TO_OPCODE['write']
        program.memory[7] = 255
        program.memory[8] = 254

        program.run()
        self.assertEqual(program.files[3].pop(), 13)


if __name__ == '__main__':
    unittest.main()
