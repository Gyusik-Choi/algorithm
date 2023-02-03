package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.HashMap;

public class B_10870 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		HashMap <Integer, Integer> fib = new HashMap<>();
		fib.put(0, 0);
		fib.put(1, 1);
		fib.put(2, 1);
		int ans = fibonacci(fib, n);
		bw.write(String.valueOf(ans));
		bw.flush();
		bw.close();
	}

	public static int fibonacci(HashMap <Integer, Integer> fib, int number) {
		if (fib.containsKey(number)) {
			return fib.get(number);
		} else {
			fib.put(number, fibonacci(fib, number - 1) + fibonacci(fib, number - 2));
			return fib.get(number);
		}
	}

}
