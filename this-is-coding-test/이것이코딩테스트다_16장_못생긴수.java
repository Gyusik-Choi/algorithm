import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int num2 = 2;
        int num3 = 3;
        int num5 = 5;

        int i2 = 1;
        int i3 = 1;
        int i5 = 1;

        int[] answer = new int[n];
        answer[0] = 1;

        for (int i = 1; i < n; i++) {
            int minNum = Math.min(num2, Math.min(num3, num5));
            answer[i] = minNum;

            if (minNum == num2) {
                i2 += 1;
                num2 = answer[i2] * 2;
            }

            if (minNum == num3) {
                i3 += 1;
                num3 = answer[i3] * 3;
            }

            if (minNum == num5) {
                i5 += 1;
                num5 = answer[i5] * 5;
            }
        }
        
        System.out.println(answer[n - 1]);
    }
}
