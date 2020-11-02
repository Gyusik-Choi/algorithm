package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_2292 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int start = 1;
		for (int i = 0; i < N; i++) {
			start += 6 * i;
			if (start == N) {
				System.out.println(i + 1);
				return;
			} else if (start > N) {
				System.out.println(i + 1);
				return;
			}
		}
	}
}
