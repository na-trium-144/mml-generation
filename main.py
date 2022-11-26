#!/usr/bin/env python3
import random


def nextcode(prev):
    if prev == 1 or prev == 3 or prev == 6:
        next = [1, 3, 6, 2, 2, 4, 4, 5, 5]
    if prev == 2 or prev == 4:
        next = [2, 4, 5, 5]
    if prev == 5:
        next = [1, 1, 3, 3, 6, 6, 5]
    return next[int(len(next) * random.random())]


def writecode(c):
    print(f"A {'_cdefga'[c]}1")
    print(f"1A {'_efgabc'[c]}1")
    print(f"2A {'_gabcde'[c]}1")


code = []
while True:
    code = [int(1 + 6 * random.random())]
    for i in range(4):
        code.append(nextcode(code[-1]))
    if code[4] == code[0]:
        break
for c in code:
    writecode(c)
