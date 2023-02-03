# 백준

## 8393

```javascript
const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString()
const N = parseInt(input)

let num = 0
for (let i = 1; i <= N; i++) {
    num += i
}
console.log(num)
```



아래처럼 풀이하면 런타임 에러가 난다.

const는 재할당이 되지 않는다.

```javascript
const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString()
const N = parseInt(input)

const num = 0
for (let i = 1; i <= N; i++) {
    num += i
}
console.log(num)
```

