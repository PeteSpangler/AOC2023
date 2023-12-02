"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
// Part One
var totalPartOne = 0;
fs.readFile('day2input.txt', 'utf8', function (err, fileData) {
    if (err) {
        console.error(err);
        return;
    }
    var lines = fileData.split('\n');
    lines.forEach(function (line) {
        var item = { red: 0, green: 0, blue: 0 };
        var game_id = parseInt(line.trim().split(":")[0].split(" ")[1]);
        var subgames = line.trim().split(":")[1].trim().split("; ");
        var correct = true;
        for (var _i = 0, subgames_1 = subgames; _i < subgames_1.length; _i++) {
            var game = subgames_1[_i];
            var parts = game.split(', ');
            for (var _a = 0, parts_1 = parts; _a < parts_1.length; _a++) {
                var part = parts_1[_a];
                var _b = part.split(' '), amount = _b[0], color = _b[1];
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
var totalPartTwo = 0;
fs.readFile('day2input.txt', 'utf8', function (err, fileData) {
    if (err) {
        console.error(err);
        return;
    }
    var lines = fileData.split('\n');
    lines.forEach(function (line) {
        var item = { red: 0, green: 0, blue: 0 };
        var game_id = parseInt(line.trim().split(":")[0].split(" ")[1]);
        var subgames = line.trim().split(":")[1].trim().split("; ");
        for (var _i = 0, subgames_2 = subgames; _i < subgames_2.length; _i++) {
            var game = subgames_2[_i];
            var parts = game.split(', ');
            for (var _a = 0, parts_2 = parts; _a < parts_2.length; _a++) {
                var part = parts_2[_a];
                var _b = part.split(' '), amount = _b[0], color = _b[1];
                item[color] = Math.max(item[color], parseInt(amount));
            }
        }
        var value = item["red"] * item["green"] * item["blue"];
        totalPartTwo += value;
    });
    console.log("Part Two answer:", totalPartTwo);
});
