import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        String answer = main.solution();
        System.out.println(answer);
    }

    public String solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer travelMetaData = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(travelMetaData.nextToken());
        int M = Integer.parseInt(travelMetaData.nextToken());
        DisjointSet disjointSet = new DisjointSet(N);

        for (int i = 0; i < N; i++) {
            StringTokenizer row = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                int r = Integer.parseInt(row.nextToken());

                if (r == 1) {
                    disjointSet.unionSet(i + 1, j + 1);
                }
            }
        }

        int[] cityInfo = new int[M];
        StringTokenizer cities = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int c = Integer.parseInt(cities.nextToken());
            cityInfo[i] = c;
        }

        for (int i = 0; i < M - 1; i++) {
            int start = cityInfo[i];
            int end = cityInfo[i + 1];

            if (disjointSet.findSet(start) != disjointSet.findSet(end)) {
                return "NO";
            }
        }

        return "YES";
    }
}

class DisjointSet {
    int n;
    int[] p;

    DisjointSet(int n) {
        this.n = n;
        p = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
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

        if (px >= py) {
            p[px] = py;
        } else {
            p[py] = px;
        }
    }
}
