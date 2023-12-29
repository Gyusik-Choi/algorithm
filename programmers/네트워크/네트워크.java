import java.util.ArrayList;
import java.util.HashMap;

public class Main {
    public static void main(String[] args){
        Solution solution = new Solution();
//        System.out.println(solution.solution(3, new int[][]{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}}));
        System.out.println(solution.solution(3, new int[][]{{1, 1, 0}, {1, 1, 1}, {0, 1, 1}}));

    }
}

class Solution {
    public int solution(int n, int[][] computers) {
        HashMap<Integer, ArrayList<Integer>> edges = new HashMap<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }

                if (computers[i][j] == 0) {
                    continue;
                }

                ArrayList<Integer> value;
                if (edges.containsKey(i)) {
                    value = edges.get(i);
                } else {
                    value = new ArrayList<>();
                }
                value.add(j);
                edges.put(i, value);
            }
        }

        boolean[] visit = new boolean[n];
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            if (!visit[i]) {
                visit[i] = true;
                cnt += 1;
                dfs(i, edges, visit);
            }
        }

        return cnt;
    }

    private void dfs(int start, HashMap<Integer, ArrayList<Integer>> nodes, boolean[] visited) {
        if (!nodes.containsKey(start)) {
            return;
        }

        for (int end : nodes.get(start)) {
            if (!visited[end]) {
                visited[end] = true;
                dfs(end, nodes, visited);
            }
        }
    }
}
