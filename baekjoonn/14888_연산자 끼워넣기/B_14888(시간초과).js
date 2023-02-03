const permutations = function(idx, length) {
    if (idx === length) {
        ops.push(temp.slice())
    } else {
        for (let i = 0; i < length; i++) {
            if (!check[i]) {
                check[i] = !check[i]
                temp.push(operations[i])
                permutations(idx + 1, length)
                check[i] = !check[i]
                temp.pop()
            }
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
const nums = input[1].split(" ").map(v => parseInt(v))
const o = input[2].split(" ").map(v => parseInt(v))

let operations = []
for (let i = 0; i < 4; i++) {
    for (let j = 0; j < o[i]; j++) {
        if (i === 0) {
            operations.push("+")
        } else if (i === 1) {
            operations.push("-")
        } else if (i === 2) {
            operations.push("*")
        } else {
            operations.push("/")
        }
    }
}
const operationsLength = operations.length

let ops = []
let temp = []
let check = new Array(operationsLength).fill(0)
permutations(0, operationsLength)

let maxSums = -Infinity
let minSums = Infinity
for (let i = 0; i < ops.length; i++) {
    let sums = nums[0]
    let arr = ops[i]
    for (let j = 0; j < arr.length; j++) {
        if (arr[j] === '+') {
            sums = sums + nums[j + 1]
        } else if (arr[j] === '-') {
            sums = sums - nums[j + 1]
        } else if (arr[j] === '*') {
            sums = sums * nums[j + 1]
        } else {
            if (sums < 0) {
                sums = sums * -1
                sums = Math.floor(sums / nums[j + 1])
                sums = sums * -1
            } else {
                sums = Math.floor(sums / nums[j + 1])
            }
        }
    }
    if (sums > maxSums) {
        maxSums = sums
    } else if (sums < minSums) {
        minSums = sums
    }
}

console.log(maxSums)
console.log(minSums)