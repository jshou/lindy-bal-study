import csv

def balable(vote):
    return vote in ('b', '2')

def lindyable(vote):
    return vote in ('l', '2')

def mostly_danceable(row, function):
    results = [function(val) for val in row]
    true_count = results.count(True)
    false_count = results.count(False)

    return true_count > false_count


if __name__ == '__main__':
    with open('results.csv', 'r') as csvfile:
        bal_gold = [] # gold standards True is balable, False is not
        lindy_gold = [] # gold standard, True is lindyable, False is not

        csv_rows = list(csv.reader(csvfile))
        for row in csv_rows[4:]: # we don't have votes for first 4 songs for a couple participants yet
            bal_gold.append(mostly_danceable(row, balable))
            lindy_gold.append(mostly_danceable(row, lindyable))
