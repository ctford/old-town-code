import csv
import random

keys = {
  "C": 0,
  "D": 2,
  "E": 4,
  "F": 5,
  "G": 7,
  "A": 9,
  "B": 11
}

def in_major(m):
  if m > 11:
    return in_major(m - 12)
  else:
    return 1 if m in keys.values() else 0

def in_key(k, m):
  return in_major(m - keys[k] + 12)

midis = range(0, 128)
notes = [[m, in_key("A", m), in_key("B", m), in_key("C", m), in_key("D", m)] for m in midis]

with open('notes.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["Midi", "A", "B", "C", "D"])
    writer.writerows(notes)

csvFile.close()
