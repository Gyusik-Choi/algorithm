package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class B_2580_2 {
	
	private static void sudoku(int index) {
		if (index == empty_arr.size()) {
			for (int k = 0; k < 9; k++) {
				for (int l = 0; l < 9; l++) {
					System.out.print(arr[k][l] + " ");
				}
				System.out.println();
			}
			System.exit(0);

		} else {
			int y = empty_arr.get(index)[0];
			int x = empty_arr.get(index)[1];
			int ay = y / 3 * 3;
			int ax = x / 3 * 3;
			int[] possible_nums = new int[10];
			for (int m = 1; m < 10; m++) {
				possible_nums[m] = 1;
			}
			
			// 가로검사
			for (int n = 0; n < 9; n++) {
				int row_num = arr[y][n];
				possible_nums[row_num] = 0;
			}
			
			// 세로검사
			for (int o = 0; o < 9; o++) {
				int col_num = arr[o][x];
				possible_nums[col_num] = 0;
			}
			
			// 3 x 3 검사
			for (int p = ay; p < ay + 3; p++) {
				for (int q = ax; q < ax + 3; q++) {
					int square_num = arr[p][q];
					possible_nums[square_num] = 0;
				}
			}
			
			// 후보 숫자 추출
			ArrayList<Integer> candidate = new ArrayList<>();
			for (int r = 1; r < 10; r++) {
				if (possible_nums[r] == 1) {
					candidate.add(r);
				}
			}
			
			// 추출한 숫자들로 백트래킹 실행
			for (int s = 0; s < candidate.size(); s++) {
				int candidate_num = candidate.get(s);
				arr[y][x] = candidate_num;
				sudoku(index + 1);
				arr[y][x] = 0;
			}
		}
	}
	
	private static ArrayList<int[]> empty_arr = new ArrayList<int[]>();
	
	private static int[][] arr = new int[9][9];
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int i = 0; i < 9; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 9; j++) {
				int num = Integer.parseInt(st.nextToken());
				arr[i][j] = num;
				if (num == 0) {
					int[] small_arr = new int[2];
					small_arr[0] = i;
					small_arr[1] = j;
					empty_arr.add(small_arr);
				}
			}
		}
		sudoku(0);
	}
	
}
