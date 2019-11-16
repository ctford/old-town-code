import csv
import random

samplesPerKey = 10000
keys = {
  "C": 0,
  "B": 11
}

def major(key, rank):
  if rank > 6:
    return major(key, rank - 7) + 12
  else:
    return keys[key] + [0, 2, 4, 5, 7, 9, 11][rank]

ranks = random.choices(range(0, 56), k=samplesPerKey)
notes = [[k, major(k, r)] for k in keys.keys() for r in ranks]

with open('notes.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["Key", "Midi"])
    writer.writerows(notes)

csvFile.close()
