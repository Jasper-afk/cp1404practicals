"""CP1404 practical 4 subject reader program."""

FILENAME = "subject_data.txt"


def main():
    display_subject_details(load_data())


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data += [parts]
    input_file.close()
    return data


def display_subject_details(data):
    for record in data:
        print("{} is taught by {:12} and has {:3} students".format(*record))


main()
