"""
Word Occurrences
Estimate: 60 minutes
Actual:   1 H 40 M
"""

import csv

def main():
    filename = "wimbledon.csv"
    wimbledon_data = read_csv(filename)
    wimbledon_champions = count_champions_number(wimbledon_data)
    print("Wimbledon Champions")
    for name, number in wimbledon_champions.items():
        print(f"{name} {number}")
    country = list_champions_country(wimbledon_data)
    print(f"These {len(country)} countries have won Wimbledon: ")
    print(",".join(country))
def read_csv(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        wimbledon_file = csv.reader(in_file)
        next(wimbledon_file)
        return [row for row in wimbledon_file]

def count_champions_number(data):
    champions = {}
    for row in data:
        name = row[2]
        if name in champions:
            champions[name]+= 1
        else:
            champions[name] = 1
    return champions

def list_champions_country(data):
    countries = []
    for row in data:
        country = row[1]
        if country not in countries:
            countries.append(country)
    countries.sort()
    return countries

main()
