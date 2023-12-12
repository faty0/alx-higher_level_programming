#!/usr/bin/node

const argv = process.argv;
let argvCount = 0;

argv.forEach((val, index) => {
  argvCount++;
});

if (argvCount === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
