"""
CP1404 Practical 5 wimbledon exercise.
estimated: 40 minutes
actual: 44 minutes
"""

CHAMPION_INDEX = 2
FILENAME = "wimbledon.csv"


def main():
    """Read data from file and print details about Wimbledon champions and their countries."""
    records = get_records(FILENAME)
    champion_to_score, countries = process_records(records)
    display_results(champion_to_score, countries)


def display_results(champion_to_score, countries):
    """Display champions, scores, and countries."""
    print("Wimbledon Champions:")
    for champion, score in champion_to_score.items():
        print(champion, score)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


def process_records(records):
    """Create dictionary of champions and a set of countries."""
    champion_to_score = {}
    countries = set()
    for record in records:
        champion_to_score[record[CHAMPION_INDEX]] = champion_to_score.get(record[CHAMPION_INDEX], 0) + 1
        countries.add(record[1])
    return champion_to_score, countries


def get_records(filename) -> list:
    """Get records from given file as lists within a list."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline() # remove header
        for line in in_file:
            record = line.strip().split(",")
            records.append(record)
    return records


main()
