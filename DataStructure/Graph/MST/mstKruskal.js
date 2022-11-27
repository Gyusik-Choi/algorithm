class DisjointSet {
    constructor(n) {
        this.p = new Array(n).fill(0);
        this.rank = new Array(n).fill(0);
        this.makeSet(n);
    }

    makeSet(n) {
        for (let i = 0; i < n; i++) {
            this.p[i] = i;
        }
    }

    findSet(x) {
        if (this.p[x] != x) {
            this.p[x] = this.findSet(this.p[x]);
        }
        return this.p[x];
    }

    unionSet(x, y) {
        const px = this.findSet(x);
        const py = this.findSet(y);

        this.p[py] = px;
        
//        if (this.rank[px] > this.rank[py]) {
//            this.p[py] = px;
//        } else {
//            this.p[px] = py;
//
//            if (this.rank[px] == this.rank[py]) {
//                this.rank[py] += 1;
//            }
//        }
    }

}

class MstKruskal {
    constructor(edges, n) {
        this.edges = edges;
        this.n = n;
        this.disjointSet = new DisjointSet(this.n);
    }

    getMinSums() {
        let minSums = 0;
        let cnt = 0;

        for (const edge of edges) {
            const [cost, start, end] = edge;

            if (this.disjointSet.findSet(start) === this.disjointSet.findSet(end)) {
                continue;
            }

            this.disjointSet.unionSet(start, end);
            minSums += cost;
            cnt += 1;

            if (cnt == this.n - 1) {
                break;
            }
        }

        return minSums;
    }
}

const input = [
    '7 11',
    '0 1 7',
    '0 3 5',
    '1 2 8',
    '1 3 9',
    '1 4 7',
    '2 4 5',
    '3 4 15',
    '3 5 6',
    '4 5 8',
    '4 6 9',
    '5 6 11',
]

const [N, M] = input[0].split(' ').map(v => parseInt(v));
let edges = [];

for (let i = 1; i <= M; i++) {
    const [start, end, cost] = input[i].split(' ').map(v => parseInt(v));
    edges.push([cost, start, end]);
}

edges.sort((a, b) => a[0] - b[0]);
const mstKruskal = new MstKruskal(edges, N);
console.log(mstKruskal.getMinSums());
