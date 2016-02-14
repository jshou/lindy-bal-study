import csv

with open('results.csv', 'r') as csvfile:
    bal_only = 0.0
    lindy_only = 0.0
    both = 0.0
    neither = 0.0

    csv_rows = list(csv.reader(csvfile))
    for row in csv_rows[4:]: # we don't have votes for first 4 songs for a couple participants yet
        bal_only += row.count('b')
        lindy_only += row.count('l')
        both += row.count('2')
        neither += row.count('0')

    total = int(bal_only + lindy_only + both + neither)

    print("Total votes: " + str(total))
    print("Balboa: " + str(bal_only / total))
    print("lindy: " + str(lindy_only / total))
    print("both: " + str(both / total))
    print("neither: " + str(neither / total))
