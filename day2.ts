import * as fs from 'fs';

// Part One
let totalPartOne = 0;

fs.readFile('day2input.txt', 'utf8', (err, fileData) => {
  if (err) {
    console.error(err);
    return;
  }

  const lines = fileData.split('\n');

  lines.forEach((line) => {
    const item: Record<string, number> = { red: 0, green: 0, blue: 0 };
    const game_id = parseInt(line.trim().split(":")[0].split(" ")[1]);
    const subgames = line.trim().split(":")[1].trim().split("; ");
    let correct = true;

    for (const game of subgames) {
      const parts = game.split(', ');

      for (const part of parts) {
        const [amount, color] = part.split(' ');
        item[color] = parseInt(amount);

        if (item['red'] > 12 || item['green'] > 13 || item['blue'] > 14) {
          correct = false;
          break;
        }
      }

      if (!correct) {
        break;
      }
    }

    if (correct) {
      totalPartOne += game_id;
    }
  });

  console.log("Part One answer:", totalPartOne);
});

// Part Two
let totalPartTwo = 0;

fs.readFile('day2input.txt', 'utf8', (err, fileData) => {
  if (err) {
    console.error(err);
    return;
  }

  const lines = fileData.split('\n');

  lines.forEach((line) => {
    const item: Record<string, number> = { red: 0, green: 0, blue: 0 };
    const game_id = parseInt(line.trim().split(":")[0].split(" ")[1]);
    const subgames = line.trim().split(":")[1].trim().split("; ");

    for (const game of subgames) {
      const parts = game.split(', ');

      for (const part of parts) {
        const [amount, color] = part.split(' ');
        item[color] = Math.max(item[color], parseInt(amount));
      }
    }

    const value = item["red"] * item["green"] * item["blue"];
    totalPartTwo += value;
  });

  console.log("Part Two answer:", totalPartTwo);
});
