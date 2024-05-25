import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 전체 조합에서 같은 무게 조합을 뺀다
        // 전체 조합은
        // nC2 로 구하고
        // 같은 무게 조합은
        // 같은 무게가 2개 이상인 공을 키로 하고
        // 무게별 공의 갯수를 값으로 하는 맵을 구한다
        // 맵에서 무게별로 nC2 를 구하고 이 총합을
        // 전체 조합에서 뺀다
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st1.nextToken());
        int M = Integer.parseInt(st1.nextToken());

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int[] ballingBalls = new int[N];
        for (int i = 0; i < N; i++) {
            ballingBalls[i] = Integer.parseInt(st2.nextToken());
        }

        HashMap<Integer, Integer> duplicatedBalls = new HashMap<>();
        for (int ball : ballingBalls) {
            if (duplicatedBalls.containsKey(ball)) {
                duplicatedBalls.put(ball, duplicatedBalls.get(ball) + 1);
            } else {
                duplicatedBalls.put(ball, 1);
            }
        }

        System.out.println((N * (N - 1) / 2) - getDuplicatedCombinations(duplicatedBalls));
    }

    private static int getDuplicatedCombinations(HashMap<Integer, Integer> balls) {
        return balls
                .values()
                .stream()
                .filter(b -> b > 1)
                .reduce(0,
                        (acc, cur) -> acc + (cur * (cur - 1) / 2));
    }
}
