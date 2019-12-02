def read_input():
    with open('input1') as input_file:
        return list(map(int, input_file.readline().split(',')))

'''
get positions from next two numbers for inputs and output position from third
if 1: add
if 2: multiply
then jump 4 places
if 99: halt
other: raise error
'''
def handle_opcodes(opcodes):
    position = 0
    while position < len(opcodes):
        opcode = opcodes[position]

        if opcode == 1:
            position, opcodes = handle_1(position, opcodes)
        elif opcode == 2:
            position, opcodes = handle_2(position, opcodes)
        elif opcode == 99:
            return opcodes
        else:
            raise ValueError('Invalid opcode {} at position {}.'.format(opcode, position))

    return opcodes


def handle_1(position, opcodes):
    position1, position2, output_position = get_positions(position, opcodes)

    opcodes[output_position] = opcodes[position1] + opcodes[position2]
    return position+4, opcodes


def handle_2(position, opcodes):
    position1, position2, output_position = get_positions(position, opcodes)

    opcodes[output_position] = opcodes[position1] * opcodes[position2]
    return position+4, opcodes


def get_positions(position, opcodes):
    position1 = opcodes[position + 1]
    position2 = opcodes[position + 2]
    output_position = opcodes[position + 3]

    if output_position > len(opcodes):
        raise ValueError('Invalid output position {}.'.format(opcode, position))

    return position1, position2, output_position


if __name__== "__main__":
    opcodes = read_input()
    print('opcodes input: {}'.format(opcodes))
    opcodes = handle_opcodes(opcodes)
    print('opcodes output: {}'.format(opcodes))
