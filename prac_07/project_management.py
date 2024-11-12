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
    print(f"{len(projects)} loaded from {DEFAULT_FILENAME}")

    menu_choice = input(f"{MENU}\n>>> ").upper()



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
