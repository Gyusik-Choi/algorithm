import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] nums = Arrays
                .stream(br.readLine().split(""))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] cnt = new int[2];
        int prev = -1;
        for (int num : nums) {
            if (num != prev) {
                cnt[num] += 1;
                prev = num;
            }
        }

        System.out.println(Math.min(cnt[0], cnt[1]));
    }
}
