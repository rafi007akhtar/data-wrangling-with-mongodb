import os
import csv
from pprint import pprint

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_csv(datafile):
    data = []
    with open(datafile, "r") as f:
        reader = csv.DictReader(f)  # returns a reader object
        for row in reader:
            data.append(row)
    
    return data

pprint(parse_csv(DATAFILE))  # pretty print

def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_csv(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
test()
