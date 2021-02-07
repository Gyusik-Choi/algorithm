package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_2750 {
	
	private static int[] insertionSort(int[] lst) {
		
		for (int i = 1; i < lst.length; i++) {
			int toInsert = lst[i];
			int idx = i;
			while (idx > 0 && lst[idx - 1] > toInsert) {
				lst[idx] = lst[idx - 1]; 
				idx--;
			}
			lst[idx] = toInsert;
		}
		return lst;
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(br.readLine());
			arr[i] = num;
		}
		int[] ans = insertionSort(arr);
		for (int j = 0; j < ans.length; j++) {
			System.out.println(ans[j]);
		}
	}

}
