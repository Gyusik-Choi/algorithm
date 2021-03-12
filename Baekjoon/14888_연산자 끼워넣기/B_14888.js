const cal = function(idx, sums, p, s, m, d) {
    if (idx === N - 1) {
        if (sums === -0) {
            sums = 0
        }
        maxSums = Math.max(sums, maxSums)
        minSums = Math.min(sums, minSums)
    } else {
        if (p > 0) {
            cal(idx + 1, sums + nums[idx + 1], p - 1, s, m, d)
        }
        if (s > 0) {
            cal(idx + 1, sums - nums[idx + 1], p, s - 1, m, d)
        }
        if (m > 0) {
            cal(idx + 1, sums * nums[idx + 1], p, s, m - 1, d)
        }
        if (d > 0) {
            if (sums < 0) {
                sums = Math.abs(sums)
                sums = Math.floor(sums / nums[idx + 1])
                sums = sums * -1
                cal(idx + 1, sums, p, s, m, d - 1)
            } else {
                cal(idx + 1, Math.floor(sums / nums[idx + 1]), p, s, m, d - 1)
            }
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
const nums = input[1].split(" ").map(v => parseInt(v))
const o = input[2].split(" ").map(v => parseInt(v))

let maxSums = -Infinity
let minSums = Infinity
cal(0, nums[0], o[0], o[1], o[2], o[3])

console.log(maxSums)
console.log(minSums)