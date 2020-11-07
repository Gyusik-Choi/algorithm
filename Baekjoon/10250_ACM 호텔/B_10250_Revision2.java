package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class B_10250_Revision2 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int H = Integer.parseInt(st.nextToken());
			int W = Integer.parseInt(st.nextToken());
			int N = Integer.parseInt(st.nextToken());
			int f = 0;
			int r = 0;
			if (N % H == 0) {
				f += H * 100;
				r += N / H;
			} else {
				f += N % H * 100;
				r += N / H + 1;
			}
			System.out.println(f + r);
		}
	}

}
