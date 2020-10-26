import preprocessor
import sys

p = preprocessor.geonames_allcountries("/home/armin/Downloads/allCountries/allCountries10000.txt")

with open("/home/armin/Desktop/test.dot", "w") as sys.stdout:
    p.to_dot()
