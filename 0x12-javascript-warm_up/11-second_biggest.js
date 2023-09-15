#!/usr/bin/node
<<<<<<< HEAD
if (process.argv.length <= 3) {
    console.log('0');
  } else {
    const arr = process.argv.slice(2).map(Number);
    const second = arr.sort(function (a, b) { return b - a; })[1];
    console.log(second);
=======

function findSecondLargestInteger(args) {
  if (args.length < 3) {
    return 0;
  }

  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i]);

    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }

  return secondLargest;
}

const args = process.argv;

const result = findSecondLargestInteger(args);
console.log(result);
>>>>>>> 689b3e5ab27dd48be4f2cecff4a08d7a8b66270d
