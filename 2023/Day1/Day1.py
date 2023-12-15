import re

with open("input.txt", "r") as file:
    input = file.read()


def first():
    sum = 0
    for _, v in enumerate(input.split("\n")):
        digitNumbers = re.findall(r"\d+", v)
        firstDigit = digitNumbers[0][0]
        lastNumber = digitNumbers[len(digitNumbers)-1]
        lastDigit = lastNumber[len(lastNumber)-1]
        sum += int(firstDigit + lastDigit)

    print(f"First: {sum}")

#Not solved yet
def second():
    sum = 0
    wordNumbers = {"one": "1", "two": "2", "three": "3", "four": "4",
                   "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for _, v in enumerate(input.split("\n")):
        numberIndicies = {}
        value = list(v)
        for word, number in wordNumbers.items():
            index = v.find(word)
            print(index)
            while not index == -1:
                value[index] = number
                index = v.find(word)
                
        v = "".join(value)
        print(v)
         

        digitNumbers = re.findall(r"\d+", v)
        firstDigit = digitNumbers[0][0]
        lastNumber = digitNumbers[len(digitNumbers)-1]
        lastDigit = lastNumber[len(lastNumber)-1]
        sum += int(firstDigit + lastDigit)

    print(f"Second: {sum}")

first()
second()
