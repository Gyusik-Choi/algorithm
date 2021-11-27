const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

let visited = new Array(21).fill(0).map(v => new Array(21).fill(0).map(v => new Array(21).fill(0)))

for (let i = 0; i < input.length; i++) {
    const w = function(a, b, c) {
        if (a <= 0 || b <= 0 || c <= 0) {
            return 1
        }

        if (a > 20 || b > 20 || c > 20) {
            return w(20, 20, 20)
        }

        if (visited[a][b][c] !== 0) {
            return visited[a][b][c]
        }
        
        if (a < b && b < c) {
            visited[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return visited[a][b][c]
        }

        visited[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return visited[a][b][c]
    }

    const isLast = function(nums) {
        for (let j = 0; j < nums.length; j++) {
            if (nums[j] !== -1) {
                return false
            }
        }

        return true
    }

    const numbers = input[i].split(' ').map(v => parseInt(v))
    if (isLast(numbers) === false) {
        const [first, second, third] = numbers
        const answer = w(first, second, third)
        
        console.log(`w(${first}, ${second}, ${third}) = ${answer}`)
    }    
}

// a, b, c 각각의 값 보다도 w(a, b, c) 가 어떤 하나의 값으로 나오는지
// 각 w(a, b, c)를 저장해두고 (메모이제이션)
// 같은 값이 있으면 바로 리턴해주면 시간을 단축할 수 있다
// key, value 형태로 저장할때 어떻게 저장할지가 고민된다
// 파이썬이라면 딕셔너리를 이용해 key를 튜플로 할 수 있지만
// 자바스크립트에서는 할 수 없으므로
// 3차원 배열로 하면 최대 약 8000(21 * 21 * 21) 만큼의 공간이 필요하다
// 그리고 해당 값이 있는지 조회하는 것을 어떻게 구성해야 할지 고민된다
// 기존에 주어진 재귀 함수의 조건과 어떻게 함께 구성하는게 좋을지 쉽게 떠오르지 않는다
