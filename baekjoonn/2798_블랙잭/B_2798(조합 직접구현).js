function combination(idx) {
    if (max_num === M) {
        return
    } else if (idx === 3) {
        let sums = comb.reduce(function(sumNum, curVal) {
            return sumNum + curVal
        }, 0)
        if (sums == M) {
            max_num = sums
            return
        } else if (max_num < sums && sums < M) {
            max_num = sums
        }
    } else {
        for (let i = 0; i < N; i++) {
            if (check[i] === 0) {
                if (comb.length === 0) {
                    check[i] = 1
                    comb.push(nums[i])
                    combination(idx + 1)
                    check[i] = 0
                    comb.pop()
                } else {
                    if (comb[comb.length - 1] <= nums[i]) {
                        check[i] = 1
                        comb.push(nums[i])
                        combination(idx + 1)
                        check[i] = 0
                        comb.pop()
                    }
                }
            }
        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

let nm = input[0].split(' ')
nm = nm.map(v => Number(v))
let N = nm[0]
let M = nm[1]

let nums = input[1].split(' ')
nums = nums.map(v => Number(v))
nums = nums.sort(function(a, b) {
    return a - b
})

let check = new Array(N).fill(0)
let max_num = 1
let comb = []

combination(0)
console.log(max_num)