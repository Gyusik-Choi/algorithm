import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            System.out.println(solutionByTestCase(br));
        }
    }

    public int solutionByTestCase(BufferedReader br) throws IOException {
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 위처럼
        // BufferedReader 인스턴스를 새로 생성해서 입력 받은 값을 StringTokenizer 의 인자로 넣으니
        // st.countTokens() 값이 0으로 나온다
        // token 이 없다고 나오니
        // int n = Integer.parseInt(st.nextToken()); 에서
        // NoSuchElementException 에러가 발생한다
        // (Exception in thread "main" java.util.NoSuchElementException)
        //
        // solution 함수에서 생성한 BufferedReader 인스턴스를 넘겨 받아서 입력을 처리하니
        // 에러가 발생하지 않았다
        // 왜 이렇게 하면 에러가 발생하지 않고
        // 위와 같이 새로운 BufferedReader 인스턴스를 생성 했을 때는 에러가 발생 하는지
        // 아직 파악하지 못했다
        //
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] goldMine = new int[n][m];
        StringTokenizer st2 = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int cnt = Integer.parseInt(st2.nextToken());
                goldMine[i][j] = cnt;
            }
        }

        int[][] dp = new int[n][m];

        for (int i = 0; i < n; i++) {
            dp[i][0] = goldMine[i][0];
        }

        for (int j = 1; j < m; j++) {
            for (int i = 0; i < n; i++) {
                if (i == 0) {
                    // n 이 1인 경우
                    if (n == 1) {
                        dp[i][j] = dp[i][j - 1] + goldMine[i][j];
                    } else {
                        dp[i][j] = Math.max(dp[i][j - 1], dp[i + 1][j - 1]) + goldMine[i][j];
                    }
                } else if (i == n - 1) {
                    // 위 if (i ==0) 에서 n 이 1인 경우를 처리 해서
                    // n 이 1인 경우 이곳에 들어올 수 없다
                    dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i][j - 1]) + goldMine[i][j];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j - 1], Math.max(dp[i][j - 1], dp[i + 1][j - 1])) + goldMine[i][j];
                }
            }
        }

        int maxValue = 0;

        for (int i = 0; i < n; i++) {
            maxValue = Math.max(maxValue, dp[i][m - 1]);
        }

        return maxValue;
    }

}