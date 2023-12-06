# Part 1
import re

with open("day4input.txt") as file:
    lines = file.read().strip().split("\n")

total = 0

for line in lines:
    parts = re.split("\s+", line)
    winning = list(map(int, parts[2:12]))
    ours = list(map(int, parts[13:]))

    score = 0
    for num in ours:
        if num in winning:
            score += 1

    if score > 0:
        total += 2**(score - 1)

print("Part 1 answer:", total)

#Part 2
import re

with open("day4input.txt") as file:
    lines = file.read().strip().split("\n")


n = len(lines)
copies = [[] for _ in range(n)]

for i, line in enumerate(lines):
    parts = re.split("\s+", line)
    idx = parts.index("|")
    winning = list(map(int, parts[2:idx]))
    ours = list(map(int, parts[idx+1:]))

    score = 0
    for num in ours:
        if num in winning:
            score += 1

    for j in range(i+1, i+score+1):
        copies[i].append(j)


score = [1 for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in copies[i]:
        score[i] += score[j]

print("Part 2 answer:", sum(score))