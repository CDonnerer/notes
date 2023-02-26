import itertools

def neighbours(points):
    x, y = points
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1 
    yield x + 1, y + 1
    yield x + 1, y - 1
    yield x - 1, y + 1
    yield x - 1, y - 1

def advance(board):
    newstate = set()
    recalc = board | set(itertools.chain(*map(neighbours, board)))

    for point in recalc:
        count = sum(
            (neighbour in board)
            for neighbour in neighbours(point)
        )
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)
    return newstate

glider = set([(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)])

for i in range(100):
    glider = advance(glider)

print(glider)
