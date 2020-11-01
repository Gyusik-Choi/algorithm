package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_2839 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int N2 = N;
		if (N < 5) {
			if (N == 4) {
				System.out.println(-1);
				return;
			} else {
				System.out.println(1);
				return;
			}
		}
		if (N % 5 == 0) {
			System.out.println(N / 5);
			return;
		} else {
			int quotient = N / 5;
			int quotient2 = quotient;
			for (int i = 0; i < quotient2; i++) {
				N = 5 * quotient;
				if ((N2 - N) % 3 == 0) {
					System.out.println(quotient + ((N2 - N) / 3));
					return;
				}
				quotient -= 1;
			}
			if (N2 % 3 == 0) {
				System.out.println(N2 / 3);
				return;
			} else {
				System.out.println(-1);
				return;
			}
		}
		
	}

}
