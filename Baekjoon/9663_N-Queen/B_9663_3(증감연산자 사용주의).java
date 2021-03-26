package baekjoon_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class B_9663_3 {
	
	private static int N;
	
	private static int[] col;
	
	private static int[] diagonal1;
	
	private static int[] diagonal2;
	
	private static int cnt = 0;
	
	private static void nQueen(int y) {
		if (y == N) {
			cnt++;
			return;
		} else {
			for (int x = 0; x < N; x++) {
				if (col[x] == 0 && diagonal1[N - (y - x) - 1] == 0 && diagonal2[y + x] == 0) {
					col[x] = 1;
					diagonal1[N - (y - x) - 1] = 1;
					diagonal2[y + x] = 1;
//					nQueen(y++);
//					증감연산자 사용 주의할 것
//					https://m.blog.naver.com/PostView.nhn?blogId=tipsware&logNo=100168296597&proxyReferer=https:%2F%2Fwww.google.com%2F
					nQueen(y + 1);
					col[x] = 0;
					diagonal1[N - (y - x) - 1] = 0;
					diagonal2[y + x] = 0;
				}
			}
		}
		
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		col = new int[N];
		diagonal1 = new int[2 * N - 1];
		diagonal2 = new int[2 * N - 1];
		nQueen(0);
		System.out.println(cnt);
		
	}

}
