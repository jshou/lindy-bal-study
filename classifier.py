import csv
from nltk.metrics.scores import accuracy

def balable(vote):
    return vote in ('b', '2')

def lindyable(vote):
    return vote in ('l', '2')

def mostly_danceable(row, function):
    results = [function(val) for val in row]
    true_count = results.count(True)
    false_count = results.count(False)

    return true_count > false_count

def gold_standards():
    with open('results.csv', 'r') as csvfile:
        bal_gold = [] # gold standards True is balable, False is not
        lindy_gold = [] # gold standard, True is lindyable, False is not

        csv_rows = list(csv.reader(csvfile))
        for row in csv_rows:
            bal_gold.append(mostly_danceable(row, balable))
            lindy_gold.append(mostly_danceable(row, lindyable))

    return bal_gold, lindy_gold

def bal_speed(gs, speeds, limit):
    acc = str(accuracy(gs, [i >= limit for i in speeds]))
    print("bal speed over " + str(limit) + ": " + acc)

def lindy_speed(gs, speeds, limit):
    acc = str(accuracy(gs, [i < limit for i in speeds]))
    print("lindy speed under " + str(limit) + ": " + acc)


if __name__ == '__main__':
    bal_gold, lindy_gold = gold_standards()

    attributes = open('song_attributes.csv', 'r')
    attribute_rows = list(csv.reader(attributes))

    speeds = [int(row[0]) for row in attribute_rows]
    triplety = [row[1] == '1' for row in attribute_rows]
    backbeat = [row[2] == '1' for row in attribute_rows]
    accent_m = [row[3] == '1' for row in attribute_rows]
    big_band = [row[4] == '0' for row in attribute_rows]
    crashy_c = [row[5] == '1' for row in attribute_rows]

    print("bal triplety: " + str(accuracy(bal_gold, [not i for i in triplety])))
    print("bal backbeat: " + str(accuracy(bal_gold, [not i for i in backbeat])))
    print("bal accent_m: " + str(accuracy(bal_gold, [not i for i in accent_m])))
    print("bal big_band: " + str(accuracy(bal_gold, big_band)))

    print("lindy triplety: " + str(accuracy(lindy_gold, triplety)))
    print("lindy backbeat: " + str(accuracy(lindy_gold, backbeat)))
    print("lindy accent_m: " + str(accuracy(lindy_gold, accent_m)))
    print("lindy big_band: " + str(accuracy(lindy_gold, big_band)))


    print("bal tempos:")
    for song_index, is_bal in enumerate(bal_gold):
        if is_bal:
            print(speeds[song_index])

    print("lindy tempos:")
    for song_index, is_lindy in enumerate(lindy_gold):
        if is_lindy:
            print(speeds[song_index])
