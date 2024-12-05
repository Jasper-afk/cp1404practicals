"""
CP1404 Practical 10
Wiki exercise
"""

import wikipedia


def main():
    """Wikipedia program - Get a page from wikipedia via user input."""
    wiki_title = input("Enter page title: ")
    while wiki_title:  # Check if wiki_title is empty.
        try:
            page = wikipedia.page(wiki_title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as error:
            print(f"We need a more specific title. Try one of the following, or a new search:\n{error.options}")
        except wikipedia.exceptions.PageError:
            print(f'Page id "{wiki_title}" does not match any pages. Try another id!')
        wiki_title = input("Enter page title: ")
    print("Thank you.")


main()
