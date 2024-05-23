import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] coins = new int[N];
        for (int i = 0; i < N; i++) {
            coins[i] = Integer.parseInt(st.nextToken());
        }
        int[] sortedCoins = Arrays
                .stream(coins)
                .sorted()
                .toArray();

        int sums = 1;
        for (int coin : sortedCoins) {
            if (coin > sums) {
                break;
            }
            sums += coin;
        }

        System.out.println(sums);

        // sums 는 1부터 시작한다
        // sums 보다 큰 동전이 나오면 안 된다
        // 1, 1, 1 이 나왔다고 하면 3원까지 만들 수 있고
        // sums 는 1부터 시작했으니 4다.
        // 실제로 다음 동전으로 4이하까지 가능하고
        // 5이상은 안 된다
    }
}
