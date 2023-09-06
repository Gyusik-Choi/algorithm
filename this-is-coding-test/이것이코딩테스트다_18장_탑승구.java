import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        System.out.println(main.solution());
    }

    public int solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int G = Integer.parseInt(br.readLine());
        int P = Integer.parseInt(br.readLine());

        DisjointSet disjointSet = new DisjointSet(G);
        int cnt = 0;

        for (int i = 0; i < P; i++) {
            int g = Integer.parseInt(br.readLine());
            int f = disjointSet.findSet(g);

            // 루트 노드가 0인 경우 도킹을 할 수 있는 탑승구가 없다
            if (f == 0) {
                break;
            }

            disjointSet.unionSet(f - 1, f);
            cnt += 1;
        }

        return cnt;
    }
}

class DisjointSet {
    int n;
    int[] p;

    DisjointSet(int n) {
        this.n = n;
        p = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            makeSet(i);
        }
    }

    void makeSet(int x) {
        p[x] = x;
    }

    int findSet(int x) {
        if (p[x] != x) {
            p[x] = findSet(p[x]);
        }
        return p[x];
    }

    void unionSet(int x, int y) {
        int px = findSet(x);
        int py = findSet(y);

        if (p[px] >= p[py]) {
            p[px] = py;
        } else {
            p[py] = px;
        }
    }
}
