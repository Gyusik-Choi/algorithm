package com.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeIntervals56_4 {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
        List<int[]> result = new ArrayList<>();
        for (int[] interval : intervals) {
            if (result.isEmpty() || result.getLast()[1] < interval[0]) {
                result.add(interval);
                continue;
            }
            if (result.getLast()[1] < interval[1]) {
                result.getLast()[1] = interval[1];
            }
        }
        return result.toArray(new int[result.size()][]);
    }
}
