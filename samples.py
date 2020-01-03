import csv
import random
import itertools

keys = {
  "C": 0,
  "D": 2,
  "E": 4,
  "F": 5,
  "G": 7,
  "A": 9,
  "B": 11
}

def pick_key():
  return random.choice(keys.keys())

def pick_in_key(k):
  root = keys[k]
  degrees = keys.values()
  octave = random.randrange(10)
  degree = random.choice(degrees)
  return root + degree + (12 * octave)

def pick_sample():
    key = pick_key()
    return [key,
            pick_in_key(key),
            pick_in_key(key),
            pick_in_key(key),
            pick_in_key(key)]

def samples():
  while True:
    yield pick_sample()

with open('samples.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["Key", "W", "X", "Y", "Z"])
    rows = itertools.islice(samples(), 5000)
    writer.writerows(rows)

csvFile.close()
