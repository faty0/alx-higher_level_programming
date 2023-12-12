#!/usr/bin/node

const argv = process.argv;
let x = argv[2];
let line;

if (isNaN(x)) {
  console.log('Missing size');
} else {
  x = parseInt(x);
  for (let i = 0; i < x; i++) {
    line = '';
    for (let j = 0; j < x; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
