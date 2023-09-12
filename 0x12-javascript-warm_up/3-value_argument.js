#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log('No argument');
} else {
  const firstArgument = process.argv[2];
  console.log(firstArgument);
}
