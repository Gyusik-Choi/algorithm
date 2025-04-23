#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int compare(const void* a, const void* b) {
	return strcmp((char *)a, (char *)b);
}

int main(void) {
	char input[10001];
	scanf("%s", input);

	int length = strlen(input);

	int sums = 0;
	for (int i = 0; i < length; i++) {
		if (48 <= input[i] && input[i] <= 57) {
			sums += input[i] - '0';
		}
	}

	char str[10001];
	int idx = 0;
	for (int i = 0; i < length; i++) {
		if (input[i] > 57) {
			str[idx] = input[i];
			idx += 1;
		}
	}
	// 마지막에 null terminator 지정
	str[idx] = '\0';

	qsort(str, idx, sizeof(str[0]), compare);

	printf("%s%d\n", str, sums);
	return 0;
}
