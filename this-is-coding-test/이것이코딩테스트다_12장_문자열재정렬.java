import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        ArrayList<Character> arr = new ArrayList<Character>();
        int nums = 0;

        for (int i = 0; i < S.length(); i++) {
            char s = S.charAt(i);
            if (Character.isAlphabetic(s)) {
                arr.add(s);
            } else {
                nums += s - '0';
            }
        }

        Collections.sort(arr);

        StringBuilder sb = new StringBuilder();

        for (Character character : arr) {
            sb.append(character);
        }

        sb.append(String.valueOf(nums));

        System.out.println(sb);

        br.close();
    }
}
