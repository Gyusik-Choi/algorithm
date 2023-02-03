const fibonacci = function(n) {
    if (fibonacciObj.hasOwnProperty(n)) {
        return fibonacciObj[n]
    } else {
        fibonacciObj[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fibonacciObj[n]
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = Number(input[0])
let numbers = []
for (let i = 1; i <= T; i++) {
    N = Number(input[i])
    numbers.push(N)
}

let fibonacciObj = {0: 0, 1: 1}

fibonacci(40)
for (let i = 0; i < T; i++) {
    const number = numbers[i]
    if (number === 0) {
        console.log(1, 0)
    } else if (number === 1) {
        console.log(0, 1)
    } else if (number === 2) {
        console.log(1, 1)
    } else {
        console.log(fibonacciObj[number - 1], fibonacciObj[number])
    }
}

