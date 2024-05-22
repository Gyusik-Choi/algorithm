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

        Arrays.sort(coins);

        int min_val = 1;

        for (int i = 0; i < N; i++) {
            if (min_val < coins[i]) {
                break;
            }

            min_val += coins[i];
        }

        System.out.println(min_val);
    }
}
