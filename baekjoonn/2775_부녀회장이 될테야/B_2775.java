package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_2775 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			int k = 0;
			int n = 0;
			for (int j = 0; j < 2; j++) {
				if (j == 0) {
					k += Integer.parseInt(br.readLine());
				} else {
					n += Integer.parseInt(br.readLine());
				}
			}
			int[][] arr = new int[15][15];
			for (int o = 0; o < 15; o++) {
				arr[0][o] = o + 1;
				arr[o][0] = 1;
			}
			arr[14][0] = 1;
			for (int l = 1; l < 15; l++) {
				for (int m = 1; m < 15; m++) {
					arr[l][m] = arr[l - 1][m] + arr[l][m - 1];
				}
			}
			System.out.println(arr[k][n - 1]);
			System.out.println(arr[1][14]);
		}

		
	}
}
