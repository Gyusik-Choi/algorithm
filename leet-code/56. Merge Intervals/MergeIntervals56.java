package com.example;

import java.util.ArrayDeque;
import java.util.Deque;

public class MergeIntervals56 {
    public int[][] merge(int[][] intervals) {
        int[][] sortedIntervals = sortIntervals(intervals);
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(sortedIntervals[0]);
        for (int i = 1; i < sortedIntervals.length; i++) {
            int[] prev = stack.pop();
            int[] cur = sortedIntervals[i];
            if (prev[1] >= cur[0]) {
                stack.push(new int[]{prev[0], Math.max(prev[1], cur[1])});
            } else {
                stack.push(prev);
                stack.push(cur);
            }
        }

        int[][] answer = new int[stack.size()][2];
        int idx = 0;
        while (!stack.isEmpty()) answer[idx++] = stack.pollLast();
        return answer;
    }

    private int[][] sortIntervals(int[][] intervals) {
        return sortArray(intervals, 0, intervals.length - 1);
    }

    private int[][] sortArray(int[][] intervals, int low, int high) {
        if (low >= high) return intervals;
        int mid = (low + high) / 2;
        sortArray(intervals, low, mid);
        sortArray(intervals, mid + 1, high);

        int[][] temp = new int[high - low + 1][2];
        int l = low, h = mid + 1, idx = 0;
        while (l <= mid && h <= high) {
            if (intervals[l][0] <= intervals[h][0]) {
                temp[idx][0] = intervals[l][0];
                temp[idx][1] = intervals[l][1];
                l += 1;
            } else {
                temp[idx][0] = intervals[h][0];
                temp[idx][1] = intervals[h][1];
                h += 1;
            }
            idx += 1;
        }

        while (l <= mid) {
            temp[idx][0] = intervals[l][0];
            temp[idx][1] = intervals[l][1];
            l += 1;
            idx += 1;
        }

        while (h <= high) {
            temp[idx][0] = intervals[h][0];
            temp[idx][1] = intervals[h][1];
            h += 1;
            idx += 1;
        }

        for (int i = 0; i < temp.length; i++) {
            intervals[low + i][0] = temp[i][0];
            intervals[low + i][1] = temp[i][1];
        }
        return intervals;
    }
}
