import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    public static int N;

    public static int L;

    public static int R;

    public static int[][] populations;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        populations = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer p = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                populations[i][j] = Integer.parseInt(p.nextToken());
            }
        }

        System.out.println(movePopulation());
    }

    public static int movePopulation() {
        int days = 0;

        while (true) {
            boolean[][] visit = getVisitedArr();
            boolean isMoved = false;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (visit[i][j]) {
                        continue;
                    }

                    if (bfs(visit, new int[]{i, j})) {
                        isMoved = true;
                    };
                }
            }

            if (!isMoved) {
                break;
            }

            days += 1;
        }

        return days;
    }

    public static boolean[][] getVisitedArr() {
        return new boolean[N][N];
    }

    public static boolean bfs(boolean[][] visited, int[] go) {
        ArrayDeque<int[]> deq = new ArrayDeque<int[]>();
        ArrayDeque<int[]> countries = new ArrayDeque<int[]>();
        visited[go[0]][go[1]] = true;
        deq.add(go);
        countries.add(go);

        int cnt = 1;
        int sums = populations[go[0]][go[1]];

        int[] yValue = new int[]{-1, 0, 1, 0};
        int[] xValue = new int[]{0, 1, 0, -1};

        while (!deq.isEmpty()) {
            int[] start = deq.pollFirst();
            int y = start[0];
            int x = start[1];

            for (int i = 0; i < 4; i++) {
                int yIdx = y + yValue[i];
                int xIdx = x + xValue[i];

                if (0 > yIdx || yIdx >= N || 0 > xIdx || xIdx >= N) {
                    continue;
                }

                if (visited[yIdx][xIdx]) {
                    continue;
                }

                if (!isCanMove(populations[y][x], populations[yIdx][xIdx])) {
                    continue;
                }

                visited[yIdx][xIdx] = true;
                deq.add(new int[]{yIdx, xIdx});
                countries.add(new int[]{yIdx, xIdx});
                cnt += 1;
                sums += populations[yIdx][xIdx];
            }
        }

        if (cnt == 1) {
            return false;
        }

        move(countries, sums / cnt);
        return true;
    }

    public static boolean isCanMove(int from, int to) {
        return L <= Math.abs(from - to) && Math.abs(from - to) <= R;
    }

    public static void move(ArrayDeque<int[]> countries, int avg) {
        for (int[] country: countries) {
            populations[country[0]][country[1]] = avg;
        }
    }
}
