import java.util.ArrayDeque;
import java.util.Queue;

public class Programmers1844 {
    public int solution(int[][] maps) {
        Queue<int[]> deq = new ArrayDeque<>();
        int n = maps.length;
        int m = maps[0].length;
        int[] yValue = new int[]{-1, 0, 1, 0};
        int[] xValue = new int[]{0, 1, 0, -1};
        // y축, x축, 이동횟수
        deq.add(new int[]{0, 0, 1});
        maps[0][0] = 0;

        while (!deq.isEmpty()) {
            int[] start = deq.poll();

            for (int i = 0; i < 4; i++) {
                int y = start[0] + yValue[i];
                int x = start[1] + xValue[i];
                if (start[0] == n - 1 && start[1] == m - 1) return start[2];
                if (y < 0 || y >= n || x < 0 || x >= m) continue;
                if (maps[y][x] == 0) continue;
                maps[y][x] = 0;
                deq.add(new int[]{y, x, start[2] + 1});
            }
        }
        return -1;
    }
}
