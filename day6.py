"""

Find start-of-packet marker, which is any four unique characters in sequence

Test data

    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

Part 1: How many characters need to be processed before the first start-of-packet marker is detected?

Part 2: Now with 14 characters, where does the first message marker end?
"""


def findFirstMarker(datastream: str, markerLength=4):
    for i in range(markerLength, len(datastream)):
        rng = datastream[i - markerLength:i]
        uniq = set(rng)
        if len(rng) == len(uniq):
            return i, rng


if __name__ == '__main__':
    # @todo: add error handling
    inFile = open('./inputData/day6', 'r')
    data = inFile.read()
    inFile.close()

    i, seq = findFirstMarker(data)
    print(f'Part 1: The first marker is {seq}, ending at character {i}.')

    i, seq = findFirstMarker(data, 14)
    print(f'Part 2: The first marker is {seq}, ending at character {i}.')

