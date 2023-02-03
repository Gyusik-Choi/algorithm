package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_5622 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String phoneAlpha = br.readLine();
		int[] arr = new int[26];
		int sec = 0;
		int second = 3;
		while (sec < 25) {
			// PQRS, WXYZ의 경우
			if (sec == 15 || sec == 22) {
				for (int j = 0; j < 4; j++) {
					arr[sec] = second;
					sec += 1;
				}
				second += 1;
			// 그 외의 경우
			} else {
				for (int j = 0; j < 3; j++) {
					arr[sec] = second;
				}
				second += 1;
			}
		}
		int ans = 0;
		for (int k = 0; k < phoneAlpha.length(); k++) {
			char alpha = phoneAlpha.charAt(k);
			int ascii = (int)alpha - 65;
			ans += arr[ascii];
		}
		System.out.println(ans);
	}

}
