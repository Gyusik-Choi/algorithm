# 함수 실행 방법

```javascript
let a = (() => { console.log(1) })()
// 1
```

```javascript
let a = () => { console.log(1) }
// undefined
a()
// 1
```

위와 아래의 차이는 a를 곧장 실행하도록 만드는것과 따로 a를 a()로 호출해야 실행되는 것의 차이



그런데 화살표 함수는 되는데 일반 함수로는 안 된다.

```javascript
let a = (function() {})()
// undefined

a()
// 1 Uncaught TypeError: a is not a function
```

