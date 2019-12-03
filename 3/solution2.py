def read_input():
    with open('input') as input_file:
        return list(map(str.strip, input_file.readlines()))


def handle_r(coordinate_pair):
    return (coordinate_pair[0] + 1, coordinate_pair[1])


def handle_l(coordinate_pair):
    return (coordinate_pair[0] - 1, coordinate_pair[1])


def handle_u(coordinate_pair):
    return (coordinate_pair[0], coordinate_pair[1] + 1)


def handle_d(coordinate_pair):
    return (coordinate_pair[0], coordinate_pair[1] - 1)


def generate_path(wire_direction):
    wire_direction = wire_direction.split(',')
    wire_path = [(0,0)]

    for instruction in wire_direction:
        direction = instruction[0]
        steps = int(instruction[1:])

        for i in range(steps):
            coordinate_pair = []
            if direction == 'R':
                coordinate_pair = handle_r(wire_path[-1])
            elif direction == 'L':
                coordinate_pair = handle_l(wire_path[-1])
            elif direction == 'U':
                coordinate_pair = handle_u(wire_path[-1])
            elif direction == 'D':
                coordinate_pair = handle_d(wire_path[-1])
            wire_path.append(coordinate_pair)

    return wire_path[1:]


def manhattan_distance(point):
    source = (0,0)
    return abs(source[0] - point[0]) + abs(source[1] - point[1])


def combined_steps(wire_path1, wire_path2, intersection_point):
    wire_path1_steps = wire_path1.index(intersection_point) + 1
    wire_path2_steps = wire_path2.index(intersection_point) + 1
    return wire_path1_steps + wire_path2_steps


if __name__== "__main__":
    wire_directions = read_input()
    wire_paths = list(map(generate_path, wire_directions))
    intersections = list(set(wire_paths[0]) & set(wire_paths[1]))
    manhattan_distances = list(map(manhattan_distance, intersections))
    #print(intersections)
    combined_steps = list(map(lambda intersection: combined_steps(wire_paths[0], wire_paths[1], intersection), intersections))
    print('combined steps: {}'.format(min(combined_steps)))