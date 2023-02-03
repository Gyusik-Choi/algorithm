package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Comparator;

public class B_11650 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N][2];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr, new Comparator<int[]>() {
			@Override
			public int compare(int[] a1, int[] a2) {
				if (a1[0] == a2[0]) {
					return a1[1] - a2[1];
				} else {
					return a1[0] - a2[0];
				}
			}
			
		});
		
		StringBuilder sb = new StringBuilder();
		for (int j = 0; j < arr.length; j++) {
			sb.append(arr[j][0] + " " + arr[j][1] + "\n");
		}
		System.out.println(sb);
	}

}

// Âü°í
// https://st-lab.tistory.com/110
// https://seeminglyjs.tistory.com/164
