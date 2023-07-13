import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        String[] arrayS = S.split("");

        int prev = -1;
        int[] cnt = new int[]{0, 0};

        for (int i = 0; i < arrayS.length; i++) {
            int cur = Integer.parseInt(arrayS[i]);

            if (prev == cur) {
                continue;
            }

            prev = cur;
            cnt[cur] += 1;
        }

        System.out.println(Arrays.stream(cnt).min().getAsInt());
    }
}
