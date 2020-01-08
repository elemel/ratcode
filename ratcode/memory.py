from fractions import Fraction


def load(memory, address, size=4):
    address = int(address)
    assert address >= 0, 'Invalid address'

    numerator = int.from_bytes(
        memory[address:address + size], 'big', signed=True)

    denominator = int.from_bytes(
        memory[address + size:address + 2 * size], 'big', signed=False)

    return Fraction(numerator, denominator)


def load_integer(memory, address, size=4):
    address = int(address)
    assert address >= 0, 'Invalid address'

    return Fraction(
        int.from_bytes(memory[address:address + size], 'big', signed=True))


def store(memory, address, rational, size=4):
    address = int(address)
    assert address >= 0, 'Invalid address'

    modulus = 1 << (8 * size)

    memory[address:address + size] = int.to_bytes(
        rational.numerator % modulus, size, 'big', signed=False)

    memory[address + size:address + 2 * size] = int.to_bytes(
        rational.denominator % modulus, size, 'big', signed=False)


def store_integer(memory, address, rational, size=4):
    address = int(address)
    assert address >= 0, 'Invalid address'

    modulus = 1 << (8 * size)

    memory[address:address + size] = int.to_bytes(
        int(rational) % modulus, size, 'big', signed=False)
