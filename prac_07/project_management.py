"""
CP1404 Practical 7 - Project Management Program exercise.

Estimate: 2 hours
Current: 1 hour, 20 minutes
Actual:
"""
from prac_07.project import Project
from operator import attrgetter
import datetime

CURRENT_DATE = datetime.date
DEFAULT_FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


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
            projects.sort(key=attrgetter("priority"))
            display_projects(projects)

        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            pass
        elif menu_choice == "U":
            pass
        else:
            print("Invalid menu choice.")
        menu_choice = input(f"{MENU}\n>>> ").upper()


def display_projects(data):
    """Display all current projects, both complete and incomplete."""
    print("Incomplete projects:")
    [print(project) for project in data if project.completion_percentage < 100]
    print("Completed projects:")
    [print(project) for project in data if project.completion_percentage == 100]


def get_valid_filename():
    """Get a non-empty filename string."""
    filename = input("Enter filename (with extension): ")
    while not filename:  # Checks if the user entered a non-empty string.
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
    project_data = []
    with open(filename) as in_file:
        in_file.readline()  # Remove data file header.
        for line in in_file:
            parts = line.strip().split("\t")
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = int(parts[4])
            project_data.append(Project(*parts))
    return project_data


main()
