#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	char input[9];
	scanf("%s", input);

	int length = strlen(input);
	
	int sum1 = 0;
	int sum2 = 0;

	for (int i = 0; i < length / 2; i++) {
		sum1 += input[i] - '0';
	}

	for (int i = length / 2; i < length; i++) {
		sum2 += input[i] - '0';
	}

	printf("%s", sum1 == sum2 ? "LUCKY" : "READY");
	return 0;
}
