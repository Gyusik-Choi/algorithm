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

        int[] adventurers = new int[N];
        for (int i = 0; i < N; i++) {
            adventurers[i] = Integer.parseInt(st.nextToken());
        }
        int[] sortedAdventurers = Arrays
                .stream(adventurers)
                .sorted()
                .toArray();

        int total = 0;
        int cnt = 0;
        for (int a : sortedAdventurers) {
            cnt += 1;
            if (cnt == a) {
                total += 1;
                cnt = 0;
            }
        }

        System.out.println(total);
    }
}
