function primeFactorization(num) {
    if (num === 1) {
        return -1
    }

    ans = []
    if (arr[num] === 0) {
        ans.push(num)
        return ans
    } else {
        let squareRoot = Math.floor(Math.sqrt(num))
        while (num >= 2) {
            let flag = 0
            for (let k = 2; k <= squareRoot; k++) {
                if (num % k == 0) {
                    num = parseInt(num / k)
                    ans.push(k)
                    flag = 1
                    break
                }
            }
            if (flag === 0) {
                ans.push(num)
                break
            }
        }
        return ans
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin')
let N = parseInt(input)

let arr = new Array(N + 1).fill(0)
arr[0] = 1
arr[1] = 1
for (let i = 2; i * i <= N; i++) {
    for (let j = i * 2; j <= N; j += i) {
        if (arr[j] === 0) {
            arr[j] = 1
        }
    }
}

let n = N
let p = primeFactorization(n)
if (p !== -1) {
    for (let i = 0; i < p.length; i++) {
        console.log(p[i])
    }
}