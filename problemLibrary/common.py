import os

INSTANCE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instances')


def read_maxcut_instance(size, degree = 3):
    file_path = os.path.join(INSTANCE_DIR ,f"mc_{size:03d}_{degree:03d}_000.txt")
    try:
        with open(file_path, 'r') as file:
            nodes = int(file.readline())
            edges = []
            for line in file.readlines():
                parts = line.split()
                edges.append((int(parts[0]), int(parts[1])))

        return nodes, edges
    except Exception as e:
        print(e)
        return None, None

def read_maxcut_solution(size, degree = 3):
    file_path = os.path.join(INSTANCE_DIR, f"mc_{size:03d}_{degree:03d}_000.sol")
    try:
        with open(file_path, 'r') as file:
            objective = int(file.readline())
            solution = [int(v) for v in file.readline().split()]

        return objective, solution
    except Exception as e:
        print(e)
        return None, None

def eval_cut(nodes, edges, solution):
    assert(nodes == len(solution))

    cut_size = 0
    for i,j in edges:
        if solution[i] != solution[j]:
            cut_size += 1

    return cut_size
