from collections import deque

def read_input():
    with open('input') as input_file:
        return list(map(str.strip, input_file.readlines()))

def build_graph(orbit_map):
    graph = {}
    points = []
    for orbit in orbit_map:
        parent, child = orbit.split(')')

        if parent not in graph:
            graph[parent] = []

        if child not in graph:
            graph[child] = []

        graph[parent].append(child)
        graph[child].append(parent)
        points.append(parent)
        points.append(child)

    points = list(set(points))

    for point in points:
        if point not in graph:
            graph[point] = []

    return graph


def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def generate_distances(source, graph, destination=None):
    points = list(set(graph.keys()))
    visited = dict(zip(points, [None]*len(points)))
    queue = [(source, 0)]
    visited[source] = 0
    parent = {}

    while queue:
        node, current_depth = queue.pop(0)

        if destination and node == destination:
            return backtrace(parent, source, destination)

        if node in graph:
            for child in graph[node]:
                if visited[child] == None:
                    queue.append((child, current_depth + 1))
                    visited[child] = current_depth + 1
                    parent[child] = node

    return visited


if __name__== "__main__":
    orbit_map = read_input()
    graph = build_graph(orbit_map)
    print('distances from COM: {}'.format(sum(generate_distances('COM', graph).values())))
    you_source = [k for k,v in graph.items() if 'YOU' in v][0]
    san_dest = [k for k,v in graph.items() if 'SAN' in v][0]
    path = generate_distances(you_source, graph, san_dest)
    print('distances from YOU to SAN: {}'.format(len(path) - 1))