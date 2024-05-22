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

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st2.nextToken());
        }

        int left = bisectLeft(numbers, x);
        int right = bisectRight(numbers, x);
        System.out.println(right);
        int diff = right - left;

        return diff == 0 ? -1 : diff;
    }

    // 찾으려는 숫자가 위치한 인덱스
    // 찾으려는 숫자가 여러개인 경우 가장 첫번째 (왼쪽) 인덱스
    //
    // 찾으려는 숫자가 없는 경우
    // 1. nums 배열에 있는 숫자보다 작은 숫자를 찾는 경우
    //    0을 리턴
    // 2. nums 배열에 있는 숫자보다 큰 숫자를 찾는 경우
    //    nums 길이 값을 리턴
    //
    // 2번의 경우 right 값을 어떻게 하느냐에 따라 달라질 수 있다
    // right 를 만약에 nums.length - 1 로 한다면
    // 찾으려는 숫자가 nums 배열에 있는 숫자보다 큰 경우
    // nums.length - 1 이 리턴된다
    // 이 경우 해당 인덱스의 값이 찾으려는 숫자인지를 한번 더 검증해야 한다
    // 왜냐면 찾으려는 숫자가 정말로 그 인덱스에 있는 경우도
    // nums.length - 1이 리턴될 수 있기 때문이다
    public int bisectLeft(int[] nums, int target) {
        int left = 0;
        int right = nums.length;

        while (left < right) {
            int mid = (left + right) / 2;

            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    // 찾으려는 숫자가 위치한 인덱스의 한칸 뒤 인덱스
    // 찾으려는 숫자가 여러개인 경우 해당 숫자가 위치한 마지막 인덱스의 한칸 뒤 인덱스
    //
    // 1. nums 배열에 있는 숫자보다 작은 숫자를 찾는 경우
    //    0을 리턴
    // 2. nums 배열에 있는 숫자보다 큰 숫자를 찾는 경우
    //    nums 길이 값을 리턴
    //
    // 한 가지 주의할점은
    // 리턴된 값이 nums.length 일 경우
    // 찾는 값이 있어서 나올 수도 있고 찾는 값이 없어서 나올 수도 있다
    // 무슨 말이냐면
    // 7 3
    // 1 1 2 2 2 2 3
    // 위와 같은 입력이 주어지면 7이 리턴된다
    // 7 4
    // 1 1 2 2 2 2 3
    // 위와 같은 입력이 주어져도 7이 리턴된다
    public int bisectRight(int[] nums, int target) {
        int left = 0;
        int right = nums.length;

        while (left < right) {
            int mid = (left + right) / 2;

            if (nums[mid] > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}
