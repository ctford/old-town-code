import csv
import random

major = set([0, 2, 4, 5, 7, 9, 11])

def whiteNote(midi):
  return midi in major

def key(midi):
  if midi > 11:
    return key(midi - 12)
  if whiteNote(midi):
    return "C"
  else:
    return "B"

possibleMidis = range(0, 127)
midis = random.choices(possibleMidis, k=200)
data = [[key(note), note] for note in midis]

with open('notes.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["Key", "Midi"])
    writer.writerows(data)

csvFile.close()
