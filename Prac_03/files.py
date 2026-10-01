name = input("Enter your name: ")
in_file = open("name.txt", "w")
in_file.write(name)
in_file.close()

