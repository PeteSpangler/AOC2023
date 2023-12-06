#Part 1
with open("day5input.txt") as file:
    lines = file.read().strip().split("\n")

seeds = list(map(int, lines[0].split(" ")[1:]))

maps = []

i = 2
while i < len(lines):
    maps.append([])

    i += 1
    while i < len(lines) and not lines[i] == "":
        dstStart, srcStart, rangeLen = map(int, lines[i].split())
        maps[-1].append((dstStart, srcStart, rangeLen))
        i += 1

    i += 1


def findLocation(seed):
    curNum = seed

    for m in maps:
        for dstStart, srcStart, rangeLen in m:
            if srcStart <= curNum < srcStart + rangeLen:
                curNum = dstStart + (curNum - srcStart)
                break

    return curNum


locations = []
for seed in seeds:
    location = findLocation(seed)
    locations.append(location)

print("Part 1 answer:", min(locations))

#Part 2
import re

with open("day5input.txt") as file:
    lines = file.read().strip().split("\n")

raw_seeds = list(map(int, lines[0].split(" ")[1:]))
seeds = [
    (raw_seeds[i], raw_seeds[i+1])
    for i in range(0, len(raw_seeds), 2)
]

maps = []

i = 2
while i < len(lines):
    catA, _, catB = lines[i].split(" ")[0].split("-")
    maps.append([])

    i += 1
    while i < len(lines) and not lines[i] == "":
        dstStart, srcStart, rangeLen = map(int, lines[i].split())
        maps[-1].append((dstStart, srcStart, rangeLen))
        i += 1

    maps[-1].sort(key=lambda x: x[1])

    i += 1


for m in maps:
    for i in range(len(m)-1):
        if not m[i][1] + m[i][2] <= m[i+1][1]:
            print(m[i], m[i+1])


def remap(lo, hi, m):
    answer = []
    for dst, src, R in m:
        end = src + R - 1
        D = dst - src

        if not (end < lo or src > hi):
            answer.append((max(src, lo), min(end, hi), D))

    for i, interval in enumerate(answer):
        l, r, D = interval
        yield (l + D, r + D)

        if i < len(answer) - 1 and answer[i+1][0] > r + 1:
            yield (r + 1, answer[i+1][0] - 1)

    if len(answer) == 0:
        yield (lo, hi)
        return

    if answer[0][0] != lo:
        yield (lo, answer[0][0] - 1)
    if answer[-1][1] != hi:
        yield (answer[-1][1] + 1, hi)


locations = []

total = 1 << 60

for start, R in seeds:
    cur_intervals = [(start, start + R - 1)]
    new_intervals = []

    for m in maps:
        for lo, hi in cur_intervals:
            for new_interval in remap(lo, hi, m):
                new_intervals.append(new_interval)

        cur_intervals, new_intervals = new_intervals, []

    for lo, hi in cur_intervals:
        total = min(total, lo)


print("Part 2 answer:", total)