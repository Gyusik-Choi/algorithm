const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
let people = []
for (let i = 1; i <= N; i++) {
    let person = input[i].split(' ')
    person = person.map(function(v) { 
        return parseInt(v)
    })
    people.push(person)
}

ans = new Array(N).fill(0)

idx = 0
while (idx < N) {
    cnt = 0
    for (let i = 0; i < N; i++) {
        if (i !== idx) {
            if (people[idx][0] < people[i][0] && people[idx][1] < people[i][1]) {
                cnt += 1
            }
        }
    }
    ans[idx] = cnt + 1
    idx += 1
}

console.log(ans.join(' '))