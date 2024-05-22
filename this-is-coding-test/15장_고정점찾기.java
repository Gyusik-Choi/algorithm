import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        System.out.println(main.solution());
    }

    public int solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] numbers = new int[N];

        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int idx = bisectLeft(numbers);

        // idx 가 0일 경우는 0번 인덱스가 답일 수도 있지만 그렇지 않을 수도 있다
        // 값이 없을 경우도 0이 나올 수 있어서 예외 처리를 한다
        // 그리고 idx 가 numbers 의 길이와 같은 경우도 값이 없는 경우다
        if ((idx == 0 && numbers[idx] != 0) || (idx == numbers.length)) {
            return -1;
        }

        return idx;
    }

    public int bisectLeft(int[] nums) {
        int left = 0;
        int right = nums.length;

        while (left < right) {
            int mid = (left + right) / 2;

            if (nums[mid] >= mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}
