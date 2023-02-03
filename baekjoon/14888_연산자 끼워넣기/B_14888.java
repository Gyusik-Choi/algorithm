package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class B_14888 {
	
	private static int N;
	
	private static int[] nums;
	
	// 연산자별 갯수
	private static int[] operators;
	
	// operators에서 연산자별 갯수에 맞춰 연산자를 정리한 배열
	private static String[] newOperators;
	
	private static long maxSum = -10000000000L;
	
	private static long minSum = 10000000000L;
	
	// 연산자 순열
	private static String[] temp;
	
	// 중복돼서 temp 배열에 담기지 않도록 해당하는 인덱스의 newOperators값이 temp에 포함됐는지 여부
	private static int[] check;
	
	private static void permutation(int idx) {
		if (idx == N - 1) {
			
			int tempSum = nums[0];
			for (int j = 0; j < N - 1; j++) {
				if (temp[j] == "+") {
					tempSum += nums[j + 1];
				} else if (temp[j] == "-") {
					tempSum -= nums[j + 1];
				} else if (temp[j] == "*") {
					tempSum *= nums[j + 1];
				} else {
					if (tempSum < 0) {
						tempSum *= -1;
						tempSum /= nums[j + 1];
						tempSum *= -1;
					} else {
						tempSum /= nums[j + 1];
					}
				}
			}
			if (tempSum > maxSum) {
				maxSum = tempSum;
			}
			
			if (tempSum < minSum) {
				minSum = tempSum;
			}
		} else {
			for (int i = 0; i < N - 1; i++) {
				if (check[i] == 0) {
					check[i] = 1;
					temp[idx] = newOperators[i];
					permutation(idx + 1);
					check[i] = 0;
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		nums = new int[N];
		operators = new int[4];
		StringTokenizer st; 
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(st.nextToken());
			nums[i] = num;
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 4; i++) {
			int operator = Integer.parseInt(st.nextToken());
			operators[i] = operator;
		}
		newOperators = new String[N - 1];
		int idx = 0;
		for (int i = 0; i < 4; i++) {
			int operatorNum = operators[i];		
			for (int j = 0; j < operatorNum; j++) {
				if (i == 0) {
					newOperators[idx] = "+";
					idx++;
				} else if (i == 1) {
					newOperators[idx] = "-";
					idx++;
				} else if (i == 2) {
					newOperators[idx] = "*";
					idx++;
				} else {
					newOperators[idx] = "/";
					idx++;
				}
			}
		}
		
		temp = new String[N - 1];
		check = new int[N - 1];
		permutation(0);
		System.out.println(maxSum);
		System.out.println(minSum);
		
	}

}
