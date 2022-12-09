const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('').map(v => parseInt(v));

let zero = 0;
let one = 0;

input[0] === 0 ? zero += 1 : one += 1;

let leftNumber = input[0];

input.shift();
input.forEach((number, idx) => {
    if (number !== leftNumber) {
        if (number === 0) {
            zero += 1;
        } else {
            one += 1;
        }

        leftNumber = number;
    }
});

zero <= one ? console.log(zero) : console.log(one);
