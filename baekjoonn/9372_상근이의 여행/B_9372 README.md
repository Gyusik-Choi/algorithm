# 백준

## 9372

최소신장트리의 기본 개념을 확인하는 문제다.

순환 없이 모든 정점들을 최소 비용으로 연결하면 간선의 개수는 정점 - 1이다.

<br>

### 자바스크립트

비행스케줄에 대한 입력을 안 받았을때 받았을때 보다 시간이 2배 이상 단축 되었다. 

그리고 배열 디스트럭처링을 사용했을 때 보다 사용하지 않았을 때 시간이 아주 조금 더 단축되었다.

<br>

즉, 배열 디스트럭처링을 사용하여 N, M 에 대한 입력을 받다가

```javascript
const [N, M] = input[idx].split(' ').map(v => parseInt(v))
```

<br>

사용하지 않으니

```javascript
let NM = input[idx].split(' ').map(v => parseInt(v))
const N = NM[0]
const M = NM[1]
```

시간이 조금 더 단축되었다.
