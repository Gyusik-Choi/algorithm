package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_1157 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String word = br.readLine();
		int[] arr = new int[26];
		for (int i = 0; i < word.length(); i++) {
			char alpha = word.charAt(i);
			alpha = Character.toUpperCase(alpha);
			int ascii = (int)alpha - 65;
			arr[ascii] += 1;
		}
		int maxNum = -1;
		int idx = 0;
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] > maxNum) {
				maxNum = arr[i];
				idx = i;
			}
		}
		int maxNumCnt = 0;
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == maxNum) {
				maxNumCnt += 1;
			}
		}
		if (maxNumCnt > 1) {
			System.out.println('?');
		} else {
			idx += 65;
			char maxWord = (char)idx;
			System.out.println(maxWord);
		}
	}
}
