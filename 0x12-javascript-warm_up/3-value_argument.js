#!/usr/bin/node

let argv = process.argv;
let argvCount = 0;

argv.forEach((val, index) => {
  argvCount++;
});

if (argvCount === 2) {
  console.log('No argument');
} else if (argvCount === 3) {
	console.log('Argument found');
} else {
	argv.forEach((val, index) => {
		console.log(`${val}`);
	  });
}
