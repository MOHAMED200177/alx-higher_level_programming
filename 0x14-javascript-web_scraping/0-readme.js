#!/usr/bin/node
// read arg file
const fs = require('fs');
const filePath = process.argv[2];
fs.readFile('' + process.argv[2], 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else console.log(data);
});
