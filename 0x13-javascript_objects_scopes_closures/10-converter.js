#!/usr/bin/node

exports.converter = function (base) {
  function convertRecursive(number) {
    if (number === 0) {
      return '';
    } else {
      const remainder = number % base;
      return convertRecursive(Math.floor(number / base)) + remainder;
    }
  }

  return function (number) {
    return convertRecursive(number);
  };
};
