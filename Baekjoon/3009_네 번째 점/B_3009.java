package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class B_3009 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		ArrayList<Integer> arr1 = new ArrayList<>();
		ArrayList<Integer> arr2 = new ArrayList<>();
		for (int i = 0; i < 3; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 2; j++) {
				int num = Integer.parseInt(st.nextToken());
				if (j == 0) {
					int check = arr1.indexOf(num);
					if (check == -1) {
						arr1.add(num);
					} else {
						arr1.remove(check);
					}
				} else {
					int check = arr2.indexOf(num);
					if (check == -1) {
						arr2.add(num);
					} else {
						arr2.remove(check);
					}
				}
			}
		}
		String ans1 = Integer.toString(arr1.get(0));
		String ans2 = Integer.toString(arr2.get(0));
		System.out.println(ans1 + ' ' + ans2);
	}
}
