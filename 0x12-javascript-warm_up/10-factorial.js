#!/usr/bin/node

function factorial (number) {
  if (isNaN(number)) {
    return 1;
  } else if (number === 1) {
    return 1;
  } else {
    return (number * (factorial(number - 1)));
  }
}

const argv = process.argv;
const f = factorial(argv[2]);

console.log(f);
