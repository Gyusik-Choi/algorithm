package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;

public class B_9020 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			int num = Integer.parseInt(br.readLine());
			if (num % 2 == 0) {
				int half_num = num / 2;
				if (prime(half_num) == 1) {
					System.out.println(Integer.toString(half_num) + ' ' + Integer.toString(half_num));
					continue;
				}
			}
			
			ArrayList<Integer> arr = new ArrayList<Integer>();
			for (int j = 2; j < num; j++) {
				int p = prime(j);
				if (p == 1) {
					arr.add(j);
				}
			}
			
			ArrayList<Integer> lst = new ArrayList<Integer>();
			for (int l = 0; l < arr.size() - 1; l++) {
				int n1 = arr.get(l);
				if (n1 + n1 == num) {
					lst.add(n1);
					lst.add(n1);
				}
				for (int m = l + 1; m < arr.size(); m++) {
					int n2 = arr.get(m);
					if (n1 + n2 == num) {
						lst.add(n1);
						lst.add(n2);
					}
				}
			}
			
			int min_dif = 10001;
			int min_num1 = 0;
			int min_num2 = 0;
			for (int o = 0; o < lst.size(); o += 2) {
				int n3 = lst.get(o);
				int n4 = lst.get(o + 1);
				if (Math.abs(n3 - n4) < min_dif) {
					min_dif = n4 - n3;
					min_num1 = n3;
					min_num2 = n4;
				}
			}
			System.out.println(Integer.toString(min_num1) + ' ' + Integer.toString(min_num2));
		}
	}
	
	public static int prime(int number) {
		if (number == 2) {
			return 1;
		} else if (number % 2 == 0) {
			return 0;
		} else {
			for (int k = 3; k < number; k += 2) {
				if (number % k == 0) {
					return 0;
				}
			}
			return 1;
		}
	}

}
