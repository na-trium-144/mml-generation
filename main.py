#!/usr/bin/env python3
import random
import sys

# print("A t150")

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

def nextnote(prev, chord):
    next_pr = [0] * 7
    next_pr[prev % 7] = 2
    for i in range(1, 4):
        next_pr[(prev + i) % 7] = 4 - i
        next_pr[(prev + 7 - i) % 7] = 4 - i
    for i in range(3):
        next_pr[(chord + i * 2) % 7] += 1
    next = []
    for i in range(7):
        next += [i] * int(next_pr[i])
    # sys.stderr.write(f"{prev}, {next_pr}\n")
    n = random.choice(next)
    if n == 0:
        n = 7
    return n

rhythmpattern_8beat = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
]

note = random.choice(range(1, 8))
prev_note = 4

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
    mml_out = "B C2l8"

    for j in range(8):
        if rp_melody[j]:
            note = nextnote(note, chords[i])
            if note - prev_note >= 4:
                mml_out += "<" #オクターブ下げ
            if note - prev_note <= -4:
                mml_out += ">" #オクターブ上げ
            mml_out += "_cdefgab"[note]
            prev_note = note
        else:
            mml_out += "^"
    print(mml_out)
