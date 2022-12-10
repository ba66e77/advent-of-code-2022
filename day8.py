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

if __name__ == '__main__':
    inFile = open('./inputData/day8', 'r')
    data = [list(line.strip()) for line in inFile]
    inFile.close()

    data = data[0:5]

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

    for y in range(1, len(data)-1):
        for x in range(1, len(data[0])-1):
            target = data[y][x]
            #top
            comparisonSet = data[1:y+1]




    for l in mapgrid:
        print(l)
