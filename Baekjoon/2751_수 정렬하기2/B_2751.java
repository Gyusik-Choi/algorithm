package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class B_2751 {
	
	private static int[] arr;
	
	private static void merge(int low, int mid, int high) {
		int[] temp = new int[high - low];
		int t = 0;
		int l = low;
		int m = mid;
		
		while (l < mid && m < high) {
			if (arr[l] < arr[m]) {
				temp[t] = arr[l];
				t++;
				l++;
			} else {
				temp[t] = arr[m];
				t++;
				m++;
			}
		}
		
		while (l < mid) {
			temp[t] = arr[l];
			t++;
			l++;
		}
		
		while (m < high) {
			temp[t] = arr[m];
			t++;
			m++;
		}
		
		for (int i = low; i < high; i++) {
			arr[i] = temp[i - low];
		}
	}
	
	private static void sort(int low, int high) {
		if (high - low < 2) {
			return;
		}
		int mid = (low + high) / 2;
		sort(low, mid);
		sort(mid, high);
		merge(low, mid, high);
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		arr = new int[N];
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(br.readLine());
			arr[i] = num;
		}
		
		sort(0, N);
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int j = 0; j < N; j++) {
			bw.write(String.valueOf(arr[j]) + '\n');
		}
		bw.flush();
		bw.close();
	}

}
