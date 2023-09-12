#!/usr/bin/node

const dict = require('./101-data'); // Assuming the dictionary is exported from '101-data.js'

function invertDictionary(inputDict) {
  const outputDict = {};

  for (const userId in inputDict) {
    const occurrence = inputDict[userId];

    if (!outputDict[occurrence]) {
      outputDict[occurrence] = [];
    }

    outputDict[occurrence].push(userId);
  }

  return outputDict;
}

const invertedDict = invertDictionary(dict);

console.log(invertedDict);
