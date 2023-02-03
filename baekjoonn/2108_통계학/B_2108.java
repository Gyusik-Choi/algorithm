package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
//import java.util.Arrays;

public class B_2108 {

	private static int[] common = new int[8001];

	private static int average(int[] lst) {
		int sums = 0;
		for (int j = 0; j < lst.length; j++) {
			sums += lst[j];
		}
		int avg = (int)Math.round((double)sums / lst.length);
		return avg;
	}

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		int maxNum = -4001;
		int minNum = 4001;
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(br.readLine());
			arr[i] = num;
			common[num + 4000]++;
			if (maxNum < num) {
				maxNum = num;
			}
			
			if (minNum > num) {
				minNum = num;
			}
		}
		
		// Æò±Õ
		System.out.println(average(arr));
		
		// Áß¾Ó°ª
		int median = -4001;
		int cnt = 0;
		
		// ÃÖºó°ª
		int commonNum = 0;
		int commonCnt = 0;
		int check = 0;
		
		for (int j = minNum + 4000; j <= maxNum + 4000; j++) {
			if (common[j] > 0) {
				if (cnt < (N + 1) / 2) {
					cnt += common[j];
					median = j - 4000;
				}
				
				if (commonCnt < common[j]) {
					commonCnt = common[j];
					commonNum = j - 4000;
					check = 0;
				} else if (commonCnt == common[j] && check == 0) {
					commonNum = j - 4000;
					check = 1;
					
				}
			}
		}
		System.out.println(median);
		System.out.println(commonNum);
		// ¹üÀ§
		System.out.println(maxNum - minNum);
		
	}
}
