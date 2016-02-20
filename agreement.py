import sys
import csv
import random

from nltk.metrics.agreement import AnnotationTask

def song_row_to_annotation_entries(row):
    song = row[0]
    results = row[1:]

    return [(song, coder, category) for (coder, category) in enumerate(results)]

def balify(annotation_entry):
    song, coder, category = annotation_entry
    can_bal = category in ('b', '2')

    return (coder, song, can_bal)

def lindify(annotation_entry):
    song, coder, category = annotation_entry
    can_lindy = category in ('l', '2')

    return (coder, song, can_lindy)

if __name__ == "__main__":
    with open('results.csv', 'r') as csvfile:
        results = []

        csv_rows = list(csv.reader(csvfile))
        for row in csv_rows:
            results += song_row_to_annotation_entries(row)

        bal_annotation = AnnotationTask(data=[balify(r) for r in results])
        lindy_annotation = AnnotationTask(data=[lindify(r) for r in results])

        print("Bal agreement: " + str(bal_annotation.multi_kappa()))
        print("Lindy agreement: " + str(lindy_annotation.multi_kappa()))
