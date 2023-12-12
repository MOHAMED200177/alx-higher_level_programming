#!/usr/bin/node
const frist = Number(process.argv[2]);
if (isNaN(frist)) {
  console.log('Missing size');
} else {
  let mySqure;
  for (let i = 0; i < frist; i++) {
    mySqure = ''
    for (let j = 0; j < frist; j++) {
      mySqure += 'X';
    }
    console.log(mySqure);
  }
}
