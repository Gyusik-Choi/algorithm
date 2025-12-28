package com.example;

import java.util.Arrays;

public class GasStation134_2 {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if (Arrays.stream(gas).sum() < Arrays.stream(cost).sum()) {
            return -1;
        }
        int size = gas.length;
        int[] sums = new int[size];
        for (int i = 0; i < size; i++) {
            sums[i] = gas[i] - cost[i];
        }
        int idx = 0;
        while (idx < size) {
            if (sums[idx] < 0) {
                idx += 1;
                continue;
            }
            // idx 에서 순회가 불가능한 인덱스 사이의 모든 인덱스는
            // idx 와 마찬가지로 순회가 불가능하다
            // 다만 현재 idx 부터 전체 범위를 보기 때문에
            // 반환받은 인덱스 값이 idx 보다 작은 값일 수 있다
            // 이 경우는 idx 다음부터 탐색을 하면 되고
            // 그렇지 않은 경우는 반환받은 인덱스의 다음 인덱스부터 탐색을 한다
            // 이때는 idx 의 바로 다음이 아니라
            // 불필요한 부분을 건너뛰고 탐색할 수 있다
            int circuit = checkCircuit(sums, idx);
            if (circuit == -1) {
                break;
            }
            if (circuit < idx) {
                idx += 1;
            } else {
                idx = circuit + 1;
            }
        }
        return idx;
    }

    // 순회가 가능한 경우
    // -1을 리턴
    // 순회가 불가능한 경우
    // 불가능한 인덱스를 반환한다
    private int checkCircuit(int[] sums, int idx) {
        int acc = sums[idx];
        int size = sums.length;
        for (int i = 1; i < size - 1; i++) {
            if (acc + sums[(idx + i) % size] < 0) {
                return (idx + i) % size;
            }
            acc += sums[(idx + i) % size];
        }
        return -1;
    }
}
