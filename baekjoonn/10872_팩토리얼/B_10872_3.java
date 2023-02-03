package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashMap;

public class B_10872_3 {
	
	// 문제에서는 N이 12까지라 value로 int를 해도 되지만 20 이상은 value가 int범위 초과라 음수로 나오기 때문에 이를 처리하려면 Long으로 해야 한다.
	private static HashMap <Integer, Long> fac = new HashMap<>();
	
	private static Long factorial(int n) {
		if (fac.containsKey(n)) {
			return fac.get(n);
		} else {
			fac.put(n, (long) n * factorial(n - 1));
			return fac.get(n);
		}
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		fac.put(0, (long) 1);
		fac.put(1, (long) 1);
		fac.put(2, (long) 2);
		Long ans = factorial(N);
		System.out.println(ans);
		
	}
}
