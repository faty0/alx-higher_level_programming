#!/usr/bin/node

const argv = process.argv;
let a = argv[2];
let b = argv[3];

if (!isNaN(a)) {
  a = parseFloat(a);
}
if (!isNaN(b)) {
  b = parseFloat(b);
}
console.log(a + b);
