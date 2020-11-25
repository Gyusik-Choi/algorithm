package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class B_1085 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[4];
		int i = 0;
		while (st.hasMoreTokens()) {
			int n = Integer.parseInt(st.nextToken());
			arr[i] = n;
			i++;
		}
		int minus = 1000;
		for (int j = 0; j < 2; j++) {
			int minus1 = arr[j];
			int minus2 = arr[j + 2] - arr[j];
			int minus3 = Math.min(minus1, minus2);
			minus = Math.min(minus, minus3);
		}
		System.out.println(minus);
	}
}
