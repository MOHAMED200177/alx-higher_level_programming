#!/user/bin/node
// Write a script that reads and prints the content of a file.
const { error } = require('console');
const fs = require('fs');
fs.readFile('' + process.argv[2], 'utf8', (err, data) => {
    if(err){
        console.log(error);
    }else{
        console.log(data);
    }
});
