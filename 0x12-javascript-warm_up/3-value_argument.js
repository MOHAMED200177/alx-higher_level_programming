#!/usr/bin/node
if (process.argv.length >= 4) {
  const arg1 = process.argv[2];
  const arg2 = process.argv[3];

  console.log(`${arg1} is ${arg2}`);
} else {
  console.log("Please provide at least two arguments.");
}
