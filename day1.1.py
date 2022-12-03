"""
https://adventofcode.com/2022/day/1

Given a file of groups of numbers where each number is on a single line and groups are delimited by an empty line,
determine the highest group sum.

Data file read from https://adventofcode.com/2022/day/1/input

"""
inFile = open('./inputData/day1', 'r')
calorieData = [line.strip() for line in inFile]
inFile.close()

calorieGroups = []
groupSum = 0

for snack in calorieData:
    if snack == '':
        calorieGroups.append(groupSum)
        groupSum = 0
    else:
        groupSum += int(snack)

print(f"Highest calorie group is: {max(calorieGroups)}")

"""
Part 2: Find the sum of the top 3 calorie groups.
"""
calorieGroups.sort(reverse = True)
topThree = calorieGroups[:3]

print(f"Sum of top three groups is: {sum(topThree)}")