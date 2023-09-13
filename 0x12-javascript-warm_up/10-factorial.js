#!/usr/bin/node

function computeFactorial(n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }

  return n * computeFactorial(n - 1);
}

const input = Number(process.argv[2]);
console.log(`Factorial of ${input} is: ${computeFactorial(input)}`);
