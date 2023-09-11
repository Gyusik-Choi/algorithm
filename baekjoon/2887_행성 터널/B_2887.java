import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        System.out.println(main.solution());
    }

    public int solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] xPlanets = new int[N][4];
        int[][] yPlanets = new int[N][4];
        int[][] zPlanets = new int[N][4];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());

            xPlanets[i] = new int[]{x, y, z, i};
            yPlanets[i] = new int[]{x, y, z, i};
            zPlanets[i] = new int[]{x, y, z, i};
        }

        // x 좌표 기준 정렬
        Arrays.sort(xPlanets, Comparator.comparingInt(x -> x[0]));
        // y 좌표 기준 정렬
        Arrays.sort(yPlanets, Comparator.comparingInt(y -> y[1]));
        // z 좌표 기준 정렬
        Arrays.sort(zPlanets, Comparator.comparingInt(z -> z[2]));

        ArrayList<int[]> arr = new ArrayList<int[]>();

        for (int i = 0; i < N - 1; i++) {
            arr.add(new int[]{
                xPlanets[i][3],
                xPlanets[i + 1][3],
                Math.min(
                    Math.abs(xPlanets[i][0] - xPlanets[i + 1][0]),
                    Math.min(
                        Math.abs(xPlanets[i][1] - xPlanets[i + 1][1]),
                        Math.abs(xPlanets[i][2] - xPlanets[i + 1][2])
                    ))
                }
            );

            arr.add(new int[]{
                yPlanets[i][3],
                yPlanets[i + 1][3],
                Math.min(
                    Math.abs(yPlanets[i][0] - yPlanets[i + 1][0]),
                    Math.min(
                        Math.abs(yPlanets[i][1] - yPlanets[i + 1][1]),
                        Math.abs(yPlanets[i][2] - yPlanets[i + 1][2])
                    ))
                }
            );

            arr.add(new int[]{
                zPlanets[i][3],
                zPlanets[i + 1][3],
                Math.min(
                    Math.abs(zPlanets[i][0] - zPlanets[i + 1][0]),
                    Math.min(
                        Math.abs(zPlanets[i][1] - zPlanets[i + 1][1]),
                        Math.abs(zPlanets[i][2] - zPlanets[i + 1][2])
                    ))
                }
            );
        }

        arr.sort(Comparator.comparingInt(a -> a[2]));

        DisjointSet disjointSet = new DisjointSet(N);
        int answer = 0;
        int cnt = 0;

        for (int i = 0; i < arr.size(); i++) {
            int[] item = arr.get(i);
            int start = item[0];
            int end = item[1];
            int dist = item[2];

            if (disjointSet.findSet(start) == disjointSet.findSet(end)) {
                continue;
            }

            disjointSet.unionSet(start, end);
            answer += dist;
            cnt += 1;

            if (cnt == N - 1) {
                break;
            }
        }

        return answer;
    }
}

class DisjointSet {

    int n;
    int[] p;

    DisjointSet(int n) {
        this.n = n;
        this.p = new int[n];

        for (int i = 0; i < n; i++) {
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
