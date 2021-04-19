const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
const N = parseInt(input[0])

let nums = []
for (let i = 1; i <= N; i++) {
    const temp = input[i].split(" ").map(v => Number(v))
    nums.push(temp)
}

nums.sort((a, b) => {
    if (a[0] !== b[0]) {
        return a[0] - b[0]
    } else {
        return a[1] - b[1]
    }
})

let sortedNums = ''
for (let i = 0; i < N; i++) {
    sortedNums += `${nums[i][0]} ${nums[i][1]}\n`
}
console.log(sortedNums)