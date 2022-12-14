const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('').map(v => parseInt(v));
const mid = input.length / 2;

let leftSums = 0;
let rightSums = 0;

for (let i = 0; i < mid; i++) {
    leftSums += input[i];
}


for (let i = mid; i < input.length; i++) {
    rightSums += input[i];
}

leftSums === rightSums ? console.log('LUCKY') : console.log('READY');
