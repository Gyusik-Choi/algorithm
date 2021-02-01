function findNum(n) {
    for (let i = 1; i < n; i++) {
        candidate = i
        candidate = String(candidate).split('').map(v => Number(v))
        let sums = candidate.reduce((sumVal, curVal) => { return sumVal + curVal})
        sums += i
        if (sums === n) {
            console.log(i)
            return
        }
    }
    console.log(0)
    return
}

const fs = require('fs')
const N = parseInt(fs.readFileSync('/dev/stdin'))

findNum(N)