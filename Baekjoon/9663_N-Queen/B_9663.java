package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_9663 {
	
	private static int N;
	private static boolean[] vertical;
	private static boolean[] diagonal1;
	private static boolean[] diagonal2;
	private static int cnt = 0;
	
	private static void n_queen(int y) {
		if (y == N) {
			cnt++;
			return;
		} else {
			for (int x = 0; x < N; x++) {
				if (vertical[x] == false && diagonal1[N + x - y - 1] == false && diagonal2[x + y] == false) {
					vertical[x] = true; 
					diagonal1[N + x - y - 1] = true;
					diagonal2[x + y] = true;
					n_queen(y + 1);
					vertical[x] = false;
					diagonal1[N + x - y - 1] = false;
					diagonal2[x + y] = false;
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		vertical = new boolean[N];
		diagonal1 = new boolean[2 * N - 1];
		diagonal2 = new boolean[2 * N - 1];
		n_queen(0);
		System.out.println(cnt);
	}

}
