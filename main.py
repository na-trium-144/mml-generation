#!/usr/bin/env python3
import random


def nextchord(prev):
    if prev == 1 or prev == 3 or prev == 6:
        next = [1, 3, 6, 2, 2, 4, 4, 5, 5]
    if prev == 2 or prev == 4:
        next = [2, 4, 5, 5]
    if prev == 5:
        next = [1, 1, 3, 3, 6, 6, 5]
    return random.choice(next)

def writechord(c):
    print(f"A {'_cdefga'[c]}1")
    print(f"1A {'_efgabc'[c]}1")
    print(f"2A {'_gabcde'[c]}1")

chords = []
while True:
    chords = [random.choice(range(1, 7))]
    for i in range(4):
        chords.append(nextchord(chords[-1]))
    if chords[4] == chords[0]:
        break
for c in chords:
    writechord(c)

rhythmpattern_8beat = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
]

rp_base = random.choice(rhythmpattern_8beat)
for i in range(4):
    rp_melody = []
    for j in range(8):
        if j == 0:
            p = 1
        elif rp_base[j]:
            p = 7 / 8
        else:
            p = 1 / 4
        rp_melody.append(random.random() <= p)
    mml_out = "B C10l8J36"
    for j in range(8):
        if rp_melody[j]:
            mml_out += "c"
        else:
            mml_out += "r"
    print(mml_out)
