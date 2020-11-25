# 백준

## 4673

백준에서 node js로 풀이하면서 입력받을 때 주의사항은 하나의 정수만 받을 경우(ex> 5)(ex> 100)에

```javascript
const fs = require('fs')
const input =  fs.readFileSync('/dev/stdin')

const N = parseInt(input)
```

이렇게 parseInt를 하면서 input을 input[0]이 아니라 input으로 해야 한다.