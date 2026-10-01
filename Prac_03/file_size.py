def main():
    file_name = input("Enter file name: ")

    while file_name != "":
        try:
            number_of_lines = count_lines(file_name)
            print(f"Number of lines: {number_of_lines}")
        except FileNotFoundError:
            print("File does not exist.")

        file_name = input("Enter file name: ")

def count_lines(file_name):
    with open(file_name, "r") as in_file:
        return len(in_file.readlines())

main()