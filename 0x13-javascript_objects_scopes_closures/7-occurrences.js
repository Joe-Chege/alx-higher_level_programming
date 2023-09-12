#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  let count = 0;

  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }

  return count;
};
