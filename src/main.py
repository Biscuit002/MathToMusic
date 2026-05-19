from midiutil import MIDIFile
from sympy import *
import random
import math

midi = MIDIFile(1)          # 1 track
midi.addTempo(0, 0, 120)    # track, start time, BPM

notes = [60, 62, 64, 65, 67]   # C D E F G
x = symbols('x')

k = 5
c = 2
function = x**4
derivativeValues = []
taylor = 0

def compute_taylor():
    current = function
    taylor = 0
    for i in range(k):
        derivativeValues.append((diff(current, x).subs(x, c)))
        current = diff(current, x)
    for i in range(len(derivativeValues)):
        taylor += (derivativeValues[i]/math.factorial(i))(x-c)**i

compute_taylor()

for i in range(len(derivativeValues)):
    derivativeValues[i] 
    
for i in range(len(notes)):
    notes[i] = random.randint(0,127)

for i, pitch in enumerate(notes):
    midi.addNote(0, 0, pitch, i, random.randint(1,4), 100)
    # track, channel, pitch, start_beat, duration, volume

with open("output.mid", "wb") as f:
    midi.writeFile(f)