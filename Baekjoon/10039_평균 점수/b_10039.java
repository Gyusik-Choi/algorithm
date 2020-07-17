import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b_10039 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// 합계 저장할 정수 선언
		int sums = 0;
		// 5번 반복하면서 40점 미만은 40점으로 바꿔서 sums에 더하고, 40점 이상은 원래 점수대로 sums에 더한다.
		for (int i = 0; i < 5; i++) {
			int point = Integer.parseInt(br.readLine());
			if (point < 40) {
				point = 40;
				sums += point;
			} else {
				sums += point;
			}
		}
		// sums를 5로 나눠서 평균을 구한다.
		System.out.println(sums / 5);
		
	}
}
