"""Wire crossings
"""
import numpy as np
from scipy.spatial.distance import cityblock


def get_new_position(current_position, step):
    """Calculate the new postion given current_position and step
    """
    direction = step[0]
    amount = int(step[1:])

    if direction == "R":
        return (current_position[0], current_position[1] + amount)
    elif direction == "L":
        return (current_position[0], current_position[1] - amount)
    elif direction == "U":
        return (current_position[0] - amount, current_position[1])
    elif direction == "D":
        return (current_position[0] + amount, current_position[1])
    else:
        return None


def take_step(grid, current_position, new_position):
    """Take a step
    """
    pos_y = sorted([current_position[0], new_position[0]])
    pos_x = sorted([current_position[1], new_position[1]])

    grid[pos_y[0] : pos_y[1] + 1, pos_x[0] : pos_x[1] + 1] = 1

    return grid


def trace_wire(grid, central_port, wire):
    current_position = central_port

    for step in wire:
        new_position = get_new_position(current_position, step)
        grid = take_step(grid, current_position, new_position)
        current_position = new_position

    return grid.astype(bool).astype(int)


def count_steps(grid, central_port, wire, target):
    current_position = central_port
    steps = 0

    for step in wire:
        new_position = get_new_position(current_position, step)
        grid = np.zeros(shape=(10000, 10000), dtype=np.uint)
        grid = take_step(grid, current_position, new_position)
        steps += grid.sum()
        current_position = new_position

        if grid[target] == 1:
            # print("Found!:", target, current_position)

            grid_s = np.zeros(shape=(10000, 10000), dtype=np.uint)
            grid_s = take_step(grid_s, current_position, target)

            return steps - grid_s.sum()


def main():
    """
    """
    with open("input.dat") as f:
        lines = f.readlines()

    wire_1 = lines[0].strip().split(",")
    wire_2 = lines[1].strip().split(",")

    grid = np.zeros(shape=(10000, 10000), dtype=np.uint)
    # print(grid)

    central_port = (5000, 5000)
    wire_1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
    wire_2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
    # wire_1 = [
    #     "R98",
    #     "U47",
    #     "R26",
    #     "D63",
    #     "R33",
    #     "U87",
    #     "L62",
    #     "D20",
    #     "R33",
    #     "U53",
    #     "R51",
    # ]
    # wire_2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
    # wire_1 = ["R8", "U5", "L5", "D3"]
    # wire_2 = ["U7", "R6", "D4", "L4"]

    grid1 = trace_wire(grid, central_port, wire_1)
    # print(grid1)

    grid = np.zeros(shape=(10000, 10000), dtype=np.uint)

    grid2 = trace_wire(grid, central_port, wire_2)
    # print(grid2)

    intersection = np.where(grid1 + grid2 == 2)
    distances = list()

    for x, y in zip(intersection[0], intersection[1]):
        # print(x, y)
        distances.append(cityblock(central_port, (x, y)))

    print(sorted(distances))

    n_steps = list()

    for x, y in zip(intersection[0], intersection[1]):
        grid = np.zeros(shape=(10000, 10000), dtype=np.uint)
        steps_1 = count_steps(grid, central_port, wire_1, (x, y))
        grid = np.zeros(shape=(10000, 10000), dtype=np.uint)
        steps_2 = count_steps(grid, central_port, wire_2, (x, y))

        n_steps.append(steps_1 + steps_2)

    # 9004 is too low
    print(sorted(n_steps))


if __name__ == "__main__":
    main()
