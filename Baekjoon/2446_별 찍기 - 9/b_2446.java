import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class b_2446 {
	
	public static void main(String[] args) throws IOException {
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		br.close();
		for (int i = N - 1; i > -1; i--) {
			for (int j = 0; j < N + N - 1; j++) {
				if ((2 * N - 1) / 2 - i <= j && j < N + i) {
					bw.write('*');
				} else if (j < (2 * N - 1) / 2 - i) {
					bw.write(' ');
				}
			}
			bw.newLine();
		}
		for (int i = 1; i < N; i++) {
			for (int j = 0; j < N + N - 1; j++) {
				if ((N + N - 1)/2 - i <= j && j < (N + N)/2 + i) {
					bw.write('*');
				} else if (j < (2 * N - 1) / 2 - i){
					bw.write(' ');
				}
			}
			bw.newLine();
		}
	bw.flush();
	bw.close();
	}	
}
