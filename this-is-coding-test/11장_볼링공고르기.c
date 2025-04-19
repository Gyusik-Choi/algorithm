#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int combinations(int n, int limit, int idx, int cnt, int comb[], int balls[]);

int main(void) {
	int N, M;
	scanf("%d %d", &N, &M);
	
	int balls[1000];
	for (int i = 0; i < N; i++) {
		scanf("%d", &balls[i]);
	}

	int comb[2] = { -1, -1 };
	int answer = combinations(N, 0, 0, 0, comb, balls);
	printf("%d", answer);
	return 0;
}

int combinations(int n, int limit, int idx, int count, int comb[], int balls[]) {
	if (limit == 2) {
		return count + 1;
	}

	for (int i = idx; i < n; i++) {
		// 0�� �ε��� ���� 1�� �ε����� ���� �� ũ�鼭
		// �� �ε��� ������ ���� �������� ��ȣ�� ���� ���� ��츸 ��� ȣ��
		if (limit > 0 && (comb[limit - 1] >= i || balls[comb[limit - 1]] == balls[i])) {
			continue;
		}
		
		comb[limit] = i;
		count = combinations(n, limit + 1, i + 1, count, comb, balls);
		comb[limit] = -1;
	}
	return count;
}
