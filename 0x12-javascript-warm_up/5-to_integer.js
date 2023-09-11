#!/usr/bin/node
const firstArgument = process.argv[2];

if (!isNaN(parseInt(firstArgument))) {
  console.log(`My number: ${parseInt(firstArgument)}`);
} else {
  console.log("Not a number");
}
