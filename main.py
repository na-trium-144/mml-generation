#!/usr/bin/env python3
import random
import sys

print("A t" + str(random.choice(range(120, 160, 5))))
print("A C1o3@4")
print("B C2o5@0")


def nextchord(prev):
    if prev == 1 or prev == 3 or prev == 6:
        next = [1, 3, 6, 2, 2, 4, 4, 5, 5]
    if prev == 2 or prev == 4:
        next = [2, 4, 5, 5]
    if prev == 5:
        next = [1, 1, 3, 3, 6, 6, 5]
    return random.choice(next)


def writechord(c, rp_base, flip):
    mml_out = ["", "", ""]
    for b in rp_base:
        if b ^ flip:
            mml_out[0] += "_cdecdc"[c]
            mml_out[1] += "r"
            mml_out[2] += "r"
        else:
            mml_out[0] += "r"
            mml_out[1] += "_efgfge"[c]
            mml_out[2] += "_gababa"[c]
    print(f"A l8{mml_out[0]}")
    print(f"1A l8{mml_out[1]}")
    print(f"2A l8{mml_out[2]}")


def randompick(pr):
    l = []
    for i in range(len(pr)):
        l += [i] * int(pr[i])
    return random.choice(l)


def nextnote_first(prev, chord):
    next_pr = [0] * 7
    for i in range(3):
        next_pr[(chord + i * 2) % 7] += 4 - abs(prev - (chord + i * 2)) % 7
    n = randompick(next_pr)
    if n == 0:
        n = 7
    return n


def nextnote_other(prev, chord):
    next_pr = [0] * 7
    next_pr[prev % 7] = 2
    for i in range(1, 4):
        next_pr[(prev + i) % 7] = 4 - i
        next_pr[(prev + 7 - i) % 7] = 4 - i
    n = randompick(next_pr)
    if n == 0:
        n = 7
    return n


def nextnote_beat(prev, chord):
    next_pr = [0] * 7
    next_pr[prev % 7] = 2
    for i in range(1, 4):
        next_pr[(prev + i) % 7] = 4 - i
        next_pr[(prev + 7 - i) % 7] = 4 - i
    for i in range(3):
        next_pr[(chord + i * 2) % 7] += 1
    n = randompick(next_pr)
    if n == 0:
        n = 7
    return n


start_chord = 1
for p in range(2):
    chords = []
    while True:
        chords = [start_chord]
        for i in range(4):
            chords.append(nextchord(chords[-1]))
        if chords[4] == chords[0]:
            break
    del chords[4]
    start_chord = chords[3]

    rhythmpattern_8beat = [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 1, 0, 0],
    ]

    rp_base = random.choice(rhythmpattern_8beat)
    flip = random.choice([True, False])

    for l in range(2):
        note = random.choice(range(1, 8))
        prev_note = 4
        print("B o5l8")

        for c in chords:
            writechord(c, rp_base, flip)

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
            mml_out = "B "

            for j in range(8):
                if rp_melody[j]:
                    if j == 0:
                        note = nextnote_first(note, chords[i])
                    elif rp_base[j]:
                        note = nextnote_beat(note, chords[i])
                    else:
                        note = nextnote_other(note, chords[i])
                    if note - prev_note >= 4:
                        mml_out += "<"  # オクターブ下げ
                    if note - prev_note <= -4:
                        mml_out += ">"  # オクターブ上げ
                    mml_out += "_cdefgab"[note]
                    prev_note = note
                else:
                    mml_out += "^"
            print(mml_out)

    mml_out = "c"
    for j in range(7):
        mml_out += random.choice("ccr")
    print("C C10l8J36" + mml_out * 8)
    print("D C10l4J40 [rcrc]8")
    # mml_out = ""
    # for j in range(8):
    #     mml_out += random.choice("crr")
    # print("D C10l8J40" + mml_out * 8)
    mml_out = ""
    for j in range(4):
        mml_out += "J44" + random.choice(["cc", "cr", "cr", "rr"])
        mml_out += "J42" + random.choice(["cc", "cr", "cr", "rr"])
    print("E C10l16" + mml_out * 8)

# 適当にアウトロつけてやろ
print("A l1c")
print("1A l1e")
print("2A l1g")
mml_out = "B "
note = nextnote_first(note, 1)
if note - prev_note >= 4:
    mml_out += "<"  # オクターブ下げ
if note - prev_note <= -4:
    mml_out += ">"  # オクターブ上げ
print(f"B l1{note}")
