package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_10872 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		System.out.println(factorial(N));
		
	}
	
	public static int factorial(int n) {
		if (n < 2) {
			return 1;
		} else if (n == 2) {
			return 2;
		} else {
			return n * factorial(n - 1);
		}
	}

}
