import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] soldiers = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            soldiers[i] = Integer.parseInt(st.nextToken());
        }

        ArrayList<Integer> dp = new ArrayList<Integer>();

        for (int i = 0; i < N; i++) {
            int soldier = soldiers[i];

            if (dp.isEmpty()) {
                dp.add(soldier);
                continue;
            }

            // "병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치" 한다는 조건에 유의
            if (dp.get(dp.size() - 1) > soldier) {
                dp.add(soldier);
            } else {
                dp.set(getIdx(dp, soldier), soldier);
            }
        }

        System.out.println(N - dp.size());
    }

    public int getIdx(ArrayList<Integer> arr, int target) {
        int low = 0;
        int high = arr.size() - 1;

        while (low < high) {
            int mid = (low + high) / 2;

            if (target >= arr.get(mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return high;
    }
}
