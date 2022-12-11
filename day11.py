"""
Monkey Business
===============

Each monkey has several attributes:

    Starting items lists your worry level for each item the monkey is currently holding in the order they will be
    inspected.
    Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means
     that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
    Test shows how the monkey uses your worry level to decide where to throw an item next.
        If true shows what happens with an item if the Test was true.
        If false shows what happens with an item if the Test was false.

After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't
 damage the item causes your worry level to be divided by three and rounded down to the nearest integer.

The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the items
 it is holding one at a time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each monkey
 has had one turn. The process of each monkey taking a single turn is called a round.

When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that
starts a round with no items could end up inspecting and throwing many items by the time its turn comes around. If a
monkey is holding no items at the start of its turn, its turn ends.


Part 1: Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of
monkey business after 20 rounds of stuff-slinging simian shenanigans?
"""

class Monkey:

    def __init__(self, startingItems: list[int], operation, test, throwTrue: int, throwFalse: int):
        self.itemList = startingItems
        self.operation = operation
        self.test = test
        self.throwTrue = throwTrue
        self.throwFalse = throwFalse
        self.monkeySwarm = []
        self.itemsInspected = 0

    def inspectItems(self):
        while self.itemList:
            item = self.itemList.pop(0)

            # increase the worry, decrease the worry, and pass on the item
            self.throwItem(
                self.decreaseWorry(
                    self.increaseWorry(item)
                )
            )

            self.itemsInspected += 1

    def increaseWorry(self, worryLevel: int) -> int:
        return self.operation(worryLevel)

    def decreaseWorry(self, worryLevel: int) -> int:
        return int(worryLevel / 3)

    def throwItem(self, item):
        if self.test(item):
            self.monkeySwarm[self.throwTrue].addItem(item)
        else:
            self.monkeySwarm[self.throwFalse].addItem(item)

    def addItem(self, item: int):
        self.itemList.append(item)


def playRounds(roundsToPlay: int, monkeySwarm: list[Monkey]):
    for i in range(roundsToPlay):
        for monkey in monkeySwarm:
            monkey.inspectItems()

    print(f"At the end of {roundsToPlay} rounds, monkeys have...:")
    for i, monkey in enumerate(monkeySwarm):
        print(f"Monkey {i}: {monkey.itemList}")


def initializeMonkeys(test = False) -> list[Monkey]:
    if test is False:
        # Initialize all the monkeys
        monkey0 = Monkey(
            [89, 95, 92, 64, 87, 68],
            lambda x: x * 11,
            lambda x: x % 2 == 0,
            7,
            4
        )

        monkey1 = Monkey(
            [87, 67],
            lambda x: x + 1,
            lambda x: x % 13 == 0,
            3,
            6
        )

        monkey2 = Monkey(
            [95, 79, 92, 82, 60],
            lambda x: x + 6,
            lambda x: x % 3 == 0,
            1,
            6
        )

        monkey3 = Monkey(
            [67, 97, 56],
            lambda x: x ** 2,
            lambda x: x % 17 == 0,
            7,
            0
        )

        monkey4 = Monkey(
            [80, 68, 87, 94, 61, 59, 50, 68],
            lambda x: x * 7,
            lambda x: x % 19 == 0,
            5,
            2
        )

        monkey5 = Monkey(
            [73, 51, 76, 59],
            lambda x: x + 8,
            lambda x: x % 7 == 0,
            2,
            1
        )

        monkey6 = Monkey(
            [92],
            lambda x: x + 5,
            lambda x: x % 11 == 0,
            3,
            0
        )

        monkey7 = Monkey(
            [99, 76, 78, 76, 79, 90, 89],
            lambda x: x + 7,
            lambda x: x % 5 == 0,
            4,
            5
        )

        monkeys = [
            monkey0,
            monkey1,
            monkey2,
            monkey3,
            monkey4,
            monkey5,
            monkey6,
            monkey7
        ]

    else:
        # Initialize all the monkeys
        monkey0 = Monkey(
            [79, 98],
            lambda x: x * 19,
            lambda x: x % 23 == 0,
            2,
            3
        )

        monkey1 = Monkey(
            [54, 65, 75, 74],
            lambda x: x + 6,
            lambda x: x % 19 == 0,
            2,
            0
        )

        monkey2 = Monkey(
            [79, 60, 97],
            lambda x: x**2,
            lambda x: x % 13 == 0,
            1,
            3
        )

        monkey3 = Monkey(
            [74],
            lambda x: x + 3,
            lambda x: x % 17 == 0,
            0,
            1
        )

        monkeys = [monkey0, monkey1, monkey2, monkey3]

    # All the monkeys know about the other monkeys in their game.
    for monkey in monkeys:
        monkey.monkeySwarm = monkeys

    return monkeys


def part1():
    monkeys = initializeMonkeys()
    playRounds(20, monkeys)

    inspections = [monkey.itemsInspected for monkey in monkeys]
    print(inspections)

    inspections.sort(reverse=True)
    print(f"Total monkey business = {inspections[0] * inspections[1]}")


if __name__ == '__main__':

    part1()
