package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class b_8958 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			String quiz = br.readLine();
			int length = quiz.length();
			int sums = 0;
			int consecutive = 0;
			for (int j = 0; j < length; j++) {
				if (quiz.charAt(j) == 'O') {
					consecutive += 1;
					sums += consecutive;
				} else {
					consecutive = 0;
				}
			}
			System.out.println(sums);
		}
	
	}

}
