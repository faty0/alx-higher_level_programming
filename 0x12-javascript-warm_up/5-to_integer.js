#!/usr/bin/node

const argv = process.argv;
const arg1 = argv[2];

if (isNaN(arg1)) {
  console.log('Not a number');
} else {
  const c = parseFloat(arg1);
  console.log('My number:', c);
}
