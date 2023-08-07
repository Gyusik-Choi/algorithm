import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        System.out.println(main.solution());
    }

    public int solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int[] house = new int[N];
        for (int i = 0; i < N; i++) {
            house[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(house);

        return binarySearch(house, C);
    }

    public int binarySearch(int[] houses, int installNumber) {
        // int left = houses[0];
        // 위와 같이 하면 안 된다
        // left 는 시작 지점이 아니라 최소 거리가 되야 한다
        // 최소 거리부터 시작 하기 위해 1로 초기값 설정을 해야 한다
        int left = 1;
        // int right = houses[houses.length - 1] - 1;
        // 위와 같이 하면 안 된다
        // 위의 코드에 대한 반례
        // 2 2
        // 0
        // 2
        // 여기서
        // right 마지막 지점이 아니라 최대 거리가 되야 한다
        // 최대 거리는
        // houses 배열의 마지막 값에서
        // houses 배열의 첫번째 값을 뺀 값이다
        // houses 배열의 첫번째 값이 1이 아닐 수 있기 때문에
        // 1을 빼면 안 된다
        // 집의 최소 좌표가 0일 수 있는데 1을 빼면
        // 최대 거리를 제대로 구할 수 없다
        int right = houses[houses.length - 1] - houses[0];
        int maxDistance = 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (getInstallTotal(houses, mid) >= installNumber) {
                maxDistance = Math.max(maxDistance, mid);
                left = mid + 1;
            } else {
                // 설치가 안되면 거리를 줄여야 한다
                right = mid - 1;
            }
        }

        return maxDistance;
    }

    public int getInstallTotal(int[] houses, int distance) {
        // 첫번째 집은 무조건 설치
        int installTotal = 1;
        int prev = houses[0];

        for (int i = 1; i < houses.length; i++) {
            int cur = houses[i];

            if (cur - prev >= distance) {
                installTotal += 1;
                prev = cur;
            }
        }

        return installTotal;
    }
}
