#!/usr/bin/node
const { argv } = require('node:process');
const argvCount = Object.keys(argv).length;
if (argvCount === 2) {
  console.log('No argument');
} else if (argvCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
