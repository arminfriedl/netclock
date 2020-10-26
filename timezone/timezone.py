import csv
from search.trie import Trie

def load_geonames():
    t = Trie(multi_value=True)
    with open("data/cities500.txt", "r") as f:
        reader = csv.reader(f, delimiter='\t')
        for i, row in enumerate(reader):
            try:
                t.insert(row[1].encode("utf-8"), row[17])
            except Exception:
                print(f"Error in row {i}")
                print(f"Label: '{row[1]}'")
                print(f"Type: {type(row[1])}")
                raise
    return t

def check_geonames():
    with open("data/cities500.txt", "r") as f:
        reader = csv.reader(f, delimiter='\t')
        for i, row in enumerate(reader):
            try:
                if row[1].endswith("lea"):
                    print(f"{i}: {row[1]} \t\t\t {row[17]}")
            except Exception:
                print(f"Error in row {i}")
                print(f"Label: '{row[1]}'")
                print(f"Type: {type(row[1])}")
                raise
