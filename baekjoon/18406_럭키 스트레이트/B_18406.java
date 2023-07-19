import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String N = br.readLine();

        int length = N.length();
        int half = length / 2;

        String[] left = N.substring(0, half).split("");
        String[] right = N.substring(half).split("");

        int leftSum = 0;
        int rightSum = 0;

        for (int i = 0; i < half; i++) {
            leftSum += Integer.parseInt(left[i]);
            rightSum += Integer.parseInt(right[i]);
        }

        System.out.println(leftSum == rightSum ? "LUCKY" : "READY");
        br.close();
    }
}
