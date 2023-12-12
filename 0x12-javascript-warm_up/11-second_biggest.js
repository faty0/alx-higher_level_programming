#!/usr/bin/node

// this function will receive only arrays that have minimum of 2 elemnts
function secondBiggest (arr) {
  let temp;
  for (let i = 2; i < arr.length; i++) {
    for (let j = i; j < arr.length; j++) {
      const one = parseFloat(arr[j]);
      const second = parseFloat(arr[i]);
      if (one > second) {
        temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
      }
    }
  }
  return arr[3];
}

const argv = process.argv;
let count = 0;

argv.forEach(element => {
  count++;
});

if (count === 2) {
  console.log(0);
} else if (count === 3) {
  console.log(0);
} else {
  const sb = secondBiggest(argv);
  console.log(sb);
}
