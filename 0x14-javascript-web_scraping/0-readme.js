#!/usr/bin/node
// read and print content of a file

const fs = require("fs");

if (process.argv.length !== 3) {
  console.log("Usage: node script.js <file_path>");
} else {
  const filePath = process.argv[2];

  fs.readFile(filePath, "utf8", (error, data) => {
    if (error) {
      console.error("Error reading the file:", error);
    } else {
      console.log("File content:\n", data);
    }
  });
}
