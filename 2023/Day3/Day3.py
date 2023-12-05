with open("input.txt", "r") as file:
    input = file.read()

def first():
    sum = 0
    filterCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    for i, v in enumerate(input.split("\n")):
        for j, c in enumerate(v):
            if not c in filterCharacters:
                
                print(c)    
                

    print(f"First: {sum}")

first()