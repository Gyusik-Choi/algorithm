import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b_10039 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// �հ� ������ ���� ����
		int sums = 0;
		// 5�� �ݺ��ϸ鼭 40�� �̸��� 40������ �ٲ㼭 sums�� ���ϰ�, 40�� �̻��� ���� ������� sums�� ���Ѵ�.
		for (int i = 0; i < 5; i++) {
			int point = Integer.parseInt(br.readLine());
			if (point < 40) {
				point = 40;
				sums += point;
			} else {
				sums += point;
			}
		}
		// sums�� 5�� ������ ����� ���Ѵ�.
		System.out.println(sums / 5);
		
	}
}
