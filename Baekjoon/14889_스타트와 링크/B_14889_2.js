const getMinAbilityDifference = function(sumStart, sumLink) {
    minAbilityDifference = Math.min(minAbilityDifference, Math.abs(sumStart - sumLink))
}

const getAbilitiesOfLink = function(linkTeam) {
    sumOfLinkAbility = 0
    for (let m = 0; m < N / 2 - 1; m++) {
        for (let n = m + 1; n < N / 2; n++) {
            const linkAbility = abilities[linkTeam[m]][linkTeam[n]] + abilities[linkTeam[n]][linkTeam[m]]
            sumOfLinkAbility += linkAbility
        }
    }
}

const getAbilitiesOfStart = function(startTeam) {
    sumOfStartAbility = 0
    for (let m = 0; m < N / 2 - 1; m++) {
        for (let n = m + 1; n < N / 2; n++) {
            const startAbility = abilities[startTeam[m]][startTeam[n]] + abilities[startTeam[n]][startTeam[m]]
            sumOfStartAbility += startAbility
        }
    }
}

const findLink = function() {
    link = []
    for (let k = 0; k < N; k++) {
        if (inStart[k] === 0) {
            link.push(k)
        }
    }
}

const combination = function(idx) {
    if (idx === N / 2) {
        // find link N/2
        findLink()
        // get abilities
        getAbilitiesOfStart(start)
        getAbilitiesOfLink(link)
        getMinAbilityDifference(sumOfStartAbility, sumOfLinkAbility)
    } else {
        for (let j = 0; j < N; j++) {
            if (start.length > 0) {
                if (start[start.length - 1] < j && inStart[j] === 0) {
                    start.push(j)
                    inStart[j] = 1
                    combination(idx + 1)
                    start.pop()
                    inStart[j] = 0
                }
            } else {
                start.push(j)
                inStart[j] = 1
                combination(idx + 1)
                start.pop()
                inStart[j] = 0
            }

        }
    }
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])
let abilities = []
for (let i = 1; i <= N; i++) {
    const ability = input[i].split(' ').map(v => Number(v))
    abilities.push(ability)
}

let inStart = new Array(N).fill(0)
let start = []
let link = []
let sumOfStartAbility = 0
let sumOfLinkAbility = 0
let minAbilityDifference = Infinity
combination(0)
console.log(minAbilityDifference)

// N/2 그룹을 찾는다
// N/2에 속하지 않는 나머지 N/2 그룹을 찾는다
// N/2를 하나 찾으면 바로 나머지 N/2 찾고 능력치 비교 들어간다