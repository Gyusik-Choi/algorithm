package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;

public class B_9020_2 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		boolean[] arr = new boolean[10001];
		for (int i = 2; i <= 10000; i++) {
			arr[i] = true;
		}
		for (int i = 2; i * i <= 10000; i++) {
			if (arr[i]) {
				for (int j = 2 * i; j <= 10000; j += i) {
					arr[j] = false;
				}
			}
		}
		for (int k = 0; k < T; k++) {
			int num = Integer.parseInt(br.readLine());
			int num_half = num / 2;
			for (int l = num_half; 2 <= l; l--) {
				if (arr[l] == true && arr[num-l] == true) {
					System.out.println(Integer.toString(l) + ' ' + Integer.toString(num - l));
					break;
				}
			}
		}
	}

}
