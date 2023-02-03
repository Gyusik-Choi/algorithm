const permutation = function(idx, m) {
    if (idx === m) {
        console.log(perm.join(" "))
    } else {
        for (let j = 0; j < N; j++) {
            if (check[j] === 0) {
                perm.push(arr[j])
                check[j] = 1
                permutation(idx + 1, m)
                perm.splice(perm.length - 1, 1)
                check[j] = 0
            }
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim()

const nAndM = input.split(' ')
const N = parseInt(nAndM[0])
const M = parseInt(nAndM[1])

const arr = new Array(N)
for (let i = 1; i <= N; i++) {
    arr[i - 1] = i
}

let check = new Array(N).fill(0)
let perm = []

permutation(0, M)