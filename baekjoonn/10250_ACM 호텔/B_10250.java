package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class B_10250 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int H = Integer.parseInt(st.nextToken());
			int W = Integer.parseInt(st.nextToken());
			int N = Integer.parseInt(st.nextToken());
			if (H >= N) {
				String floor = Integer.toString(N);
				String room = Integer.toString(1);
				System.out.println(floor + "0" + room);
			} else {
				int f = N % H;
				int r = 0;
				String floor = "";
				String room = "";
				if (f == 0) {
					r += N / H;
					floor += Integer.toString(H);
					room += Integer.toString(r);
					if (r < 10) {
						System.out.println(floor + "0" + room);
					} else {
						System.out.println(floor + room);
					}
				} else {
					r += N / H + 1;
					floor += Integer.toString(f);
					room += Integer.toString(r);
					if (r < 10) {
						System.out.println(floor + "0" + room);
					} else {
						System.out.println(floor + room);
					}
				}
				
			}
			
		}
	}

}
