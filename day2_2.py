"""
Rock Paper Scissors

Given data file as strategy guide where column 1 is opponent's play and column 2 is what I should play, and scoring
rules below.

column1:
A for Rock, B for Paper, and C for Scissors

column2:
X for Rock, Y for Paper, and Z for Scissors

Your total score is the sum of your scores for each round. The score for a single round is the score for the shape
you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you
lost, 3 if the round was a draw, and 6 if you won).

Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape,
the round instead ends in a draw.


--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round
needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round
ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also
    choose Rock. This gives you a score of 1 + 3 = 4. In the second round, your opponent will choose Paper (B),
    and you choose Rock so you lose (X) with a score of 1 + 0 = 1. In the third round, you will defeat your
    opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly
according to your strategy guide?

"""


def decodeLine(line: str):
    key = [
            {
                'A': "Rock",
                'B': "Paper",
                'C': "Scissors"
            },
            {
                'X': "lose",
                'Y': "draw",
                'Z': "win"
            }
    ]

    line = line.split(' ')
    return key[0][line[0]], key[1][line[1]]


def determinePlay(opponentPlay, outcome):

    out = None

    match outcome:
        case 'draw':
            out = opponentPlay
        case 'win':
            out = _getWinningPlay(opponentPlay)
        case 'lose':
            out = _getLosingPlay(opponentPlay)
        case _:
            raise Exception(f'unexpected value {outcome}')

    return out


def _getLosingPlay(opponentPlay):
    match opponentPlay:
        case 'Rock':
            play = 'Scissors'
        case 'Paper':
            play = 'Rock'
        case 'Scissors':
            play = 'Paper'
        case _:
            raise Exception(f'unexpected value {opponentPlay}')

    return play


def _getWinningPlay(opponentPlay):
    match opponentPlay:
        case 'Rock':
            play = 'Paper'
        case 'Paper':
            play = 'Scissors'
        case 'Scissors':
            play = 'Rock'
        case _:
            raise Exception(f'unexpected value {opponentPlay}')

    return play


def determineOutcomePoints(opponentPlay, myPlay):
    if opponentPlay == 'Rock':
        if myPlay == 'Rock':
            # draw
            points = 3 + 1
        elif myPlay == 'Paper':
            # I win
            points = 6 + 2
        else:
            # I lose with Scissors
            points = 0 + 3
    elif opponentPlay == 'Paper':
        if myPlay == 'Rock':
            # I lose
            points = 0 + 1
        elif myPlay == 'Paper':
            # I draw
            points = 3 + 2
        else:
            # I win with Scissors
            points = 6 + 3
    elif opponentPlay == 'Scissors':
        if myPlay == 'Rock':
            # I win
            points = 6 + 1
        elif myPlay == 'Paper':
            # I lose
            points = 0 + 2
        else:
            # draw with Scissors
            points = 3 + 3
    else:
        raise Exception('dafuq did you do??')

    return points


if __name__ == '__main__':
    inFile = open('./inputData/day2', 'r')
    playData = [line.strip() for line in inFile]
    inFile.close()

    totalScore = 0

    for playRound in playData:
        opponentPlay, outcome = decodeLine(playRound)
        myPlay = determinePlay(opponentPlay, outcome)
        totalScore += determineOutcomePoints(opponentPlay, myPlay)

    print(f"Part 2: Total points in tournament = {totalScore}")
