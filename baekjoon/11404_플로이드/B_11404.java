import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int[][] cities = new int[n][n];
        int maxValue = 100000 * (100 - 1) + 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    cities[i][j] = maxValue;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            cities[a - 1][b - 1] = Math.min(cities[a - 1][b - 1], c);
        }

        floydWarshall(cities);
        System.out.println(getAnswerFormat(cities, maxValue));

    }

    public void floydWarshall(int[][] cityInfo) {
        for (int k = 0; k < cityInfo.length; k++) {
            for (int i = 0; i < cityInfo.length; i++) {
                for (int j = 0; j < cityInfo.length; j++) {
                    cityInfo[i][j] = Math.min(cityInfo[i][j], cityInfo[i][k] + cityInfo[k][j]);
                }
            }
        }
    }

    public String getAnswerFormat(int[][] cityInfo, int limit) {
        StringBuilder sb = new StringBuilder();

        for (int[] cities : cityInfo) {
            for (int city : cities) {
                if (city == limit) {
                    sb.append(0);
                } else {
                    sb.append(city);
                }
                sb.append(" ");
            }
            sb.append("\n");
        }

        return sb.toString();
    }
}
