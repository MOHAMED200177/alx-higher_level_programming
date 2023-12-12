#!/usr/bin/node
const frist = Number(process.argv[2]);
if (isNaN(frist))
{
  console.log('Missing number of occurrences');
}
else
{
  for (let i = 0; i < frist; i++) {
    console.log('C is fun');
  }
}
