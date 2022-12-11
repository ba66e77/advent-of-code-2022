"""
To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes.
In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

Part 1: Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those
 directories?

"""
import re


class Directory:
    global sizelog

    def __init__(self, name: str):
        self.name = name
        self.childDirectories = {}
        self.files = {}

    def getSize(self) -> int:
        global sizelog

        size = 0
        for f in self.files:
            size += int(self.files[f])

        if self.childDirectories:
            for child in self.childDirectories:
                size += self.childDirectories[child].getSize()

        if size <= 100000:
            sizelog[self.name] = size

        return size

    def addChildDirectory(self, name: str):
        self.childDirectories[name] = Directory(name)

    def addFile(self, name: str, size: int):
        self.files[name] = size

class FileSystemModel:
    position = ['/']

    model = {}

    def __init__(self):
        self.model['/'] = Directory('/')


    def _addFile(self, name: str, size: int):
        position = self._getPosition()
        position.addFile(name, size)


    def _addDirectory(self, directoryName: str):
        position = self._getPosition()
        position.addChildDirectory(directoryName)


    def _getPosition(self):
        position = self.model[self.position[0]]
        for d in self.position[1:]:
            position = position.childDirectories[d]

        return position



    def processLs(self, resultList: list):
        for item in resultList:
            item = item.strip()
            if item[0:3] == 'dir':
                self._addDirectory(item.split()[1])
            else:
                size, name = item.split()
                self._addFile(name, size)


    def processCd(self, newRelativeDirectory: str) -> None:
        match newRelativeDirectory:
            case '..':
                self.position.pop()
            case '/':
                self.position = [self.position[0]]
            case _:
                self.position.append(newRelativeDirectory)



def extractCommands(inFileName: str) -> list[str]:
    inFile = open(inFileName, 'r')
    data = inFile.read()

    print(data)
    inFile.close()

    # data = """
    #         $ cd /
    #         $ ls
    #         dir a
    #         14848514 b.txt
    #         8504156 c.dat
    #         dir d
    #         $ cd a
    #         $ ls
    #         dir e
    #         29116 f
    #         2557 g
    #         62596 h.lst
    #         $ cd e
    #         $ ls
    #         584 i
    #         $ cd ..
    #         $ cd ..
    #         $ cd d
    #         $ ls
    #         4060174 j
    #         8033020 d.log
    #         5626152 d.ext
    #         7214296 k
    #         """

    pattern = r'\$([^$]*)'
    commands = re.findall(pattern, data, re.DOTALL)

    return commands


def processCommand(rawCommand: str, model: FileSystemModel):
    command = rawCommand.strip().split('\n')

    match command[0][0:2]:
        case 'ls':
            model.processLs(command[1:])
        case 'cd':
            model.processCd(command[0].split()[1])
        case _ :
            raise Exception(f"Unexpected command: {command[0][0:2]}")


def part1(inFileName):
    commands = extractCommands(inFileName)

    model = FileSystemModel()

    for command in commands:
        processCommand(command, model)

    global sizelog

    model.model['/'].getSize()

    totalsize = 0
    for d in sizelog:
        totalsize += int(sizelog[d])

    print(f"Part 1: Total size = {totalsize}")


    print(sizelog)


if __name__ == '__main__':
    inFileName = './inputData/day7'

    sizelog = {}
    part1(inFileName)
