package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashMap;

public class B_10872_another {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		HashMap <Integer, Integer> fac = new HashMap<>();
		System.out.println(factorial(fac, N));
	
	}
	
	public static int factorial(HashMap<Integer, Integer> fac, int n) {
		if (n < 2) {
			return 1;
		} else if (n == 2) {
			return 2;
		} else {
			if (fac.containsKey(n)) {
				return fac.get(n);
			} else {
				fac.put(n, n * factorial(fac, n - 1));
				return n * factorial(fac, n - 1);
			}
		}
	}

}
