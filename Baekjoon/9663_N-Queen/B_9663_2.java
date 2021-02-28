package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_9663_2 {
	
	private static int cnt;
	
	private static int N;
	
	private static int[] vertical;
	
	private static boolean check(int y) {
		for (int beforeY = 0; beforeY < y; beforeY++) {
			if (vertical[beforeY] == vertical[y]) {
				return false;
			}
			
			if (Math.abs(vertical[beforeY] - vertical[y]) == y - beforeY) {
				return false;
			}
		}
		return true;
	}
	
	private static void nQueen(int y) {
		if (y == N) {
			cnt++;
		} else {
			for (int i = 0; i < n; i++) {
				vertical[y] = i;
				if (check(y)) {
					nQueen(y + 1);
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		vertical = new int[N];
		nQueen(0);
		System.out.println(cnt);
	}
}

