package baekjoon_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_15649 {
	
	private static int N;
	
	private static int M;
	
	private static int[] check;
	
	private static int[] arr;
	
	private static void permutation(int idx) {
		if (idx == M) {
			for (int i = 0; i < M; i++) {
				System.out.print(arr[i] + " ");
			}
			System.out.println();
		} else {
			for (int i = 0; i < N; i++) {
				if (check[i] == 0) {
					check[i] = 1;
					arr[idx] = i + 1;
					permutation(idx + 1);
					check[i] = 0;
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		check = new int[N];
		arr = new int[N];
		permutation(0);
	}

}
