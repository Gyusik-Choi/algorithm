# 백준

## 10818

```javascript
const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

const N = parseInt(input[0])
let nums = input[1].split(' ')
let new_nums = nums.map(v => { return parseInt(v) })

let min_num = new_nums[0]
let max_num = new_nums[0]
for (let i = 0; i < N; i++) {
    if (min_num > new_nums[i]) {
        min_num = new_nums[i]
    }
    if (max_num < new_nums[i]) {
        max_num = new_nums[i]
    }
}
console.log(min_num + ' ' + max_num)
```



자바스크립트 문법을 익힐겸 백준에서 node js로 문제도 풀고 있으나 파이썬이나 자바보다 상대적으로 까다로운 듯 하다. 입력과 관련한 세팅이 특히 그렇다. fs 모듈을 쓰면 에러가 나서 readline으로만 풀어지는 문제도 있었다.

아무튼 이번 문제에서는 map 메소드를 활용했다.

파이썬의 map과 거의 같은 기능을 담당한다. 둘 다 배열(파이썬은 리스트)을 반복문을 돌면서 요소를 1 : 1 매핑을 시켜준다. 차이는 파이썬의 map은 리스트와 튜플에서 가능한데 자바스크립트는 튜플 자료구조가 없기 때문에 배열에서 사용 가능하다.

```javascript
let arr = ['1', '2', '3']
arr = arr.map(function(v) {
    return Number(v)
})
console.log(arr)
// [1, 2, 3]
```

```javascript
let arr = ['1', '2', '3']
arr = arr.map(v => {
    return Number(v)
})
console.log(arr)
// [1, 2, 3]
```

