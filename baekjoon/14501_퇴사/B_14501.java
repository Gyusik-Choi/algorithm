import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][2];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            arr[i][0] = t;
            arr[i][1] = p;
        }

        System.out.println(getMaxProfit(N, arr));
    }

    private int getMaxProfit(int n, int[][] array) {
        int[] dp = new int[n];

        // 초기값 설정
        // 상담이 가능한 날짜만 초기값을 설정한다
        // 3
        // 1 10
        // 2 20
        // 2 30
        // 입력 값이 위와 같으면
        // 첫번째, 두번째 날은 상담이 가능한데
        // 세번째 날은 상담이 불가능 해서 0으로 둔다
        //
        // 초기값이 필요한 이유는
        // 4
        // 3 1
        // 1 100
        // 2 100
        // 1 1000
        // 입력 값이 위와 같으면
        // 세번째 날인 2 100 의 최대값은
        // 두번째 날과 세번째 날을 합해서 300이다
        // 만약 초기값을 설정하지 않으면
        // 세번째 날의 최대값을 구할때 (for 문 i = 2 일때)
        // dp[i] = Math.max(dp[i], dp[j] + array[i][1]);
        // 에서 두번째 날의 최대값인 dp[j] 는 100이 아니라 0이다
        for (int i = 0; i < n; i++) {
            if (i + array[i][0] <= n) {
                dp[i] = array[i][1];
            }
        }

        // 7
        // 3 10
        // 5 20
        // 1 10
        // 1 20
        // 2 15
        // 4 40
        // 2 200
        // 입력 값이 위와 같으면
        // 4 40
        // 2 200 처럼 상담이 안 되는 날짜는
        // 아예 dp 값을 갱신하지 않는다
        // 위에서 초기값을 설정하는 부분에서도
        // 상담이 안 되는 날에는 초기값을 설정하지 않았다
        // i + array[i][0] <= n
        // 위의 코드가 위와 아래에 중복으로 사용되고 있는데
        // 초기값 설정과 함께
        // dp 값을 갱신할 때도 해당 조건이 있어야
        // 상담이 가능한 날짜에 대해서만 dp 값을 구할 수 있다
        // dp 배열 중 최대값을 구할 때 (findMax 함수) 는
        // 상담이 가능하지 않은 날짜는 값이 0 이라서
        // 별도의 조건 없이 최대값을 바로 구할 수 있다
        //
        // 현재 날짜 (i) 보다
        // 이전 날짜 (j) 중에서
        // 이전 날짜에 상담을 했다면
        // 현재 날짜도 상담이 가능한 경우
        // 직전 날짜의 dp 값과 현재 날짜의 수익을 더해서
        // 현재 날짜의 dp 값과 비교 한다
        // 현재 날짜의 dp 값과 비교하는 이유는
        // 현재 날짜의 dp 값이 계속 수정될 수 있어서
        // 이미 수정된 값이 새로 구한 값보다 클 수 있어서
        // 큰 값을 유지하기 위해 비교가 필요하다
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (i + array[i][0] <= n && i - (j + array[j][0]) >= 0) {
                    dp[i] = Math.max(dp[i], dp[j] + array[i][1]);
                }
            }
        }

        return findMax(n, dp);
    }

    private int findMax(int n, int[] dp) {
        // 값을 무조건 누적해 오지 않아서
        // 최대 수익을 따로 구해야 한다
        return Arrays.stream(dp).max().getAsInt();
    }
}
