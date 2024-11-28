package com.example;

import java.util.*;

public class MergeIntervals56_3 {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        List<int[]> list = new ArrayList<>();
        for (int[] i : intervals) {
            if (!list.isEmpty() && list.get(list.size() - 1)[1] >= i[0]) {
                list.get(list.size() - 1)[1] = Math.max(list.get(list.size() - 1)[1], i[1]);
            } else {
                list.add(i);
            }
        }
        return list.toArray(new int[list.size()][]);
    }
}
