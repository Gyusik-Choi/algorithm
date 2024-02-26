import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args){
        Mst mst = new Mst();
        int minLength = mst.kruskal(
                7,
                11,
                new int[][]{
                        {0, 5, 60},
                        {0, 1, 32},
                        {0, 2, 31},
                        {0, 6, 51},
                        {1, 2, 21},
                        {2, 4, 46},
                        {2, 6, 25},
                        {3, 4, 34},
                        {3, 5, 18},
                        {4, 5, 40},
                        {4, 6, 51}
                }
        );
        System.out.println(minLength);
    }
}

class Mst {
    public int kruskal(int v, int e, int[][] edges) {
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        Arrays
            .stream(edges)
            .forEach((int[] edge) -> pq.add(new Edge(edge[0], edge[1], edge[2])));

        int minLength = 0;
        DisjointSet disjointSet = new DisjointSet(v);

        while (!pq.isEmpty()) {
            Edge edge = pq.poll();

            int px = disjointSet.findSet(edge.start);
            int py = disjointSet.findSet(edge.end);

            if (px == py) {
                continue;
            }

            minLength += edge.distance;
            disjointSet.unionSet(px, py);
        }

        return minLength;
    }
}

class DisjointSet {
    int size;
    int[] parent;

    DisjointSet(int size) {
        this.size = size;
        initParent(size);
        IntStream.range(0, size).forEach(this::makeSet);
    }

    void initParent(int size) {
        parent = new int[size];
    }

    void makeSet(int x) {
        parent[x] = x;
    }

    int findSet(int x) {
        if (parent[x] != x) {
            parent[x] = findSet(parent[x]);
        }
        return parent[x];
    }

    void unionSet(int x, int y) {
        int px = findSet(x);
        int py = findSet(y);

        if (px < py) {
            parent[py] = px;
        } else {
            parent[px] = py;
        }
    }
}

class Edge implements Comparable<Edge> {
    int start;
    int end;
    int distance;

    Edge(int start, int end, int distance) {
        this.start = start;
        this.end = end;
        this.distance = distance;
    }

    @Override
    public int compareTo(Edge edge) {
        return this.distance - edge.distance;
    }
}

// 참고
// https://blog.naver.com/ssarang8649/221038259400
// https://cjh5414.github.io/priorityqueue/
