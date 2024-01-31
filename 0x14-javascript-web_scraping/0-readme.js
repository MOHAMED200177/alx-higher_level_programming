#!/usr/bin/node
// Script to read and print the content of a file

const fs = require("fs");

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error("Usage: ./script.js <file_path>");
  process.exit(1); // Exit with a non-zero status code to indicate an error
}

const filePath = process.argv[2];

// Read the file content in utf-8
fs.readFile(filePath, "utf8", (error, data) => {
  if (error) {
    console.error(error); // Print the error object
  } else {
    console.log(data); // Print the file content
  }
});
