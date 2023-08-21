import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();
        int[][] arr = new int[b.length() + 1][a.length() + 1];

        // y축 초기값 설정
        for (int i = 0; i < b.length(); i++) {
            arr[i + 1][0] = arr[i][0] + 1;
        }

        // x축 초기값 설정
        for (int j = 0; j < a.length(); j++) {
            arr[0][j + 1] = arr[0][j] + 1;
        }

        for (int i = 0; i < b.length(); i++) {
            for (int j = 0; j < a.length(); j++) {
                if (b.charAt(i) == a.charAt(j)) {
                    arr[i + 1][j + 1] = arr[i][j];
                } else {
                    arr[i + 1][j + 1] = Math.min(arr[i + 1][j], Math.min(arr[i][j], arr[i][j + 1])) + 1;
                }
            }
        }

        System.out.println(arr[b.length()][a.length()]);
    }
}
