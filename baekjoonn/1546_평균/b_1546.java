package baekjoon_java;

import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b_1546 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		double sums = 0.0;
		int max = 0;
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		for (int i = 0; i < N; i++) {
			int grade = Integer.parseInt(st.nextToken());
			if (grade > max) {
				max = grade;
			}
			sums += grade;
		}
		System.out.println(((sums/max) * 100) / N);
	}
}
