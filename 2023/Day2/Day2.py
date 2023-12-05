with open("input.txt", "r") as file:
    input = file.read()


def first():
    sum = 0
    for i, v in enumerate(input.split("\n")):
        game = v.replace(f"Game {i+1}: ", "")
        sets = game.split("; ")
        isPossible = False
        for set in sets:
            # print(set)
            isPossible = checkSet(set, 12, 13, 14, True)
            if not isPossible:
                break
        if isPossible:
            sum += i+1

    print(f"First: {sum}")


def second():
    sum = 0
    for i, v in enumerate(input.split("\n")):
        game = v.replace(f"Game {i+1}: ", "")
        sets = game.split("; ")
        maxRed, maxGreen, maxBlue = 0, 0, 0
        for set in sets:
            # print(set)
            r, g, b = checkSet(set, maxRed, maxGreen, maxBlue, False)
            if r > maxRed:
                maxRed = r
            if g > maxGreen:
                maxGreen = g
            if b > maxBlue:
                maxBlue = b

        sum += (maxRed * maxGreen * maxBlue)

    print(f"Second: {sum}")

def checkSet(set: str, maxRed: int, maxGreen: int, maxBlue: int, checkPossible: bool):
    cubes = set.split(", ")
    isPossible = True
    for cube in cubes:
        number = int(cube.split(" ")[0])
        # print(number)
        if "red" in cube:
            if number > maxRed:
                isPossible = False
                maxRed = number
        if "green" in cube:
            if number > maxGreen:
                isPossible = False
                maxGreen = number
        if "blue" in cube:
            if number > maxBlue:
                isPossible = False
                maxBlue = number

    if checkPossible:
        return isPossible
    else:
        return maxRed, maxGreen, maxBlue


first()
second()
