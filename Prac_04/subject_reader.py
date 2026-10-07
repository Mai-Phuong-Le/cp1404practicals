"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subjects = load_subject_data(FILENAME)
    display_subjects(subjects)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts

        subject = [parts[0], parts[1], int(parts[2])]
        subject_data.append(subject)

    input_file.close()

    return subject_data

def display_subjects(subjects):
    """Display information about all subjects."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

main()