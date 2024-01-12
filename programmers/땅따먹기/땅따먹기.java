import java.util.Arrays;

import static java.lang.Math.*;

public class Main {
    public static void main(String[] args){
        Solution solution = new Solution();
        System.out.println(solution.solution(new int[][]{{1, 2, 3, 5}, {5, 6, 7, 8}, {4, 3, 2, 1}}));
    }
}

class Solution {
    int solution(int[][] land) {
        int n = land.length;
        int[][] dp = new int[n][4];
        System.arraycopy(land[0], 0, dp[0], 0, 4);

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    if (j == k) {
                        continue;
                    }
                    dp[i][j] = max(dp[i][j], dp[i - 1][k]);
                }
                dp[i][j] += land[i][j];
            }
        }

        return Arrays.stream(dp[n - 1]).max().getAsInt();
    }
}
