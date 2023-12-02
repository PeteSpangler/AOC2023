import * as fs from 'fs';

const data: number[][] = [];

fs.readFile('day1input.txt', 'utf8', (err, fileData) => {
  if (err) {
    console.error(err);
    return;
  }

  const lines = fileData.split('\n');

  lines.forEach((line) => {
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

    const item: number[] = [];

    for (const char of line) {
      if (char >= '0' && char <= '9') {
        item.push(parseInt(char));
      }
    }

    data.push(item);
  });

  let total = 0;

  for (const item of data) {
    total += 10 * item[0];
    total += item[item.length - 1];
  }

  console.log(total);
});
