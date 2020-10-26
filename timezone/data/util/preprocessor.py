# Create Patricia Tries from various datasets
#
# Each Trie leaf has a timezone assigned which
# may be a fixed UTC offset or a tz timezone

import csv
from patricia_trie import PatriciaTrie

# Geonames from
# http://download.geonames.org/export/dump/allCountries.zip
def geonames_allcountries(path):
    patricia = PatriciaTrie()

    with open(path) as all_countries_csv:
        reader = csv.reader(all_countries_csv, delimiter='\t')
        for row in reader:
            if row[6] != "P": continue

            place_clean = row[2].replace(' ', '')
            patricia.add(place_clean)

    return patricia

# Timezone abbreviations from
# https://www.timeanddate.com/time/zones/
def timezone_abbreviations():
    return

# Timezones from
# https://www.iana.org/time-zones
def tz_zones():
    return
