const fs = require('fs')
const input = fs.readFileSync('/dev/stdin')
const N = parseInt(input)

fib = {
    0: 0,
    1: 1,
    2: 1,
}

function fibonacci(n) {
    if (n == 0) {
        return 0
    } else if (n == 1 || n == 2) {
        return 1
    } else {
        if (fib.hasOwnProperty(n)) {
            return fib[n]
        } else {
            fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return fib[n]
        }
    }
}

console.log(fibonacci(N))