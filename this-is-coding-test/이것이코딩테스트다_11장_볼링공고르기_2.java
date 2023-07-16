import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st1.nextToken());
        int M = Integer.parseInt(st1.nextToken());

        StringTokenizer st2 = new StringTokenizer(br.readLine());

        int[] balls = new int[N];

        for (int i = 0; i < N; i++) {
            balls[i] = Integer.parseInt(st2.nextToken());
        }

        int[] ballCount = new int[M + 1];

        for (int i = 0; i < N; i++) {
            ballCount[balls[i]] += 1;
        }

        int total = 0;

        for (int cnt: ballCount) {
            N -= cnt;
            total += N * cnt;
        }

        System.out.println(total);
    }
}