with open('input.txt') as file:
    binaryStrings = file.readlines()

oneDigitDict = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0
}

for binaryString in binaryStrings:
    for index, digit in enumerate(binaryString, 0):
        if digit == '1':
            oneDigitDict[index] += 1

gammaRate = ""
epsilonRate = ""

for key, value in oneDigitDict.items():
    if value > len(binaryStrings) / 2:
        gammaRate += "1"
        epsilonRate += "0"
    else:
        gammaRate += "0"
        epsilonRate += "1"


print("Power consumption: " + str(int(gammaRate, 2) * int(epsilonRate, 2)))
