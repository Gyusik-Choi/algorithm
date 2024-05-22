import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        String[] splitWord = S.split("");

        int sums = 0;

        for (int i = 0; i < splitWord.length; i++) {
            int number = Integer.parseInt(splitWord[i]);

            if (sums < 2 || number < 2) {
                sums += number;
            } else {
                sums *= number;
            }
        }

        System.out.println(sums);
    }
}
