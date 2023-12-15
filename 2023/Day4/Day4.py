with open("input.txt", "r") as file:
    input = file.read()


def first():
    sum = 0
    for i, line in enumerate(input.split("\n")):
        matches = 0
        print(line)
        line = line.split(": ")[1]
        winningNumbers = line.split(" | ")[0].split(" ")
        myNumbers = line.split(" | ")[1].split(" ")
        for mN in myNumbers:
            if mN == "":
                continue
            if mN in winningNumbers:
                print(mN)
                matches += 1

        print(matches)
        if matches == 0:
            continue
        sum += 2**(matches-1)

    print(f"First: {sum}")


def second():
    sum = 0
    copies = dict.fromkeys(input.split("\n"), 1)
    for i, line in enumerate(input.split("\n")):
        #print(copies[line])
        instances = copies[line]
        sum += instances
        matches = 0
        # print(line)
        winningNumbers = line.split(": ")[1].split(" | ")[0].split(" ")
        myNumbers = line.split(": ")[1].split(" | ")[1].split(" ")
        for mN in myNumbers:
            if mN == "":
                continue
            if mN in winningNumbers:
                # print(mN)
                matches += 1

        print(matches)
        #print(copies)
        if matches == 0:
            continue
        while matches > 0:
            print(str(i) + " "+ input.split("\n")[i+matches])
            copies[input.split("\n")[i+matches]] += instances
            matches -= 1

    print(copies)

    print(f"Second: {sum}")


first()
second()
