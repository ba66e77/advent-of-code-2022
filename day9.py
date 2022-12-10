"""
Rope

rules
-----
1. If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in
    that direction so it remains close enough
2. Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step
    diagonally to keep up

Part 1: Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at
least once?

Part 2: Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of
the rope visit at least once?

"""
def part1(data):

    knots = 2
    rope = Rope(knots)

    for d in data:
        direction, steps = d.split()
        rope.moveHead(direction, int(steps))

    print(f"Part 1: With {knots} knots, tail visited {len(set(rope.getTailPositionHistory()))} positions.")

def part2(data, knots: int):

    rope = Rope(knots)

    for d in data:
        direction, steps = d.split()
        rope.moveHead(direction, int(steps))

    print(f"Part 2: With {knots} knots, tail visited {len(set(rope.getTailPositionHistory()))} positions.")


class Rope:

    def __init__(self, knots: int):
        self.knotPositions = []

        # initialize knot positions
        for i in range(0, knots):
            self.knotPositions.append((0, 0))

        self.tailPositionHistory = []
        self._recordTailPositionHistory()

    def moveHead(self, direction: str, steps: int):
        for _ in range(steps):
            self._moveHeadOnePosition(direction)

    def getTailPositionHistory(self):
        return self.tailPositionHistory

    def _getHeadPosition(self):
        return self.knotPositions[0]

    def _setHeadPosition(self, newPosition: tuple[int]):
        self._setPosition(0, newPosition)

    def _setPosition(self, index: int, newPosition: tuple[int]):
        self.knotPositions[index] = newPosition

    def _moveHeadOnePosition(self, direction: str):
        oldX, oldY = self._getHeadPosition()

        match direction:
            # move on Y axis
            case 'U':
                self._setHeadPosition((oldX, oldY+1))
            case 'D':
                self._setHeadPosition((oldX, oldY-1))

            # move on X axis
            case 'L':
                self._setHeadPosition((oldX-1, oldY))
            case 'R':
                self._setHeadPosition((oldX+1, oldY))

            # Dafuq did you do??
            case _:
                raise Exception(f"Unexpected direction: {direction}")

        self._moveTailsOnePosition(self._getHeadPosition())

    def _moveTailsOnePosition(self, headPosition):

        for i in range(1,len(self.knotPositions)):
            newPosition = self._moveTailOnePosition(self.knotPositions[i-1], self.knotPositions[i])

            if newPosition is None:
                break
            else:
                self.knotPositions[i] = newPosition

        self._recordTailPositionHistory()

    def _moveTailOnePosition(self, leaderPosition, followerPosition) -> tuple:

        # check if move needed
        variance = (leaderPosition[0] - followerPosition[0], leaderPosition[1] - followerPosition[1])

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
                self._moveDiagonally(followerPosition[0], variance[0]),
                self._moveDiagonally(followerPosition[1], variance[1])
            )
        else:
            # figure out which way to move
            newPosition = (
                self._getNewTailCoordinate(followerPosition[0], variance[0]),
                self._getNewTailCoordinate(followerPosition[1], variance[1])
            )

        # do that shizzit
        return newPosition


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
        self.tailPositionHistory.append(self._getTailPosition())

    def _getTailPosition(self):
        return self.knotPositions[-1]


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

    part1(data)
    #part2(data, 10)