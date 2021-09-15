const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])
let electricCords = []

for (let i = 1; i <= N; i++) {
    const electricCord = input[i].split(' ').map(v => Number(v))
    electricCords.push(electricCord)
}

electricCords.sort((a, b) => {
    return a[0] - b[0]
})

let lis = new Array(N).fill(1)
for (let i = 1; i < N; i++) {
    const rightTarget = electricCords[i][1]

    for (let j = 0; j < i; j++) {
        const candidate = electricCords[j]
        const rightCandidate = candidate[1]
        
        if (rightTarget > rightCandidate) {
            lis[i] = Math.max(lis[i], lis[j] + 1)
        }
    }
}

console.log(N - Math.max(...lis))
