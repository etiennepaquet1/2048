import Move
from random import randint, choice
from ui import *


def printGrid(grid):
    for row in grid:
        print(row)


def updateUI():
    for y in range(4):
        for x in range(4):
            labels[y][x].config(text=grid[y][x])


def addNewNumber(emptyCells, grid):
    if not emptyCells: pass
    try:
        n = randint(0, len(emptyCells) - 1)
    except ValueError:
        print("Game Over. Better luck next time!")
        game_over_label.config(text="Game Over. Better luck next time!", font=("Helvetica", 48))
        left_button.config(command=lambda: None)
        right_button.config(command=lambda: None)
        up_button.config(command=lambda: None)
        down_button.config(command=lambda: None)

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


def turn(direction):
    move(Move.moveDict[direction], grid)
    emptyCells = [(y, x) for y in range(4) for x in range(4) if not grid[y][x]]
    if not addNewNumber(emptyCells, grid): return
    updateUI()


def initializeCommands():
    left_button.config(command=lambda: turn('l'))
    right_button.config(command=lambda: turn('r'))
    up_button.config(command=lambda: turn('u'))
    down_button.config(command=lambda: turn('d'))


def main():
    global grid
    grid = [[0] * 4 for _ in range(4)]
    emptyCells = [(y, x) for y in range(4) for x in range(4)]
    addNewNumber(emptyCells, grid)
    initializeCommands()
    updateUI()


if __name__ == '__main__':
    retry_button = tk.Button(master=root, text="Retry", command=main)
    retry_button.pack()

    main()
    root.mainloop()
