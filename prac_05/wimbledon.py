"""
CP1404 Practical 5 wimbledon exercise.
estimated: 40 minutes
actual: 44 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read data from file and print details about Wimbledon champions and their countries."""
    records = get_records(FILENAME)
    champions_to_score, countries = process_records(records)
    display_results(champions_to_score, countries)


def display_results(champions_to_score, countries):
    """Display champions, scores, and countries."""
    print("Wimbledon Champions:")
    for champion, score in champions_to_score.items():
        print(champion, score)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


def process_records(records):
    """Create dictionary of champions and a set of countries."""
    champions_to_score = {}
    countries = set()
    for record in records:
        champions_to_score[record[2]] = champions_to_score.get(record[2], 0) + 1
        countries.add(record[1])
    return champions_to_score, countries


def get_records(filename) -> list:
    """Get records from given file as lists within a list."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            record = line.strip().split(",")
            records.append(record)
    return records


main()
