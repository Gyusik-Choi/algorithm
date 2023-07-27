import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    public static int N;

    public static int M;

    public static int[][] lab;

    public static int maxCnt = 0;

    public static int cntLimit = 3;

    public static int idxLimit;

    public static ArrayList<int[]> empty = new ArrayList<>();

    public static ArrayList<int[]> wall = new ArrayList<>();

    public static ArrayList<int[]> virus = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        lab = new int[N][M];

        for (int i = 0; i < N; i++) {
            StringTokenizer labMap = new StringTokenizer(br.readLine());

            for (int j = 0; j < M; j++) {
                int num = Integer.parseInt(labMap.nextToken());
                lab[i][j] = num;

                if (num == 0) {
                    empty.add(new int[]{i, j});
                    continue;
                }

                if (num == 1) {
                    wall.add(new int[]{i, j});
                    continue;
                }

                virus.add(new int[]{i, j});
            }
        }

        idxLimit = empty.size();
        findSafeAreaSize(0, 0, new int[3]);
        System.out.println(maxCnt);
        br.close();
    }

    private static void findSafeAreaSize(int cnt, int idx, int[] emptyComb) {
        if (cnt == cntLimit) {
            findMaxCnt(getNewLab(), emptyComb);
            return;
        }

        for (int i = idx; i < idxLimit; i++) {
            emptyComb[cnt] = i;
            findSafeAreaSize(cnt + 1, i + 1, emptyComb);
        }

    }

    private static void findMaxCnt(int[][] newLab, int[] emptyCombination) {
        for (int comb: emptyCombination) {
            int[] oneWall = empty.get(comb);
            newLab[oneWall[0]][oneWall[1]] = 1;
        }

        ArrayDeque<int[]> deq = new ArrayDeque<>(virus);
        bfs(deq, newLab);
        maxCnt = Math.max(maxCnt, countSafeArea(newLab));
    }

    private static int[][] getNewLab() {
        int[][] newLab = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                newLab[i][j] = lab[i][j];
            }
        }

        return newLab;
    }

    private static void bfs(ArrayDeque<int[]> q, int[][] newLab) {
        int[] yValue = new int[]{-1, 0, 1, 0};
        int[] xValue = new int[]{0, 1, 0, -1};

        while (!q.isEmpty()) {
            int[] v =  q.pollFirst();

            for (int i = 0; i < 4; i++) {
                int y = v[0] + yValue[i];
                int x = v[1] + xValue[i];

                // 영역 벗어남
                if (0 > y || y >= N || 0 > x || x >= M) {
                    continue;
                }

                // 벽 or 바이러스
                if (newLab[y][x] > 0) {
                    continue;
                }

                newLab[y][x] = 2;
                q.add(new int[]{y, x});
            }
        }
    }

    private static int countSafeArea(int[][] newLab) {
        int cnt = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (newLab[i][j] == 0) {
                    cnt += 1;
                }
            }
        }

        return cnt;
    }
}
