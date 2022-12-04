"""

Part 1
------
In how many assignment pairs does one range fully contain the other?

Part 2
-------
How many assignment pairs overlap at all?

"""


def splitLineToTuples(line: str) -> tuple:
    ranges = line.split(',')

    if len(ranges) != 2:
        raise Exception(f"Line {line} split to some number of ranges other than 2.")

    return _splitRangeToTuple(ranges[0]), _splitRangeToTuple(ranges[1])


def _splitRangeToTuple(range: str) -> tuple:
    r = [int(s) for s in range.split('-')]

    if len(r) != 2:
        raise Exception(f"Line {range} split to some number of ranges other than 2.")

    return tuple(r)


def fullyOverlappingTuples(t1, t2) -> bool:
    # If the elements of the tuple are equal, they overlap.
    if t1 == t2:
        return True

    if (t1[0] <= t2[0] and t1[1] >= t2[1]) \
            or (t2[0] <= t1[0] and t2[1] >= t1[1]):
        return True
    else:
        return False


def partiallyOverlappingTuples(t1, t2) -> bool:
    # If the elements of the tuple are equal, they overlap.
    if t1 == t2:
        return True

    if t1[0] in range(t2[0], t2[1] + 1) \
        or t1[1] in range(t2[0], t2[1] + 1) \
        or t2[0] in range(t1[0], t1[1] + 1) \
        or t2[1] in range(t1[0], t1[1] + 1):
        return True
    else:
        return False


def part1(data: list) -> None:

    overlapCount = 0

    for dataline in data:
        d = splitLineToTuples(dataline)
        result = fullyOverlappingTuples(d[0], d[1])
        if result:
            overlapCount += 1

    print(f"Part 1: Full overlap count = {overlapCount}")


def part2(data: list) -> None:
    overlapCount = 0

    nooverlap = 0

    for dataline in data:
        d = splitLineToTuples(dataline)
        result = partiallyOverlappingTuples(d[0], d[1])
        if result:
            overlapCount += 1
        else:
            nooverlap +=1
            print(f"no overlap: {d}")

    print(f"Part 2: Partial overlap count = {overlapCount}, no overlap = {nooverlap}")


if __name__ == '__main__':
    inFile = open('./inputData/day4', 'r')
    data = [line.strip() for line in inFile]
    inFile.close()

    # Test data
    # data = ['18-20,19-21',
    #         '9-86,9-87',
    #         '7-8,8-18',
    #         '82-98,98-99',
    #         '17-17,17-77',
    #         '13-21,20-79',
    #         '46-52,45-46',
    #         '99-99,7-97',
    #         '69-69,69-70',
    #         '9-99,8-99',
    #         '83-91,10-92',
    #         '22-22,21-21',
    #         '41-67,40-42',
    #         '2-8,7-61',
    #         '47-63,46-68']

    # part1(data)

    part2(data)