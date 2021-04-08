package baekjoon_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class B_1427 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String N = br.readLine();
		String[] arr = N.split("");
		int[] newArr = new int[arr.length];
		for (int i = 0; i < arr.length; i++) {
			newArr[i] = Integer.parseInt(arr[i]);
		}
		// 새로운 배열 리턴하지 않고 기존 배열을 변화시킨다
		Arrays.sort(newArr);
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int k = newArr.length - 1; k >= 0; k--) {
			String num = String.valueOf(newArr[k]);
			bw.write(num);
		}
		bw.flush();
		bw.close();
		
	}
}
