package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class B_2447 {
	
	private static int N;
	private static String[][] stars; 
	
	private static void make_star(int n, int y, int x) {
		if (n == 1) {
			stars[y][x] = "*";
			return;
		} else {
			n = n / 3;
			for (int k = 0; k < 3; k++) {
				for (int l = 0; l < 3; l++) {
					if (k == 1 && l == 1) {
						continue;
					} else {
						make_star(n, n * k + y, n * l + x);
					}
				}
			}
		}
		return;
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		stars = new String[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				stars[i][j] = " ";
			}
		}
		make_star(N, 0, 0);
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int m = 0; m < N; m++) {
			for (int n = 0; n < N; n++) {
				bw.write(stars[m][n]);
			}
			bw.newLine();
		}
		bw.flush();
		bw.close();
	}

}
