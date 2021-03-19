const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let arr = []
for (let i = 1; i < input.length; i++) {
    const num = parseInt(input[i])
    arr.push(num)
}

arr.sort(function(a, b) {
    return a - b
})

for (let i = 0; i < arr.length; i++) {
    console.log(arr[i])
}