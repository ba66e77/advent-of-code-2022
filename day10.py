"""
Cathode Ray Tube

Consider the following small program:

```
noop
addx 3
addx -5
```
Execution of this program proceeds as follows:

    At the start of the first cycle, the noop instruction begins execution. During the first cycle, X is 1. After the
    first cycle, the noop instruction finishes execution, doing nothing.
    At the start of the second cycle, the addx 3 instruction begins execution. During the second cycle, X is still 1.
    During the third cycle, X is still 1. After the third cycle, the addx 3 instruction finishes execution, setting X to
     4.
    At the start of the fourth cycle, the addx -5 instruction begins execution. During the fourth cycle, X is still 4.
    During the fifth cycle, X is still 4. After the fifth cycle, the addx -5 instruction finishes execution, setting X
    to -1.


commands
--------
- addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
- noop takes one cycle to complete. It has no other effect.

signal strength: the cycle number multiplied by the value of the X register

Part 1: Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these
 six signal strengths?

Part 2: Render the image given by your program. What eight capital letters appear on your CRT?

the X register controls the horizontal position of a sprite. Specifically, the sprite is 3 pixels wide, and the X
register sets the horizontal position of the middle of that sprite

You count the pixels on the CRT: 40 wide and 6 high. This CRT screen draws the top row of pixels left-to-right, then the
 row below that, and so on. The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39.

the CRT draws a single pixel during each cycle


"""

class CRT:

    def __init__(self, commandList):
        self.register = {1:1}
        self.x = 1
        self.cycle = 0
        self.commandList = commandList
        self.awaited = {}

        while self.commandList:
            self.tick()

    def tick(self):
        cmd = self.commandList.pop(0)
        self.__processCommand(cmd)

    def __processCommand(self,cmd: str):
        match cmd[0:4]:
            case 'noop':
                self.__incrementCycle()
            case 'addx':
                self.__incrementCycle()
                self.__runAddX(int(cmd.split()[1]))
            case _:
                raise Exception(f'Unexpected command: {cmd}')

    def __runAddX(self, value: int):
        self.__incrementCycle()
        self.register[self.cycle] = self.x
        self.x += value

    def __incrementCycle(self):
        self.cycle += 1
        self.register[self.cycle] = self.x


def part1(data):
    system = CRT(data)
    cycleRegistry = system.register
    print(system.register)
    totalSignalStrength = 0
    for c in [20, 60, 100, 140, 180, 220]:
        signalStrength = c * cycleRegistry[c]
        print(f"Cycle {c} has x of {cycleRegistry[c]}: {signalStrength}")
        totalSignalStrength += signalStrength

    print(f"Part 1: Total signal strength = {totalSignalStrength}")


class Renderer:

    def __init__(self, spriteCenterLocations: dict[int:int]):
        self.width = 40
        self.height = 6

        self.spriteCenterLocations = spriteCenterLocations

    def render(self):
        for h in range(0, self.height):
            rowRender = ''
            for w in range(0, self.width):
                rowRender += self.getPixel(h, w)
            print(rowRender)

    def getPixel(self, row: int, column: int) -> str:

        cycleNumber = (row * self.width) + (column + 1)
        pixelNumber = column
        spriteCenter = self.spriteCenterLocations[cycleNumber]
        if pixelNumber in range(spriteCenter-1, spriteCenter+2):
            return '#'
        else:
            return '.'


def part2(data):
    system = CRT(data)
    cycleRegistry = system.register

    renderer = Renderer(cycleRegistry)
    renderer.render()



if __name__ == '__main__':
    # data = [
    #     'noop',
    #     'addx 3',
    #     'addx -5',
    # ]

    # data = [
    #     'addx 15',
    #     'addx -11',
    #     'addx 6',
    #     'addx -3',
    #     'addx 5',
    #     'addx -1',
    #     'addx -8',
    #     'addx 13',
    #     'addx 4',
    #     'noop',
    #     'addx -1',
    #     'addx 5',
    #     'addx -1',
    #     'addx 5',
    #     'addx -1',
    #     'addx 5',
    #     'addx -1',
    #     'addx 5',
    #     'addx -1',
    #     'addx -35',
    #     'addx 1',
    #     'addx 24',
    #     'addx -19',
    #     'addx 1',
    #     'addx 16',
    #     'addx -11',
    #     'noop',
    #     'noop',
    #     'addx 21',
    #     'addx -15',
    #     'noop',
    #     'noop',
    #     'addx -3',
    #     'addx 9',
    #     'addx 1',
    #     'addx -3',
    #     'addx 8',
    #     'addx 1',
    #     'addx 5',
    #     'noop',
    #     'noop',
    #     'noop',
    #     'noop',
    #     'noop',
    #     'addx -36',
    #     'noop',
    #     'addx 1',
    #     'addx 7',
    #     'noop',
    #     'noop',
    #     'noop',
    #     'addx 2',
    #     'addx 6',
    #     'noop',
    #     'noop',
    #     'noop',
    #     'noop',
    #     'noop',
    #     'addx 1',
    #     'noop',
    #     'noop',
    #     'addx 7',
    #     'addx 1',
    #     'noop',
    #     'addx -13',
    #     'addx 13',
    #     'addx 7',
    #     'noop',
    #     'addx 1',
    #     'addx -33',
    #     'noop',
    #     'noop',
    #     'noop',
    #     'addx 2',
    #     'noop',
    #     'noop',
    #     'noop',
    #     'addx 8',
    #     'noop',
    #     'addx -1',
    #     'addx 2',
    #     'addx 1',
    #     'noop',
    #     'addx 17',
    #     'addx -9',
    #     'addx 1',
    #     'addx 1',
    #     'addx -3',
    #     'addx 11',
    #     'noop',
    #     'noop',
    #     'addx 1',
    #     'noop',
    #     'addx 1',
    #     'noop',
    #     'noop',
    #     'addx -13',
    #     'addx -19',
    #     'addx 1',
    #     'addx 3',
    #     'addx 26',
    #     'addx -30',
    #     'addx 12',
    #     'addx -1',
    #     'addx 3',
    #     'addx 1',
    #     'noop',
    #     'noop',
    #     'noop',
    #     'addx -9',
    #     'addx 18',
    #     'addx 1',
    #     'addx 2',
    #     'noop',
    #     'noop',
    #     'addx 9',
    #     'noop',
    #     'noop',
    #     'noop',
    #     'addx -1',
    #     'addx 2',
    #     'addx -37',
    #     'addx 1',
    #     'addx 3',
    #     'noop',
    #     'addx 15',
    #     'addx -21',
    #     'addx 22',
    #     'addx -6',
    #     'addx 1',
    #     'noop',
    #     'addx 2',
    #     'addx 1',
    #     'noop',
    #     'addx -10',
    #     'noop',
    #     'noop',
    #     'addx 20',
    #     'addx 1',
    #     'addx 2',
    #     'addx 2',
    #     'addx -6',
    #     'addx -11',
    #     'noop',
    #     'noop',
    #     'noop',
    #]

    inFile = open('./inputData/day10', 'r')
    data = [line.strip() for line in inFile]
    inFile.close()

    # part1(data)
    part2(data)