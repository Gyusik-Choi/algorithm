function prime_number(num) {
    if (num < 2) {
        return 0
    } else if (num === 2) {
        return 1
    } else if (num % 2 === 0) {
        return 0
    } else {
        let squareRoot = Math.floor(Math.sqrt(num))
        for (let j = 3; j <= squareRoot; j += 2) {
            if (num % j === 0) {
                return 0
            }
        }
        return 1
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const M = parseInt(input[0])
const N = parseInt(input[1])

let sums = 0
let min_num = 10001
for (let i = N; i >= M; i--) {
    let check = prime_number(i)
    if (check === 1) {
        sums += i
        min_num = i
    }
}

if (min_num === 10001) {
    console.log(-1)
} else {
    console.log(sums)
    console.log(min_num)
}