"""
Tree house

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees
 in the same row or column; that is, only look up, down, left, or right from any given tree.

Part 1: How many trees are visible from outside the grid?

"""

def targetVisible(targetValue: int, comparisonSet: list[int]) -> bool:
    """
    Assumes comparisonSet is every tree in front of the target, not including the target.
    :param targetValue:
    :param comparisonSet:
    :return:
    """
    m = max(comparisonSet)
    if m < targetValue:
        return True
    else:
        return False

def getComparisonSet(targetPosition: tuple[int,int], direction: str, data: list[list[int]]) -> list[int]:

    targetY, targetX = targetPosition

    match direction:
        case 'top':
            comparisonSet = [x[targetX] for x in data[0:targetY]]
        case 'bottom':
            comparisonSet = [x[targetX] for x in data[targetY+1:]]
        case 'right':
            comparisonSet = data[targetY][targetX+1:]
        case 'left':
            comparisonSet = data[targetY][0:targetX]
        case _:
            raise Exception(f"Unexpected direction {direction}.")

    return comparisonSet

if __name__ == '__main__':
    inFile = open('./inputData/day8', 'r')
    data = [list(line.strip()) for line in inFile]
    inFile.close()

    visibleTreeCount = 0

    # build map shell
    mapgrid = []
    for i in range(len(data)):
        row = []
        for x in range(len(data[0])):
            row.append(' ')
        mapgrid.append(row)

    # all borders are visible
    # top and bottom rows
    for i in range(len(data[0])):
        mapgrid[0][i] = 'V'
        mapgrid[-1][i] = 'V'

    # left and right columns
    for i in range(1, len(data)-1):
        mapgrid[i][0] = 'V'
        mapgrid[i][-1] = 'V'

    directions = ['top', 'bottom', 'left', 'right']

    for y in range(1, len(data)-1):
        for x in range(1, len(data[0])-1):
            target = data[y][x]

            for d in directions:
                comparisonSet = getComparisonSet((y, x), d, data)
                if targetVisible(target, comparisonSet):
                    visibility = 'V'
                    break
                else:
                    visibility = 'H'

            mapgrid[y][x] = visibility

    cnt = 0
    for l in mapgrid:
        cnt += l.count("V")
        print(l)

    print(f"Part 1: Visible tree count is {cnt}")


