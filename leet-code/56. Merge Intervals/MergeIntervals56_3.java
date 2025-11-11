package com.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeIntervals56_3 {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (i1, i2) -> i1[0] != i2[0] ? i1[0] - i2[0] : i1[1] - i2[1]);
        List<int[]> queue = new ArrayList<>();
        Arrays.stream(intervals).forEach(i -> {
            if (queue.isEmpty()) {
                queue.add(i);
                return;
            }
            if (queue.get(queue.size() - 1)[1] == i[0]) {
                queue.get(queue.size() - 1)[1] = i[1];
                return;
            }
            if (queue.get(queue.size() - 1)[1] >= i[0]) {
                if (queue.get(queue.size() - 1)[1] < i[1]) {
                    queue.get(queue.size() - 1)[1] = i[1];
                }
                return;
            }
            queue.add(i);
        });
        return queue.toArray(new int[queue.size()][]);
    }
}
