# this

this를 학습하면서 배운 내용들을 코드 위주로 정리해보려고 한다

```javascript
const obj1 = {
    name: 'abc',
    method: function() {
        console.log(this)
    },
    outer: {
        inner: function() {
            console.log(this)
        }
    }
}

console.log(this)
obj1.method()
obj1.outer.inner()
```



```javascript
const obj1 = {
    outer: function() {
        const self = this
        const inner = function() {
            console.log(self)
        }
        inner()
    }
}

obj1.outer()
```



```javascript
const func = function() {
    console.log(this)
}

const obj1 = {
    name: 'abc'
}

func.call(obj1)
```



```javascript
const obj = {
    outer: function() {
        const inner = () => {
            console.log(this)
        }
        inner()
    }
}

obj.outer()
```



```javascript
const car = {
    fuel: 100,
    power: 200,
    run: function() {
        const self = this
        const innerRun = function() {
            console.log(self.fuel * self.power)
        }
        innerRun()
    }
}

car.run()
```



```javascript
const car = {
    fuel: 100,
    power: 200,
    run: function() {
        const self = this
        const innerRun = function() {
            console.log(self.fuel * self.power)
        }
        // innerRun.bind(this)()
        // innerRun.call(this)
        innerRun.apply(this)
    }
}

car.run()
```

<br>

참고

코어자바스크립트
