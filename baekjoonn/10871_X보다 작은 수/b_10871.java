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
		
		// ù��° ���� �Է°� 2���� �������� ���� StringTokenizer ���
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		
		// �ι�° ���� �Է� ���� �迭�� ����
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