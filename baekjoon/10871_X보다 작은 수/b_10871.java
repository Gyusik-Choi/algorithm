import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class b_10871 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		// 첫번째 줄의 입력값 2개를 구분짓기 위해 StringTokenizer 사용
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		
		// 두번째 줄의 입력 값을 배열에 저장
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st2.nextToken());
		}
		br.close();
		
		for (int i = 0; i < N; i++) {
			if (arr[i] < X) {
				bw.write(arr[i] + " ");
			}
		}
		bw.flush();
		bw.close();
	}
}