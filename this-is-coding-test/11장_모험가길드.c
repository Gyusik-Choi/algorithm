#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
	return *(int*)a - *(int*)b;
}

int main(void) {
	int N;
	scanf_s("%d", &N);

	//int fears[N];
	int* fears = (int*)malloc(N * sizeof(int));
	if (fears == NULL) {
		return 1;
	}

	for (int i = 0; i < N; i++) {
		scanf_s("%d", &fears[i]);
	}

	// https://m.blog.naver.com/ygs1090/223105957292
	// 정렬할 값의 주소, 요소의 갯수, 요소의 크기, 기준 함수
	qsort(fears, N, sizeof(int), compare);

	int total = 0;
	int temp = 0;

	for (int i = 0; i < N; i++) {
		temp += 1;
		if (temp == fears[i]) {
			total += 1;
			temp = 0;
		}
	}

	free(fears);

	printf("%d", total);
	return 0;
}
