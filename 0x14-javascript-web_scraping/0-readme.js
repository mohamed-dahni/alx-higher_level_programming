#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];

fs.promises.readFile(filePath, 'utf-8')
  .then(content => console.log(content))
  .catch(error => {
    if (error.code === 'ENOENT') {
      console.error(`Error: ${error.code}: no such file or directory, open '${filePath}'`);
    } else {
      console.error(`Error occurred: ${error.message}`);
    }
  });
