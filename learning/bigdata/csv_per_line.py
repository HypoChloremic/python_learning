


import csv

def getstuff(filename, criterion):
    with open(filename, "rb") as csvfile:
        datareader = csv.reader(csvfile)
        count = 0
        for row in datareader:
            if row[3] in ("column header", criterion):
                yield row
                count += 1
            elif count < 2:
                continue
            else:
                return


def getdata(filename, criteria):
    for criterion in criteria:
        for row in getstuff(filename, criterion):
            yield row


if __name__ == '__main__':
    for row in getdata(somefilename, sequence_of_criteria):
    # process row