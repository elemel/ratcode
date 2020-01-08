from fractions import Fraction
from math import gcd

from ratcode.memory import load as load_memory
from ratcode.memory import load_integer as load_integer_memory
from ratcode.memory import store as store_memory
from ratcode.memory import store_integer as store_integer_memory


# registers[a] = b
def _constant(registers, memory, size):
    ip = int(registers[0])
    registers[0] += 2 + 2 * size

    a = memory[ip + 1]
    registers[a] = load_memory(memory, ip + 2, size)


# registers[a] = b
def _constant_integer(registers, memory, size):
    ip = int(registers[0])
    registers[0] += 2 + size

    a = memory[ip + 1]
    registers[a] = load_integer_memory(memory, ip + 2, size)


# registers[a] = memory[registers[a]]
def _load(registers, memory, size):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    registers[a] = load_memory(memory, registers[a], size)


# registers[a] = memory[registers[a]]
def _load_integer(registers, memory, size):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    registers[a] = load_integer_memory(memory, registers[a], size)


# memory[registers[a]] = registers[b]
def _store(registers, memory, size):
    ip = int(registers[0])
    registers[0] += 3

    a = memory[ip + 1]
    b = memory[ip + 2]

    store_memory(memory, registers[a], registers[b], size)


# memory[registers[a]] = registers[b]
def _store_integer(registers, memory, size):
    ip = int(registers[0])
    registers[0] += 3

    a = memory[ip + 1]
    b = memory[ip + 2]

    store_integer_memory(memory, registers[a], registers[b], size)


