const getRange = function() {
    if (arr.length > 1) {
        const range = arr[N - 1] - arr[0]
        return range
    } else {
        return 0
    }
}

const getMostCommonNum = function(lst) {
    // 문제에서 정수의 절대값은 4000 넘지 않고 갯수는 최대 50만이다
    // 카운팅 정렬을 활용(단, 음수 주의) -4000 ~ 4000 => 8001개
    let nums = new Array(8001).fill(0)
    for (let i = 0; i < lst.length; i++) {
        const num = lst[i]
        nums[num + 4000] += 1
    }

    let maxNum = -4001
    let maxVal = 0
    let maxNumArr = [-4001]
    for (let i = 0; i < nums.length; i++) {
        const val = nums[i]
        if (val !== 0) {
            if (maxVal < val) {
                maxNum = i - 4000
                maxVal = val
                maxNumArr = [maxNum]
            } else if (maxVal === val) {
                maxNum = i - 4000
                maxVal = val
                maxNumArr.push(maxNum)
            }
        }
    }

    if (maxNumArr.length > 1) {
        return maxNumArr[1]
    } else {
        return maxNumArr[0]
    }
}

const getMiddleNum = function() {
    arr.sort((a, b) => {
        return a - b
    })
    const idx = Math.floor(N / 2)
    return arr[idx]
}

const getAverage = function(lst) {
    const length = lst.length
    const sums = lst.reduce((acc, cur) => {
        return acc + cur
    })
    const avg = Math.round(sums / length)
    return avg
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(v => Number(v))

const N = input[0]
const arr = new Array(N).fill(0)
for (let i = 1; i <= N; i++) {
    arr[i - 1] = input[i]
}

const ans1 = getAverage(arr)
const ans2 = getMiddleNum()
const ans3 = getMostCommonNum(arr)
const ans4 = getRange()
console.log(ans1)
console.log(ans2)
console.log(ans3)
console.log(ans4)
