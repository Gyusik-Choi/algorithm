import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static int N;

    public static String[][] corridorInfo;

    public static ArrayList<int[]> empty = new ArrayList<int[]>();

    public static ArrayList<int[]> teachers = new ArrayList<int[]>();

    public static ArrayList<int[]> obstacleCombinations = new ArrayList<int[]>();

    public static int[] yValue = new int[]{-1, 0, 1, 0};

    public static int[] xValue = new int[]{0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        corridorInfo = new String[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                String cor = st.nextToken();
                corridorInfo[i][j] = cor;

                if (cor.equals("X")) {
                    empty.add(new int[]{i, j});
                } else if (cor.equals("T")) {
                    teachers.add(new int[]{i, j});
                }
            }
        }

        getCombinations(0, 0, new int[3]);

        boolean isPossibleToAvoid = false;

        for (int[] obstacles: obstacleCombinations) {
            if (dfs(obstacles)) {
                isPossibleToAvoid = true;
                break;
            }
        }

        System.out.println(isPossibleToAvoid ? "YES" : "NO");
    }

    public static void getCombinations(int cnt, int idx, int[] comb) {
        if (cnt == 3) {
            obstacleCombinations.add(new int[]{comb[0], comb[1], comb[2]});
            return;
        }

        for (int i = idx; i < empty.size(); i++) {
            comb[cnt] = i;
            getCombinations(cnt + 1, i + 1, comb);
        }
    }

    public static boolean dfs(int[] comb) {
        String[][] newCorridor = getNewCorridorWithObstacles(comb);

        for (int i = 0; i < teachers.size(); i++) {
            int[] teacher = teachers.get(i);
            int y = teacher[0];
            int x = teacher[1];

            if (!dfsPerTeacher(newCorridor, y, x)) {
                return false;
            };
        }

        return true;
    }

    public static String[][] getNewCorridorWithObstacles(int[] comb) {
        String[][] newCorridor = getNewCorridor();

        for (int i = 0; i < 3; i++) {
            int emptyItem = comb[i];
            int[] emptyIdx = empty.get(emptyItem);
            int y = emptyIdx[0];
            int x = emptyIdx[1];
            newCorridor[y][x] = "O";
        }

        return newCorridor;
    }

    public static String[][] getNewCorridor() {
        String[][] newCorridor = new String[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                newCorridor[i][j] = corridorInfo[i][j];
            }
        }

        return newCorridor;
    }

    public static boolean dfsPerTeacher(String[][] newCorridor, int y, int x) {
        for (int dir = 0; dir < 4; dir++) {
            // 각 방향 간의 값이 누적되지 않도록
            // for 문을 시작하기 전에 값을 초기화
            int yIdx = y;
            int xIdx = x;

            while (true) {
                // 같은 방향에서는 값을 누적
                yIdx = yIdx + yValue[dir];
                xIdx = xIdx + xValue[dir];

                if (0 > yIdx || yIdx >= N || 0 > xIdx || xIdx >= N) {
                    break;
                }

                if (newCorridor[yIdx][xIdx].equals("O")) {
                    break;
                }

                if (newCorridor[yIdx][xIdx].equals("S")) {
                    return false;
                }
            }
        }

        return true;
    }
}
