import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b_5543 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int burger = 2001;
		int beverage = 2001;
		for (int i = 0; i < 5; i++) {
			if (i < 3) {
				int hamburger = Integer.parseInt(br.readLine());
				if (hamburger < burger) {
					burger = hamburger;
				}
			} else {
				int drink = Integer.parseInt(br.readLine());
				if (drink < beverage) {
					beverage = drink;
				}
			}
		}
		System.out.println(burger + beverage - 50);
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		int[] arr = new int[5];
//		int sums = 1000000;
//		for (int i = 0; i < 5; i++) {
//			int menu = Integer.parseInt(br.readLine());
//			arr[i] = menu;
//		}
//		br.close();
//		for (int i = 0; i < 3; i++) {
//			for (int j = 3; j < 5; j++) {
//				int set = arr[i] + arr[j] - 50;
//				if (sums > set) {
//					sums = set;
//				}
//			}
//		}
//		System.out.println(sums);
}
}