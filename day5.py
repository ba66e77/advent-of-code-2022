"""
--- Day 5: Supply Stacks ---

Part 1: After the rearrangement procedure completes, what crate ends up on top of each stack?

Part 2: Moving multiple crates in a step should preserve the order of the crates.


Part 1 solution is commented out in the moveCrate function. Uncomment that and comment out the marked part 2 block if
 you want to run Part 1.

Caveat: Instead of writing code to read the two different parts of the input file, I hand cut them into two separate
 files. Maybe it's cheating, but ... meh.

"""
import re


def carryOutProcedure(procedure: str, stacks: list) -> list:

    # extract values from procedure string
    pattern = 'move (?P<crates>\d+) from (?P<fromStack>\d+) to (?P<toStack>\d+)'
    match = re.match(pattern, procedure)

    if match is None:
        raise Exception(f"no match found for procedure string '{procedure}")

    moves = match.groupdict()
    fromStackNumber = int(moves['fromStack']) - 1
    toStackNumber = int(moves['toStack']) - 1

    fromStack = stacks[fromStackNumber]
    toStack = stacks[toStackNumber]

    # invoke moveCrate
    resultFrom, resultTo = moveCrate(int(moves['crates']), fromStack, toStack)

    # write results back to stacks list
    stacks[fromStackNumber] = resultFrom
    stacks[toStackNumber] = resultTo

    return stacks


# pop a number of elements off one stack and add them to the end of another stack
def moveCrate(numberToMove: int, fromStack: list, toStack: list) -> tuple:

    # # part1 moving solution
    # for _ in range(0, numberToMove):
    #     toStack.append(fromStack.pop())

    # part2 moving solution
    movedCrates = fromStack[-1 * numberToMove::]
    toStack.extend(movedCrates)
    del fromStack[-1 * numberToMove::]

    return fromStack, toStack


# given a file name, read the contents and translate it to a list of lists representing the stacks
def initializeStacks(fileLocation: str) -> list:
    # @todo: add error handling
    inFile = open(fileLocation, 'r')
    data = [list(line.strip()) for line in inFile]
    inFile.close()

    # # test data
    # data = [
    #     list('ZN'),
    #     list('MCD'),
    #     list('P')
    # ]

    return data


def getProcedureList(fileLocation: str) -> list:
    inFile = open(fileLocation, 'r')
    data = [line.strip() for line in inFile]
    inFile.close()

    # # test data
    # data = ['move 1 from 2 to 1',
    #         'move 3 from 1 to 3',
    #         'move 2 from 2 to 1',
    #         'move 1 from 1 to 2']

    return data


if __name__ == '__main__':
    initialStackFile = './inputData/day5-startStacks'
    proceduresFile = './inputData/day5-procedures'

    stacks = initializeStacks(initialStackFile)
    procedures = getProcedureList(proceduresFile)

    for procedure in procedures:
        stacks = carryOutProcedure(procedure, stacks)

    topCrates = ''
    for stack in stacks:
        topCrates += stack[-1]

    print(f"The list of top crates is: {topCrates}")