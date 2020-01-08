from collections import deque
from fractions import Fraction

from ratcode.operations import OPCODE_TO_OPERATION


class Program:
    def __init__(self):
        self.registers = 256 * [Fraction()]
        self.memory = bytearray(256 * 256)

        self.files = [
            deque(), # stdin
            deque(), # stdout
            deque(), # stderr
            deque(), # exit code
        ]

    def step(self):
        if self.files[3]:
            return False

        ip = int(self.registers[0])
        assert ip >= 0, 'Invalid instruction pointer'

        opcode = self.memory[ip]
        operation = OPCODE_TO_OPERATION[opcode]
        assert operation, 'Invalid opcode'

        operation(self.registers, self.memory, self.files)
        return True

    def run(self):
        while self.step():
            pass
