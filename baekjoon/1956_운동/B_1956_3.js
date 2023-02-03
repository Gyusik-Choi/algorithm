const MinHeap = function() {
    this.arr = [null]
    
    MinHeap.prototype.insert = function(item) {
        this.arr.push(item)
    
        let idx = this.arr.length - 1
        while (idx > 1) {
            if (this.arr[Math.floor(idx / 2)][0] > this.arr[idx][0]) {
                let temp = this.arr[idx]
                this.arr[idx] = this.arr[Math.floor(idx / 2)]
                this.arr[Math.floor(idx / 2)] = temp
    
                idx = Math.floor(idx / 2)
            } else {
                break
            }
        }
    }
    
    MinHeap.prototype.remove = function() {
        if (this.arr.length < 2) {
            return
        }
    
        if (this.arr.length < 3) {
            const item = this.arr.pop()
            return item
        }
        
        let temp = this.arr[this.arr.length - 1]
        this.arr[this.arr.length - 1] = this.arr[1]
        this.arr[1] = temp
    
        const item = this.arr.pop()
        this.minHeapify(1)
        return item
    }
    
    MinHeap.prototype.minHeapify = function(idx) {
        let parentIdx = idx
        let leftChildIdx = idx * 2
        let rightChildIdx = idx * 2 + 1

        if (parentIdx * 2 < this.arr.length && this.arr[parentIdx][0] > this.arr[leftChildIdx][0]) {
            parentIdx = leftChildIdx
        } 

        if (parentIdx * 2 + 1 < this.arr.length && this.arr[parentIdx][0] > this.arr[rightChildIdx][0]) {
            parentIdx = rightChildIdx
        }

        if (parentIdx != idx) {
            let temp = this.arr[parentIdx]
            this.arr[parentIdx] = this.arr[idx]
            this.arr[idx] = temp

            return this.minHeapify(parentIdx)
        }
    }
}

const dijkstra = function(go) {
    let selected = new Array(V + 1).fill(false)
    let distance = new Array(V + 1).fill(Infinity)
    // distance[go] = 0
    // 출발점을 0으로 초기화하면 안 된다
    // 기존의 다익스트라 방식과 다른데
    // 기존의 다익스트라와 접근이 다르기 때문에 그럴 수 밖에 없다
    // 기존의 다익스트라는 출발점을 기준으로 나머지 정점들에 대한 최단 거리를 구하지만
    // 이번 다익스트라는 출발점을 기준으로 나머지 정점들에 대한 최단 거리를 구하고 + 정점들로부터 출발점으로 돌아오는 최단 거리도 필요하다
    // 사이클의 최단 거리를 구하는 문제라 출발점을 0으로 세팅해버리면 출발점으로 돌아오는 거리를 구할 수 없다
    // 왜냐하면 0이라서 다른 정점들에서 출발점까지의 거리 값으로 업데이트 될 수 없다(0이 이미 제일 작으므로)

    // 갈 수 있는 경로가 없다
    if (roads[go].length === 0) {
        return Infinity
    }

    mh = new MinHeap()

    roads[go].forEach((item) => {
        const [e, v] = item

        distance[e] = v
        mh.insert([distance[e], e])
    })

    while (mh.arr.length > 1) {
        [value, start] = mh.remove()

        if (selected[start]) {
            continue
        }

        selected[start] = true

        if (go === start) {
            return value
        }

        if (roads[start].length > 0) {
            roads[start].forEach((item) => {
                const [e, v] = item
                
                if (!selected[e] && distance[e] > distance[start] + v) {
                    distance[e] = distance[start] + v
                    mh.insert([distance[e], e])
                }
            })
        }
    }

    return Infinity
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [V, E] = input[0].split(' ').map(v => Number(v))
let roads = new Array(V + 1).fill(Infinity).map(v => new Array(V + 1))

for (let i = 1; i <= E; i++) {
    const [a, b, c] = input[i].split(' ').map(v => Number(v))
    roads[a].push([b, c])
}

let smallestDistance = Infinity
for (let i = 1; i <= V; i++) {
    smallestDistance = Math.min(smallestDistance, dijkstra(i))
}

console.log(smallestDistance === Infinity ? -1 : smallestDistance)

// N^3 에서 다익스트라를 통해 시간을 줄이고자 함
// 정점별로 다익스트라를 돌린다
// 다익스트라에서 우선순위 큐 사용
// 우선순위 큐에서 뽑은 출발점이 다익스트라를 돌리는 정점과 같다면 사이클이 형성된 것
// 그 중에서 가장 작은 값을 찾는다
