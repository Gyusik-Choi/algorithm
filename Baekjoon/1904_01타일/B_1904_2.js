const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString()
const N = parseInt(input)
const maxNumber = 1000000

const fibonacciNums = new Array(maxNumber + 1).fill(1)

const fibonacci = function(number) {
    while (number <= maxNumber) {
        fibonacciNums[number] = (fibonacciNums[number - 2] + fibonacciNums[number - 1]) % 15746
        number += 1
    }
}

fibonacci(2)
const answer = fibonacciNums[N]
console.log(answer)
