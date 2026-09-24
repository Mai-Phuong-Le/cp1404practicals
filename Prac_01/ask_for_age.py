# repeatedly ask for an age (unknow/ indefinite number of people)
# stopping when the user enter -1 then print the total and average of the ages
total = 0
count = 0

age = int(input("Enter age: "))

while age != -1:
    total += age
    count += 1
    age = int(input("Enter age: "))

if count > 0:
    average = total / count
    print(f"Total age: {total}")
    print(f"Average age: {average:.2f}")
else:
    print("No ages were entered.")