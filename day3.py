"""
https://adventofcode.com/2022/day/3

Part 1 ====== Find the item type that appears in both compartments of each rucksack. What is the sum of the
priorities of those item types?

priority values
---------------
Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.


Part 2
=======
As you finish identifying the misplaced items, the Elves come to you with another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg

And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?


"""
import string

# Given a string of letters, split it in half and return two lists of letters.
def splitContents(contents: str) -> tuple:
    totalLength = len(contents)

    if totalLength % 2:
        raise Exception("Input is not of evenly divisible length.")

    compartmentLength = int(totalLength / 2)

    return contents[:compartmentLength], contents[compartmentLength:]


# Given two lists of letters, find the letter that appears in both, assuming there is only one shared letter.
def findDuplicatedContents(compartment1: list, compartment2: list) -> str:
    dups = set(compartment1) & set(compartment2)

    if len(dups) != 1:
        raise Exception(f"Duplicates != 1: {dups}")

    return list(dups)[0]


# Get the numeric priority value of a given letter.
def getPriorityOfLetter(letter: str) -> int:
    # string.ascii_letters has lower and upper as string, 0 indexed
    return string.ascii_letters.find(letter) + 1


# Split data into groups for part 2.
def getGroups(data: list, groupSize: int = 3) -> list:
    steps = range(0,len(data), groupSize)

    groups = []
    for step in steps:
        group = data[step:step+groupSize]
        groups.append(group)

    return groups


# find the shared letter between members of a group.
def calculateBadge(group: list) -> str:
    # @todo: make this work for varying group sizes. This only works with groups of 3, currenlty.
    sets = [set(member) for member in group]

    dups = sets[0] & sets[1] & sets[2]

    if len(dups) != 1:
        raise Exception(f"Duplicates != 1: {dups}")

    return list(dups)[0]


if __name__ == '__main__':
    inFile = open('./inputData/day3', 'r')
    data = [line.strip() for line in inFile]
    inFile.close()

    # #test data
    #
    # data = ['vJrwpWtwJgWrhcsFMMfFFhFp',
    #     'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    #     'PmmdzqPrVvPwwTWBwg',
    #     'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    #     'ttgJtRGJQctTZtZT',
    #     'CrZsJsPPZsGzwwsLwLmpwMDw']

    totalPriority = 0

    # for d in data:
    #    c1, c2 = splitContents(d)
    #    dup = findDuplicatedContents(c1, c2)
    #    priority = getPriorityOfLetter(dup)
    #
    #    totalPriority += priority
    #
    #  print(f"Part 1: Total priority: {totalPriority}")

    groups = getGroups(data)

    for g in groups:
        badge = calculateBadge(g)
        priority = getPriorityOfLetter(badge)
        # print(f"badge: {badge}, priority: {priority}")
        totalPriority += priority

    print(f"Part2: Total priority: {totalPriority}")
