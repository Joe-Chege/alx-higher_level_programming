#!/usr/bin/node

const fs = require('fs');
const path = require('path');

if (process.argv.length !== 5) {
  console.error('Usage: concat.js <sourceFile1> <sourceFile2> <destinationFile>');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

function concatenateFiles(sourcePath1, sourcePath2, destinationPath) {
  try {
    const content1 = fs.readFileSync(sourcePath1, 'utf8');
    const content2 = fs.readFileSync(sourcePath2, 'utf8');
    const concatenatedContent = content1 + content2;
    fs.writeFileSync(destinationPath, concatenatedContent, 'utf8');
    console.log('Files concatenated successfully.');
  } catch (err) {
    console.error('Error:', err.message);
  }
}

concatenateFiles(sourceFile1, sourceFile2, destinationFile);
