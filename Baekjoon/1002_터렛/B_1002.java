package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class B_1002 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int[] arr = new int[6];
			for (int j = 0; j < 6; j++) {
				arr[j] = Integer.parseInt(st.nextToken());
			}
			int x1 = arr[0];
			int y1 = arr[1];
			int r1 = arr[2];
			int x2 = arr[3];
			int y2 = arr[4];
			int r2 = arr[5];

			int rplus_distance = (int) Math.pow(r2 + r1, 2);
			int rminus_distance = (int) Math.pow(r2 - r1, 2);
			int xy_distance = (int)(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
			
			if (x1 == x2 && y1 == y2 && r1 == r2) {
				System.out.println(-1);
				continue;
			} else if (rplus_distance < xy_distance) {
				System.out.println(0);
				continue;
			} else if (rminus_distance > xy_distance) {
				System.out.println(0);
				continue;
			} else if (rplus_distance  == xy_distance) {
				System.out.println(1);
				continue;
			} else if (rminus_distance == xy_distance) {
				System.out.println(1);
				continue;
			} else {
				System.out.println(2);
			}
		}
	}
}
