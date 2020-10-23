package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class B_2908 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[2];
		for (int i = 0; i < arr.length; i++) {
			String nums = st.nextToken();
			StringBuffer sb = new StringBuffer();
			sb.append(nums);
			int changeIntNum = Integer.parseInt(sb.reverse().toString());
			arr[i] = changeIntNum;
		}
		if (arr[0] > arr[1]) {
			System.out.println(arr[0]);
		} else {
			System.out.println(arr[1]);
		}
	}
}
