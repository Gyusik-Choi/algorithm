#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	char str[1000001];

	scanf("%s", str);

	int zero_cnt = 0;
	int one_cnt = 0;

	if (str[0] == '0') {
		zero_cnt += 1;
	}
	else {
		one_cnt += 1;
	}

	for (int i = 1; str[i] != '\0'; i++) {
		if (str[i - 1] != str[i]) {
			if (str[i] == '0') {
				zero_cnt += 1;
			}
			else {
				one_cnt += 1;
			}
		}
	}

	printf("%d", min(zero_cnt, one_cnt));
	return 0;
}

int min(int a, int b) {
	return a <= b ? a : b;
}
