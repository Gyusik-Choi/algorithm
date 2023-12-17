import java.util.ArrayDeque;

public class Main {
    public static void main(String[] args){
        Solution solution = new Solution();
        int[][] maps = {{1,0,1,1,1}, {1,0,1,0,1}, {1,0,1,1,1}, {1,1,1,0,1}, {0,0,0,0,1}};
        System.out.println(solution.solution(maps));
    }
}

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        return bfs(maps, n, m);
    }

    private static int bfs(int[][] maps, int n, int m) {
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;

        int[] yValue = {-1, 0, 1, 0};
        int[] xValue = {0, 1, 0, -1};

        ArrayDeque<int[]> deq = new ArrayDeque<>();
        deq.add(new int[]{0, 0, 1});

        while (!deq.isEmpty()) {
            int[] item = deq.pollFirst();
            int y = item[0];
            int x = item[1];
            int cnt = item[2];

            for (int i = 0; i < 4; i++) {
                int yIdx = y + yValue[i];
                int xIdx = x + xValue[i];

                if (0 > yIdx || yIdx >= n || 0 > xIdx || xIdx >= m) {
                    continue;
                }

                if (yIdx == n - 1 && xIdx == m - 1) {
                    return cnt + 1;
                }

                if (visited[yIdx][xIdx]) {
                    continue;
                }

                if (maps[yIdx][xIdx] == 0) {
                    continue;
                }

                visited[yIdx][xIdx] = true;
                deq.add(new int[]{yIdx, xIdx, cnt + 1});
            }
        }

        return -1;
    }
}
