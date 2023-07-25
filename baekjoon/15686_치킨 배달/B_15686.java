import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            StringTokenizer info = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                int cityDetail = Integer.parseInt(info.nextToken());

                if (cityDetail == 1) {
                    house.add(new int[]{i, j});
                } else if (cityDetail == 2) {
                    chicken.add(new int[]{i, j});
                }
            }
        }

        getCombination(0, M, 0, chicken.size(), new int[M]);
        System.out.println(minSumDistance);
    }

    private static final ArrayList<int[]> house = new ArrayList<int[]>();

    private static final ArrayList<int[]> chicken = new ArrayList<int[]>();

    private static int minSumDistance = 2500;

    private static void getCombination(int cnt, int cntLimit, int idx, int idxLimit, int[] comb) {
        if (cnt == cntLimit) {
            calculateMinDistance(comb);
            return;
        }

        for (int i = idx; i < idxLimit; i++) {
            comb[cnt] = i;
            getCombination(cnt + 1, cntLimit, i + 1, idxLimit, comb);
        }
    }

    private static void calculateMinDistance(int[] combination) {
        // 집마다 치킨집과의 최소 거리를 구한다
        // 최소 거리 합의 최소 값을 구한다
        int sumDistance = 0;

        for (int[] h: house) {
            int minDistancePerHome = 2500;

            int hY = h[0];
            int hX = h[1];

            for (int comb: combination) {
                int[] c = chicken.get(comb);
                int cY = c[0];
                int cX = c[1];
                int distance = Math.abs(hY - cY) + Math.abs(hX - cX);
                minDistancePerHome = Math.min(minDistancePerHome, distance);
            }

            sumDistance += minDistancePerHome;
        }

        minSumDistance = Math.min(minSumDistance, sumDistance);
    }
}
