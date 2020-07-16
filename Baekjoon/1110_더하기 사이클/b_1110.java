import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class b_1110 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		br.close();
		int A = N;
		int cnt = 0;
		while (true) {
			N = (N % 10 * 10) + (N / 10 + N % 10) % 10;
			cnt++;
			if (N == A) {
				System.out.println(cnt);
				break;
			}
		}
	}
}