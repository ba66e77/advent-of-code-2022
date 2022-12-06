"""

Find start-of-packet marker, which is any four unique characters in sequence

Test data

    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

Part 1: How many characters need to be processed before the first start-of-packet marker is detected?
"""

if __name__ == '__main__':
    # @todo: add error handling
    inFile = open('./inputData/day6', 'r')
    data = [list(line.strip()) for line in inFile]
    inFile.close()