package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_10870 {
	
	private static int n;
	
	private static int fibonacci(int num) {
		if (num == 0) {
			return 0;
		} else if (num < 3) {
			return 1;
		} else {
			return fibonacci(num - 1) + fibonacci(num - 2);
		}
	}

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		int ans = fibonacci(n);
		System.out.println(ans);
		
	}
}
