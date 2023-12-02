"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var data = [];
fs.readFile('day1input.txt', 'utf8', function (err, fileData) {
    if (err) {
        console.error(err);
        return;
    }
    var lines = fileData.split('\n');
    lines.forEach(function (line) {
        line = line
            .replace('one', 'o1ne')
            .replace('two', 't2wo')
            .replace('three', 'th3ree')
            .replace('four', 'f4our')
            .replace('five', 'f5ive')
            .replace('six', 's6ix')
            .replace('seven', 's7even')
            .replace('eight', 'e8ight')
            .replace('nine', 'n9ine');
        var item = [];
        for (var _i = 0, line_1 = line; _i < line_1.length; _i++) {
            var char = line_1[_i];
            if (char >= '0' && char <= '9') {
                item.push(parseInt(char));
            }
        }
        data.push(item);
    });
    var total = 0;
    for (var _i = 0, data_1 = data; _i < data_1.length; _i++) {
        var item = data_1[_i];
        total += 10 * item[0];
        total += item[item.length - 1];
    }
    console.log(total);
});
