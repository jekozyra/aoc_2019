import copy

def read_input():
    with open('input2') as input_file:
        return list(map(int, input_file.readline().split(',')))

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


def find_target(target):
    for noun in range(100):
        for verb in range(100):
            opcodes = read_input()
            opcodes[1], opcodes[2] = noun, verb
            output = handle_opcodes(opcodes)

            if target == output[0]:
                return noun * 100 + verb


if __name__== "__main__":
    target = 19690720
    print(find_target(target))
