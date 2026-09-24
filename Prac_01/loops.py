for i in range(1, 21, 2):
    print(i, end=' ')
# a
for i in range(0,100,10):
    print(i, end=' ')
# b
for i in range(20,1,-1):
    print(i, end=' ')
#c
number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    print(i, end=' ')
# d
number_of_lines = int(input("Number of lines: "))

for line in range(1, number_of_lines + 1):
    print("*" * line)