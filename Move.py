class Move:
    def __init__(self, y, x, start, stop, inc):
        self.y = y
        self.x = x
        self.start = start
        self.stop = stop
        self.inc = inc


UP = Move(-1, 0, 0, 3, 1)
DOWN = Move(1, 0, 3, 0, -1)
LEFT = Move(0, -1, 0, 3, 1)
RIGHT = Move(0, 1, 3, 0, -1)

moveDict = {"u": UP, 'd': DOWN, 'l': LEFT, 'r': RIGHT}