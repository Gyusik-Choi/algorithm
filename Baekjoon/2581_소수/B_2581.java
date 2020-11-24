package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_2581 {
	
	public static void main(String[] agrs) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int M = Integer.parseInt(br.readLine());
		int N = Integer.parseInt(br.readLine());
		int sums = 0;
		int prime_nums = 0;
		int min_prime = 10001;
		for (int i = M; i <= N; i++) {
			int p = prime(i);
			if (p == 1) {
				sums += i;
				prime_nums += 1;
				if (i < min_prime) {
					min_prime = i;
				}
			}
		}
		if (prime_nums > 0) {
			sb.append(sums);
			sb.append(" ");
			sb.append(min_prime);
			System.out.println(sb);
		} else {
			System.out.println(-1);
		}

	}
	
	public static int prime(int number) {
		if (number < 2) {
			return 0;
		} else {
			if (number == 2) {
				return 1;
			} else if (number % 2 == 0) {
				return 0;
			} else {
				int n = (int) Math.sqrt(number);
				for (int j = 3; j <= n; j += 2) {
					if (number % j == 0) {
						return 0;
					}
				}
				return 1;
			}
		}
	}

}
