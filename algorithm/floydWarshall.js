const floydWarshall = function() {
    // 자신에서 자신으로는 값이 업데이트 되지 않도록 0 설정
    // 아래의 if (routes[i][j] > routes[i][k] + routes[k][j]) {} 조건문을
    // 만족하지 않도록 해준다
    // 0보다 작은 합이 나올 수 없음
    for (let k = 0; k < routes.length; k++) {
        routes[k][k] = 0;
    }

    for (let k = 0; k < routes.length; k++) {
        for (let i = 0; i < routes.length; i++) {
            for (let j = 0; j < routes.length; j++) {
                if (routes[i][j] > routes[i][k] + routes[k][j]) {
                    routes[i][j] = routes[i][k] + routes[k][j]
                }
            }
        }
    }
}

const input = [[5], [14], [1, 2, 2], [1, 3, 3], [1, 4, 1], [1, 5, 10], [2, 4, 2], [3, 4, 1], [3, 5, 1], [4, 5, 3], [3, 1, 8], [1, 4, 2], [5, 1, 7], [5, 2, 4]];

const n = input[0][0];
const m = input[0][1];
// Infinity로 초기화
// 이후 직접갈 수 있는 경로는 값이 업데이트 되고,
// 직접갈 수 없는 경로는 Infinity 로 남아있다
// 이렇게 되면 직접가지 못하지만 거쳐서 갈 수 있으면
// if (routes[i][j] > routes[i][k] + routes[k][j]) { } 를 충족해서
// 값이 업데이트 될 수 있다
// 직접 못가는 경로는 Infinity 인데 
// 직접갈 수 있는 경로는 Infinity 가 아니라서 값을 합쳐도 Infinity 보다 작을 수 밖에 없다
routes = new Array(n).fill(Infinity).map(_ => new Array(n).fill(Infinity));

for (let i = 2; i < input.length; i++) {
    const [a, b, c] = input[i];
    routes[a - 1][b - 1] = c
}

floydWarshall();
console.log(routes);
