import Move
from random import randint, choice


def printGrid(grid):
    for row in grid:
        print(row)


def addNewNumber(emptyCells, grid):
    if not emptyCells: pass
    try:
        n = randint(0, len(emptyCells) - 1)
    except ValueError:
        print("Game Over. Better luck next time!")
        return False
    y, x = emptyCells[n]
    grid[y][x] = choice([2, 4])
    emptyCells.pop(n)
    return True


def processRow(row, direction):
    # Move digits left or right
    row2 = [num for num in row if num]
    row = row2 + [0] * (4 - len(row2)) if direction.inc == 1 else [0] * (4 - len(row2)) + row2

    # Combine digits that go together
    for x in range(direction.start, direction.stop, direction.inc):
        if row[x] == row[x + direction.inc] != 0:
            row[x] *= 2
            row[x + direction.inc] = 0

    # Move digits left or right for a second time
    row2 = [num for num in row if num]
    return row2 + [0] * (4 - len(row2)) if direction.inc == 1 else [0] * (4 - len(row2)) + row2


def move(direction: Move, grid):
    if direction.x:
        for y, row in enumerate(grid):
            res = processRow(row, direction)
            grid[y] = res
    else:
        for x in range(4):
            col = [row[x] for row in grid]
            res = processRow(col, direction)
            for y, val in enumerate(res):
                grid[y][x] = val


def main():
    grid = [[0] * 4 for i in range(4)]
    while True:
        emptyCells = [(y, x) for y in range(4) for x in range(4) if not grid[y][x]]
        if not addNewNumber(emptyCells, grid): return
        printGrid(grid)
        while True:
            try:
                m = Move.moveDict[input("Make your move")]
            except KeyError:
                print('Invalid Move.')
            else:
                break
        move(m, grid)


if __name__ == '__main__':
    while True:
        i = input('Welcome to 2048! Type "p" to play, or "e" to exit.')
        if i == 'e': exit()
        elif i == 'p': main()
        else: print('Invalid input')
