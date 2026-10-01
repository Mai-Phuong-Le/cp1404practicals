with open("numbers.txt", "r") as in_file:
    lines = in_file.readlines()
    total = 0

    for line in lines:
        total += int(line)

print(total)