# registers[a] += registers[b]
def add(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 3

    a = memory[ip + 1]
    b = memory[ip + 2]

    registers[a] += registers[b]


# registers[a] = b
def constant(registers, memory, files):
    _constant(registers, memory, 4)


# registers[a] = b
def constant_byte(registers, memory, files):
    _constant(registers, memory, 1)


# registers[a] = b
def constant_integer(registers, memory, files):
    _constant_integer(registers, memory, 4)


# registers[a] = b
def constant_integer_byte(registers, memory, files):
    _constant_integer(registers, memory, 1)


# registers[a] = b
def constant_integer_long(registers, memory, files):
    _constant_integer(registers, memory, 8)


# registers[a] = b
def constant_integer_short(registers, memory, files):
    _constant_integer(registers, memory, 2)


# registers[a] = b
def constant_long(registers, memory, files):
    _constant(registers, memory, 8)


# registers[a] = b
def constant_short(registers, memory, files):
    _constant(registers, memory, 2)


# registers[a] -= 1
def decrement(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    registers[a] -= 1


# registers[a] /= registers[b]
def divide(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 3

    a = memory[ip + 1]
    b = memory[ip + 2]

    registers[a] /= registers[b]


# registers[a] += 1
def increment(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    registers[a] += 1


# registers[a] = 1 / registers[a]
def invert(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    registers[a] = 1 / registers[a]


# goto registers[a]
def jump(registers, memory, files):
    ip = int(registers[0])
    a = memory[ip + 1]
    registers[0] = registers[a]


# goto registers[a] if registers[b] == 0 
def jump_equal_to(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    b = memory[ip + 2]

    if registers[b] == 0:
        registers[0] = registers[a]


# goto registers[a] if registers[b] >= 0
def jump_greater_equal(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    b = memory[ip + 2]

    if registers[b] >= 0:
        registers[0] = registers[a]


# goto registers[a] if registers[b] > 0
def jump_greater_than(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    b = memory[ip + 2]

    if registers[b] > 0:
        registers[0] = registers[a]


# goto registers[a] if registers[b] <= 0
def jump_less_equal(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    b = memory[ip + 2]

    if registers[b] <= 0:
        registers[0] = registers[a]


# goto registers[a] if registers[b] < 0
def jump_less_than(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    b = memory[ip + 2]

    if registers[b] < 0:
        registers[0] = registers[a]


# goto registers[a] if registers[b] != 0
def jump_not_equal(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    b = memory[ip + 2]

    if registers[b] != 0:
        registers[0] = registers[a]


# registers[a] = memory[registers[a]]
def load(registers, memory, files):
    _load(registers, memory, 4)


# registers[a] = memory[registers[a]]
def load_byte(registers, memory, files):
    _load(registers, memory, 1)


# registers[a] = memory[registers[a]]
def load_integer(registers, memory, files):
    _load_integer(registers, memory, 4)


# registers[a] = memory[registers[a]]
def load_integer_byte(registers, memory, files):
    _load_integer(registers, memory, 1)


# registers[a] = memory[registers[a]]
def load_integer_long(registers, memory, files):
    _load_integer(registers, memory, 8)


# registers[a] = memory[registers[a]]
def load_integer_short(registers, memory, files):
    _load_integer(registers, memory, 2)


# registers[a] = memory[registers[a]]
def load_long(registers, memory, files):
    _load(registers, memory, 8)


# registers[a] = memory[registers[a]]
def load_short(registers, memory, files):
    _load(registers, memory, 2)


# registers[a] *= registers[b]
def multiply(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 3

    a = memory[ip + 1]
    b = memory[ip + 2]

    registers[a] *= registers[b]


# registers[a] = -registers[a]
def negate(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    registers[a] = -registers[a]


# pass
def noop(registers, memory, files):
    registers[0] += 1


# registers[a] = files[registers[a]].popleft()
def read(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    fh = int(registers[a])
    assert fh >= 0, 'Invalid file handle'

    registers[a] = Fraction(files[fh].popleft())


# memory[registers[a]] = registers[b]
def store(registers, memory, files):
    _store(registers, memory, 4)


# memory[registers[a]] = registers[b]
def store_byte(registers, memory, files):
    _store(registers, memory, 1)


# memory[registers[a]] = registers[b]
def store_integer(registers, memory, files):
    _store_integer(registers, memory, 4)


# memory[registers[a]] = registers[b]
def store_integer_byte(registers, memory, files):
    _store_integer(registers, memory, 1)


# memory[registers[a]] = registers[b]
def store_integer_long(registers, memory, files):
    _store_integer(registers, memory, 8)


# memory[registers[a]] = registers[b]
def store_integer_short(registers, memory, files):
    _store_integer(registers, memory, 2)


# memory[registers[a]] = registers[b]
def store_long(registers, memory, files):
    _store(registers, memory, 8)


# memory[registers[a]] = registers[b]
def store_short(registers, memory, files):
    _store(registers, memory, 2)


# registers[a] -= registers[b]
def subtract(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 3

    a = memory[ip + 1]
    b = memory[ip + 2]

    registers[a] -= registers[b]


# registers[a] = int(registers[a])
def truncate(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 2

    a = memory[ip + 1]
    registers[a] = int(registers[a])


# files[registers[a]].append(registers[b])
def write(registers, memory, files):
    ip = int(registers[0])
    registers[0] += 3

    a = memory[ip + 1]
    b = memory[ip + 2]

    fh = int(registers[a])
    assert fh >= 0, 'Invalid file handle'

    files[fh].append(int(registers[b]) % 256)


OPCODE_TO_NAME = 256 * [None]
OPCODE_TO_NAME[0] = 'noop'

# Randomly assign all opcodes except noop
OPCODE_TO_NAME[5] = 'load_byte'
OPCODE_TO_NAME[11] = 'constant_integer_byte'
OPCODE_TO_NAME[23] = 'constant_integer'
OPCODE_TO_NAME[25] = 'invert'
OPCODE_TO_NAME[38] = 'load_integer_long'
OPCODE_TO_NAME[41] = 'jump_less_than'
OPCODE_TO_NAME[44] = 'add'
OPCODE_TO_NAME[48] = 'load_integer_byte'
OPCODE_TO_NAME[54] = 'truncate'
OPCODE_TO_NAME[55] = 'constant'
OPCODE_TO_NAME[60] = 'increment'
OPCODE_TO_NAME[62] = 'decrement'
OPCODE_TO_NAME[75] = 'negate'
OPCODE_TO_NAME[97] = 'load_short'
OPCODE_TO_NAME[122] = 'store_integer_long'
OPCODE_TO_NAME[126] = 'multiply'
OPCODE_TO_NAME[128] = 'constant_byte'
OPCODE_TO_NAME[133] = 'read'
OPCODE_TO_NAME[134] = 'store'
OPCODE_TO_NAME[135] = 'load_integer'
OPCODE_TO_NAME[138] = 'jump_not_equal'
OPCODE_TO_NAME[156] = 'divide'
OPCODE_TO_NAME[159] = 'jump_equal_to'
OPCODE_TO_NAME[163] = 'constant_long'
OPCODE_TO_NAME[165] = 'write'
OPCODE_TO_NAME[174] = 'constant_integer_long'
OPCODE_TO_NAME[178] = 'jump'
OPCODE_TO_NAME[179] = 'jump_greater_equal'
OPCODE_TO_NAME[181] = 'store_integer_byte'
OPCODE_TO_NAME[183] = 'store_short'
OPCODE_TO_NAME[186] = 'jump_greater_than'
OPCODE_TO_NAME[187] = 'constant_integer_short'
OPCODE_TO_NAME[191] = 'store_byte'
OPCODE_TO_NAME[193] = 'constant_short'
OPCODE_TO_NAME[198] = 'store_integer'
OPCODE_TO_NAME[203] = 'store_long'
OPCODE_TO_NAME[205] = 'load'
OPCODE_TO_NAME[208] = 'store_integer_short'
OPCODE_TO_NAME[228] = 'subtract'
OPCODE_TO_NAME[232] = 'load_long'
OPCODE_TO_NAME[236] = 'load_integer_short'
OPCODE_TO_NAME[238] = 'jump_less_equal'

MNEMONIC_TO_NAME = dict(
    ADD='add',
    CIB='constant_integer_byte',
    CIN='constant_integer',
    CIL='constant_integer_long',
    CIS='constant_integer_short',
    COB='constant_byte',
    COL='constant_long',
    CON='constant',
    COS='constant_short',
    DEC='decrement',
    DIV='divide',
    INC='increment',
    INV='invert',
    JET='jump_equal_to',
    JGE='jump_greater_equal',
    JGT='jump_greater_than',
    JLE='jump_less_equal',
    JLT='jump_less_than',
    JMP='jump',
    JNE='jump_not_equal',
    LIB='load_integer_byte',
    LIL='load_integer_long',
    LIN='load_integer',
    LIS='load_integer_short',
    LOB='load_byte',
    LOD='load',
    LOL='load_long',
    LOS='load_short',
    MUL='multiply',
    NEG='negate',
    NOP='noop',
    RED='read',
    RIT='write',
    SIB='store_integer_byte',
    SIL='store_integer_long',
    SIN='store_integer',
    SIS='store_integer_short',
    STB='store_byte',
    STL='store_long',
    STR='store',
    STS='store_short',
    SUB='subtract')

NAME_TO_OPCODE = {
    name: opcode
    for opcode, name in enumerate(OPCODE_TO_NAME)
    if name
}

OPCODE_TO_OPERATION = [name and globals()[name] for name in OPCODE_TO_NAME]
