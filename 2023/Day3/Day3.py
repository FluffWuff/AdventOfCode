with open("input.txt", "r") as file:
    input = file.read()


def first():
    sum = 0
    filterCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    indexDuos = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                  (1, 0), (-1, 1), (0, 1), (1, 1)]
    for i, v in enumerate(input.split("\n")):
        for j, c in enumerate(v):
            if c not in filterCharacters:
                coveredNumbers = []
                for a, b in indexDuos:
                    horizontal = j+a
                    vert = i+b
                    if horizontal < 0 or horizontal >= len(v):
                        continue
                    if vert < 0 or vert >= len(input.split("\n")):
                        continue
                    newChar = input.split("\n")[vert][horizontal]
                    if newChar == ".":
                        continue
                    # print(newChar)
                    while horizontal > 0:
                        horizontal -= 1
                        leftChar = input.split("\n")[vert][horizontal]
                        if isNumber(leftChar):
                            newChar = leftChar + newChar
                        else:
                            horizontal = -1

                    horizontal = j+a+1
                    while horizontal < len(v):
                        rightChar = input.split("\n")[vert][horizontal]
                        horizontal += 1
                        if isNumber(rightChar):
                            newChar = newChar + rightChar
                        else:
                            horizontal = len(v) + 1
                    #print(f"{c} {newChar}")
                    if newChar not in coveredNumbers:
                        sum += int(newChar)
                        coveredNumbers.append(newChar)

                # print(c)

    print(f"First: {sum}")


def second():
    sum = 0
    indexDuos = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for i, v in enumerate(input.split("\n")):
        for j, c in enumerate(v):
            if c == "*":
                coveredNumbers = []
                for a, b in indexDuos:
                    horizontal = j+a
                    vert = i+b
                    if horizontal < 0 or horizontal >= len(v):
                        continue
                    if vert < 0 or vert >= len(input.split("\n")):
                        continue
                    newChar = input.split("\n")[vert][horizontal]
                    if newChar == ".":
                        continue
                    #print(newChar)
                    while horizontal > 0:
                        horizontal -= 1
                        leftChar = input.split("\n")[vert][horizontal]
                        if isNumber(leftChar):
                            newChar = leftChar + newChar
                        else:
                            horizontal = -1
                    
                    horizontal = j+a+1
                    while horizontal < len(v):
                        rightChar = input.split("\n")[vert][horizontal]
                        horizontal += 1
                        if isNumber(rightChar):
                            newChar = newChar + rightChar
                        else:
                            horizontal = len(v) +1
                    #print(f"{c} {newChar}")
                    if newChar not in coveredNumbers:
                        coveredNumbers.append(newChar)

                if len(coveredNumbers) == 2:
                    sum += int(coveredNumbers[0]) * int(coveredNumbers[1])       
                        

                #print(c)    
                

    print(f"Second: {sum}")



def isNumber(numberToCheck: str):
    try:
        int(numberToCheck)
    except ValueError:
        return False
    else:
        return True

first()
second()