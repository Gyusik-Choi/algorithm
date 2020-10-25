package baekjoon_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B_2941 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String croatianWord = br.readLine();
		
		String[] arr = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
		int num = 0;
		String word = "";
		int idx = 0;
		while (idx < croatianWord.length()) {
			char charWord = croatianWord.charAt(idx);
			word += charWord;
			if (idx < croatianWord.length() - 1) {
				if (croatianWord.charAt(idx + 1) == '=' || croatianWord.charAt(idx + 1) == '-') {
					num += 1;
					idx += 1;
					word = "";
				} else if (Arrays.stream(arr).anyMatch((word + croatianWord.charAt(idx + 1))::equals)) {
					num += 1;
					idx += 1;
					word = "";
				} else {
					if (idx < croatianWord.length() - 2) {
						
						if (Arrays.stream(arr).anyMatch((word + croatianWord.charAt(idx + 1) + croatianWord.charAt(idx + 2))::equals)) {
							num += 1;
							idx += 2;
							word = "";
						} else {
							num += 1;
							word = "";
						}
					}
					else {
						num += 1;
						word = "";
					}
				}
			} else {
				num += 1;
			}
		idx += 1;
		}
		System.out.println(num);
	}

}
