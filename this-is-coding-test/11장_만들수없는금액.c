#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
	return *(int*)a - *(int*)b;
}

int main(void) {
	int N;
	scanf("%d", &N);

	int* coins = (int*)malloc(N * sizeof(int));

	for (int i = 0; i < N; i++) {
		scanf_s("%d", &coins[i]);
	}

	qsort(coins, N, sizeof(int), compare);

	int acc = 0;

	for (int i = 0; i < N; i++) {
		if (acc + 1 < coins[i]) {
			break;
		}
		acc += coins[i];
	}

	free(coins);
	printf("%d", acc + 1);
	return 0;
}
