import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static int[] arr = new int[2];

    public static int total = 0;

    public static int N;

    public static int M;

    public static int[] balls;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st1.nextToken());
        M = Integer.parseInt(st1.nextToken());

        StringTokenizer st2 = new StringTokenizer(br.readLine());

        balls = new int[N];

        for (int i = 0; i < N; i++) {
            balls[i] = Integer.parseInt(st2.nextToken());
        }

        // 정렬을 통해 중복된 조합이 나오지 않도록 한다
        // 예를 들어 (1, 2) 가 나왔는데 (2, 1) 이 나오지 않도록 한다
        Arrays.sort(balls);

        getCombinations(0, 0);

        System.out.println(total);
    }

    public static void getCombinations(int cnt, int idx) {
        if (cnt == 2) {
            total += 1;
            return;
        }

        for (int i = idx; i < N; i++) {
            if (cnt == 0 || arr[0] != balls[i]) {
                arr[cnt] = balls[i];
                // idx 를 1 씩 늘려 나가면서 이전 보다 같거나 더 큰 값을 찾도록 한다
                // balls 는 정렬되어 있어서 idx 를 올리면 가능하다
                getCombinations(cnt + 1, i + 1);
            }
        }
    }
}