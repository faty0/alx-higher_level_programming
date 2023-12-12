#!/usr/bin/node

const argv = process.argv;
let x = argv[2];

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  x = parseInt(x);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
