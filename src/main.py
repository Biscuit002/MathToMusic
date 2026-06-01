from midiutil import MIDIFile
from sympy import *
import random
import math

midi = MIDIFile(1)          # 1 track
midi.addTempo(0, 0, 120)    # track, start time, BPM
x = symbols('x')

#Adjustable values
mappedScale = [0,2,4,7,9] #c major pentatonic
melodyLength = 20 #length of melody
k = 10 #taylor polynomial order
c = 1 #center of taylor
inputFunction = cos(x) #Function to use

notes = [0] * melodyLength
derivativeValues = []
taylorPolynomial = 0

def compute_taylor():
    current = inputFunction
    taylorPolynomial = 0
    derivativeValues = [current]
    for i in range(k):
        derivativeValues.append((diff(current, x).subs(x, c)))
        current = diff(current, x)
    for n in range(len(derivativeValues)):
        taylorPolynomial += (derivativeValues[n]/math.factorial(n))*(x-c)**n
    return taylorPolynomial

taylor = compute_taylor()

for i in range(melodyLength):
    notes[i] = taylor.subs(x,i)


for i, pitch in enumerate(notes):
    
    octave = pitch // len(mappedScale)
    noteIndex = pitch % len(mappedScale)
    
    pitch = 60 + (octave * 12) + mappedScale[int(noteIndex)]
    while pitch > 100:
        pitch -= 12
    while pitch < 40:
        pitch += 12
    
    midi.addNote(0, 0, pitch, i, random.randint(1,4), 100)
    # track, channel, pitch, start_beat, duration, volume

    print(pitch)
with open("output.mid", "wb") as f:
    midi.writeFile(f)