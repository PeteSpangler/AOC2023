# Part One
with open("day2input.txt") as file:
    total = 0
    for line in file.readlines():
        item = {'red': 0, 'green': 0, 'blue': 0}
        game_id = int(line.strip().split(":")[0].split()[1])
        subgames = line.strip().split(":")[1].strip().split("; ")
        correct = True
        for game in subgames:
            game = game.split(', ')
            for parts in game:
                parts = parts.split()
                item[parts[1]] = int(parts[0])
            if item['red'] > 12 or item['green'] > 13 or item['blue'] > 14:
                correct = False
                break
        if correct == True:
            total += game_id

print("Part One answer:", total)

# Part Two
with open("day2input.txt") as file:
    total = 0
    data = []
    for line in file.readlines():
        item = {'red': 0, 'green': 0, 'blue': 0}
        game_id = int(line.strip().split(":")[0].split()[1])
        subgames = line.strip().split(":")[1].strip().split("; ")
        for game in subgames:
            game = game.split(', ')
            for parts in game:
                parts = parts.split()
                item[parts[1]] = max(item[parts[1]], int(parts[0]))
        value = item["red"] * item["green"] * item["blue"]        
        total += value

print("Part Two answer:", total)