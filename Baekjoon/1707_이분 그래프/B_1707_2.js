const Node = function(value, next = null) {
    this.value = value;
    this.next = next;
}

const Queue = function() {
    this.head = new Node(null);
    this.tail = this.head;
}

Queue.prototype.isEmpty = function() {
    return this.head.value === null;
}

Queue.prototype.enQueue = function(value) {
    if (this.isEmpty()) {
        this.head = new Node(value);
        this.tail = this.head;
    } else {
        const tail = this.tail;
        this.tail = new Node(value);
        tail.next = this.tail;
    }
}

Queue.prototype.deQueue = function() {
    if (this.isEmpty() === false) {
        const popItem = this.head.value;

        if (this.head === this.tail) {
            this.head = new Node(null);
            this.tail = this.head;
        } else {
            this.head = this.head.next;
        }

        return popItem;
    }
}

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const K = parseInt(input[0]);
let idx = 1;
for (let i = 0; i < K; i++) {
    const bfs = function(start) {
        const q = new Queue();
        q.enQueue(start);

        while (q.isEmpty() === false) {
            const vertexFrom = q.deQueue();
            
            if (graph[vertexFrom].length > 0) {
                for (let l = 0; l < graph[vertexFrom].length; l++) {
                    const vertexTo = graph[vertexFrom][l];
                    
                    if (visited[vertexFrom] === visited[vertexTo]) {
                        return false;
                    }

                    if (visited[vertexTo] === 0) {
                        if (visited[vertexFrom] === 1) {
                            visited[vertexTo] = 2;
                        } else {
                            visited[vertexTo] = 1;
                        }

                        q.enQueue(vertexTo);
                    }
                }
            }
        }

        return true;
    }

    const [V, E] = input[idx].split(' ').map(v => parseInt(v));
    let graph = new Array(V + 1).fill(0).map(v => new Array());
    // 미방문 0, 방문은 1과 2로 구분
    let visited = new Array(V + 1).fill(0);

    for (let j = idx + 1; j < idx + 1 + E; j++) {
        const [u, v] = input[j].split(' ').map(v => parseInt(v));
        graph[u].push(v);
        graph[v].push(u);
    }

    let flag = true;
    for (let k = 1; k <= V; k++) {
        if (visited[k] === 0) {
            visited[k] = 1;
            const result = bfs(k);

            if (result === false) {
                flag = false;
                break;
            }
        }
    }

    flag === true ? console.log("YES") : console.log("NO");

    idx += 1 + E;
}

// 간선들이 모두 연결되어 있지 않을 수 있다