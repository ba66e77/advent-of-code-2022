"""
Rope

rules
-----
1. If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in
    that direction so it remains close enough
2. Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step
    diagonally to keep up

Part 2: Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of
the rope visit at least once?

"""


def part1(data):

    rope = Rope()

    for d in data:
        direction, steps = d.split()
        rope.moveHead(direction, int(steps))

    print(f"Tail visited {len(set(rope.getTailPositionHistory()))} positions.")
    print(rope.getTailPositionHistory())


class Rope:

    def __init__(self):
        self.s = self.headPosition = self.tailPosition = (0, 0)
        self.tailPositionHistory = []
        self._recordTailPositionHistory()

    def moveHead(self, direction: str, steps: int):
        for _ in range(steps):
            self._moveHeadOnePosition(direction)

    def getTailPositionHistory(self):
        return self.tailPositionHistory

    def _moveHeadOnePosition(self, direction: str):
        oldX, oldY = self.headPosition

        match direction:
            # move on Y axis
            case 'U':
                self.headPosition = (oldX, oldY+1)
            case 'D':
                self.headPosition = (oldX, oldY-1)

            # move on X axis
            case 'L':
                self.headPosition = (oldX-1, oldY)
            case 'R':
                self.headPosition = (oldX+1, oldY)

            # Dafuq did you do??
            case _:
                raise Exception(f"Unexpected direction: {direction}")

        self._moveTailOnePosition()

    def _moveTailOnePosition(self):
        # check if move needed
        variance = (self.headPosition[0] - self.tailPosition[0], self.headPosition[1] - self.tailPosition[1])

        if abs(variance[0]) <= 1 and abs(variance[1]) <= 1:
            # no move needed
            return None
        elif (
                (abs(variance[0]) > 1 and abs(variance[1]) >= 1) \
            or
                (abs(variance[0]) >= 1 and abs(variance[1]) > 1) \
            ):
            # move diagonally
            newPosition = (
                self._moveDiagonally(self.tailPosition[0], variance[0]),
                self._moveDiagonally(self.tailPosition[1], variance[1])
            )
        else:
            # figure out which way to move
            newPosition = (
                self._getNewTailCoordinate(self.tailPosition[0], variance[0]),
                self._getNewTailCoordinate(self.tailPosition[1], variance[1])
            )

        # do that shizzit
        self.tailPosition = newPosition

        # record position
        self._recordTailPositionHistory()

    def _getNewTailCoordinate(self, coordinatePosition: int, coordinateVariance: int) -> int:

        if coordinateVariance > 1:
            coordinatePosition += 1
        elif coordinateVariance < -1:
            coordinatePosition -= 1

        return coordinatePosition


    def _moveDiagonally(self, coordinatePosition: int, coordinateVariance: int) -> int:
        """
        @todo: This is inelegant and not DRY. Make it not embarrassing.
        :param coordinatePosition:
        :param coordinateVariance:
        :return:
        """
        if coordinateVariance >= 1:
            coordinatePosition += 1
        elif coordinateVariance <= -1:
            coordinatePosition -= 1

        return coordinatePosition



    def _recordTailPositionHistory(self):
        self.tailPositionHistory.append(self.tailPosition)


if __name__ == '__main__':
    # data = ['R 4',
    #         'U 4',
    #         'L 3',
    #         'D 1',
    #         'R 4',
    #         'D 1',
    #         'L 5',
    #         'R 2'
    #         ]

    inFile = open('./inputData/day9', 'r')
    data = inFile.readlines()
    inFile.close()

    print(len(data))
    part1(data)