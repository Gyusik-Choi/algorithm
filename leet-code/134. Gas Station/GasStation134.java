package com.example.algorithm;

import java.util.Arrays;

public class GasStation134 {

    public int canCompleteCircuit(int[] gas, int[] cost) {
        if (Arrays.stream(gas).sum() < Arrays.stream(cost).sum()) return -1;
        int startIdx = 0, total = 0;
        for (int i = 0; i < gas.length; i++) {
            if (total + gas[i] < cost[i]) {
                startIdx = i + 1;
                total = 0;
            } else {
                total += gas[i] - cost[i];
            }
        }
        return startIdx;
    }
}
