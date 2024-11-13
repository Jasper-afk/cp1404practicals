"""
CP1404 Practical 7 - Project Management Program exercise.

Estimate: 2 hours
Actual: 3 hours, 40 minutes
"""

from prac_07.project import Project
from operator import attrgetter
import datetime

CURRENT_DATE = datetime.date.today()
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
            filename = get_valid_string("Enter filename (with extension): ")
            projects = load_project_data(filename)
            print(f"Loaded {len(projects)} projects from {filename}")

        elif menu_choice == "S":
            filename = get_valid_string("Enter filename (with extension): ")
            write_project_data(filename, projects)
            print(f"{len(projects)} projects successfully saved to {filename}")

        elif menu_choice == "D":
            projects.sort(key=attrgetter("priority"))
            print("Incomplete projects:")
            display_incomplete_projects(projects)
            print("Completed projects:")
            display_completed_projects(projects)

        elif menu_choice == "F":
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

            projects.sort(key=attrgetter("start_date"))
            display_filtered_projects(projects, date)

        elif menu_choice == "A":
            print("Let's add a new project")
            add_new_project(projects)

        elif menu_choice == "U":
            update_project(projects)

        else:
            print("Invalid menu choice.")
        menu_choice = input(f"{MENU}\n>>> ").upper()

    save_to_default = input(f"Would you like to save to {DEFAULT_FILENAME}? ").upper()
    if "YES" in save_to_default or save_to_default == "Y":
        write_project_data(DEFAULT_FILENAME, projects)
        print(f"{len(projects)} projects successfully saved to {DEFAULT_FILENAME}")

    print("Thank you for using custom-built project management software.")


def display_filtered_projects(data, date):
    """Display all projects, filtered by year."""
    [print(project) for project in data if project.start_date >= date]


def add_new_project(data):
    """Add a new Project object to a list."""
    name = get_valid_string("Name: ")
    start_date = get_valid_string("Start date (dd/mm/yyyy): ")
    priority = int(get_valid_number("Priority: "))
    cost_estimate = get_valid_number("Cost estimate: $")
    completion_percentage = int(get_valid_number("Percent complete: "))
    data.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(data):
    """Update a chosen project's overall completion and its priority."""
    [print(f"{i} {project}") for i, project in enumerate(data)]
    project_choice = int(input("Project choice: "))
    while project_choice > len(data):
        print("Choice out of range")
        project_choice = int(input("Project choice: "))
    print(data[project_choice])
    new_completion_percentage = int(get_valid_number("New Percentage: "))
    new_priority = int(get_valid_number("New Priority: "))
    data[project_choice].completion_percentage = new_completion_percentage
    data[project_choice].priority = new_priority


def display_completed_projects(data):
    """Display all the projects with a 100% completion percentage."""
    [print(project) for project in data if project.completion_percentage == 100]


def display_incomplete_projects(data):
    """Display all the incomplete projects."""
    [print(project) for project in data if project.completion_percentage < 100]


def get_valid_number(prompt):
    """Get a valid digit from the user."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Input must be a digit")


def get_valid_string(prompt):
    """Get a non-empty string from the user."""
    string = input(prompt)
    while not string:  # Checks if the user entered a empty string.
        print("Invalid input")
        string = input(prompt)
    return string


def write_project_data(filename, data):
    """Write project data to a file as CSV format."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage",
              file=out_file)  # Add header to data file

        for record in data:
            record.start_date = record.start_date.strftime("%d/%m/%Y")
            print(f"{record.name}\t{record.start_date}\t{record.priority}\t{record.cost_estimate}\t{
            record.completion_percentage}\t", file=out_file)


def load_project_data(filename):
    """Load project data from CSV file."""
    project_data = []
    with open(filename) as in_file:
        in_file.readline()  # Remove data file header.
        for line in in_file:
            parts = line.strip().split("\t")
            parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = int(parts[4])
            project_data.append(Project(*parts))
    return project_data


main()
