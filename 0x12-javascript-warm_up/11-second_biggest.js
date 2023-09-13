#!/usr/bin/node

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
