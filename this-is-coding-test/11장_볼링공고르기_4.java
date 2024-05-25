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
        int[] ballingBalls = new int[M + 1];
        for (int i = 0; i < N; i++) {
            ballingBalls[Integer.parseInt(st2.nextToken())] += 1;
        }

        int total = 0;
        for (int i = 1; i <= M; i++) {
            // 본인 보다 무거운 볼링공 갯수만 남도록 현재 무게의 볼링공 갯수 제거
            N -= ballingBalls[i];
            total += N * ballingBalls[i];
        }
    }
}
