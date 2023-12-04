#Part One
with open("day3input.txt") as file:
    data = file.read()
    lines = data.strip().split("\n")

n = len(lines)
m = len(lines[0])


def is_symbol(i, j):
    if not (0 <= i < n and 0 <= j < m):
        return False

    return lines[i][j] != "." and not lines[i][j].isdigit()


total = 0

for i, line in enumerate(lines):
    start = 0

    col = 0

    while col < m:
        start = col
        num = ""
        while col < m and line[col].isdigit():
            num += line[col]
            col += 1

        if num == "":
            col += 1
            continue

        num = int(num)

        # Number ended, look around
        if is_symbol(i, start-1) or is_symbol(i, col):
            total += num
            continue

        for row in range(start-1, col+1):
            if is_symbol(i-1, row) or is_symbol(i+1, row):
                total += num
                break

print("Part One Answer:", total)

# Part Two

with open("day3input.txt") as file:
    data = file.read()
    lines = data.strip().split("\n")

n = len(lines)
m = len(lines[0])


goods = [[[] for _ in range(m)] for _ in range(n)]


def is_symbol(i, j, num):
    if not (0 <= i < n and 0 <= j < m):
        return False

    if lines[i][j] == "*":
        goods[i][j].append(num)
    return lines[i][j] != "." and not lines[i][j].isdigit()


total = 0

for i, line in enumerate(lines):
    start = 0

    col = 0

    while col < m:
        start = col
        num = ""
        while col < m and line[col].isdigit():
            num += line[col]
            col += 1

        if num == "":
            col += 1
            continue

        num = int(num)

        # Number ended, look around
        is_symbol(i, start-1, num) or is_symbol(i, col, num)

        for k in range(start-1, col+1):
            is_symbol(i-1, k, num) or is_symbol(i+1, k, num)

for i in range(n):
    for col in range(m):
        nums = goods[i][col]
        if lines[i][col] == "*" and len(nums) == 2:
            total += nums[0] * nums[1]

print("Part Two ans:", total)