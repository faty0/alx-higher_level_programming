#!/usr/bin/node
const { argv } = require('node:process');
let argvCount = 0;

argv.forEach((val, index) => {
    argvCount++;
  });

if (argvCount === 0) {
  console.log('No argument');
} else if (argvCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}