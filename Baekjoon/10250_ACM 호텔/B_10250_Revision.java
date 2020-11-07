package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class B_10250_Revision {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int H = Integer.parseInt(st.nextToken());
			int W = Integer.parseInt(st.nextToken());
			int N = Integer.parseInt(st.nextToken());
			String floor = "";
			String room = "";
			int r = 0;
			if (N % H == 0) {
				r += N / H;
				floor += Integer.toString(H);
				if (r == 0) {
					room += "01";
				} else if (r < 10) {
					room += "0" + Integer.toString(r);
				} else {
					room += Integer.toString(r);
				}
			} else {
				r += N / H + 1;
				int f = N % H;
				floor += Integer.toString(f);
				if (r == 0) {
					room += "01";
				} else if (r < 10) {
					room += "0" + Integer.toString(r);
				} else {
					room += Integer.toString(r);
				}
			}
			System.out.println(floor + room);
		}
	}

}
