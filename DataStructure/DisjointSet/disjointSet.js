class DisjointSet {
    constructor(n) {
        this.p = new Array(n).fill(0);
        this.init(n);
    }

    init(n) {
        for (let i = 1; i <= n; i++) {
            this.makeSet(i);
        }
    }

    makeSet(x) {
        this.p[x] = x;
    }

    findSet(x) {
        if (this.p[x] == x) {
            return this.p[x]
        }

        this.p[x] = this.findSet(this.p[x])
        return this.p[x]
    }

    unionSet(x, y) {
        const px = this.findSet(x);
        const py = this.findSet(y);

        this.p[py] = px;
    }
}

const disjointSet = new DisjointSet(8);
disjointSet.unionSet(1, 3);
disjointSet.unionSet(2, 3);
disjointSet.unionSet(5, 6);
disjointSet.unionSet(6, 8);
disjointSet.unionSet(1, 5);
disjointSet.unionSet(6, 7);
console.log(disjointSet);
