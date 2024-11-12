"""
CP1404 Practical 7 - Project Management Program exercise.

Estimate: 2 hours
Actual:
"""
from prac_07.project import Project
import datetime

DEFAULT_FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""

def main():
    """Update information about projects."""
    print("Welcome to Pythonic Project Management")

    projects = load_project_data(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    menu_choice = input(f"{MENU}\n>>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = get_valid_filename()
            projects = load_project_data(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif menu_choice == "S":
            filename = get_valid_filename()
            write_project_data(filename, projects)
            print(f"{len(projects)} projects successfully saved to {filename}")
        elif menu_choice == "D":
            pass
        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            pass
        elif menu_choice == "U":
            pass
        else:
            print("Invalid menu choice.")
        menu_choice = input(f"{MENU}\n>>> ").upper()

def get_valid_filename():
    filename = input("Enter filename (with extension): ")
    while not filename: # Checks if the user entered a non-empty string.
        print("Invalid filename")
        filename = input("Enter filename (with extension): ")
    return filename

def write_project_data(filename, data):
    """Write project data to a file as CSV format."""
    with open(filename, "w") as out_file:
        for record in data:
            print(f"{record.name}\t{record.start_date}\t{record.priority}\t{record.cost_estimate}\t{
            record.completion_percentage}\t", file=out_file)

def load_project_data(filename):
    """Load project data from CSV file."""
    data = []
    with open(filename) as in_file:
        in_file.readline() # Remove data file header.
        for line in in_file:
            parts = line.strip().split("\t")
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = int(parts[4])
            data.append(Project(*parts))
    return data

main()
