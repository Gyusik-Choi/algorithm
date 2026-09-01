package com.example;

import java.util.Arrays;

public class Programmers92342_2 {
    public int[] solution(int n, int[] info) {
        return searchMatchPoint(n, info, new int[info.length], 0, new Diff()).maxDiffArr;
    }

    private Diff searchMatchPoint(int n, int[] apeach, int[] lion, int cur, Diff d) {
        if (n == 0) {
            int diff = getDiff(apeach, lion);
            if (diff > d.maxDiff || (d.maxDiff > 0 && diff == d.maxDiff && d.containsLessLowerPointThan(lion))) {
                d.updateDiff(diff, Arrays.copyOf(lion, lion.length));
            }
            return d;
        }
        for (int i = cur; i < apeach.length; i++) {
            int point = Math.min(apeach[i] + 1, n);
            lion[i] = point;
            searchMatchPoint(n - point, apeach, lion, i + 1, d);
            lion[i] = 0;
        }
        return d;
    }

    private int getDiff(int[] apeach, int[] lion) {
        int apeachSum = 0;
        int lionSum = 0;
        for (int i = 0; i < apeach.length; i++) {
            if (apeach[i] == 0 && lion[i] == 0) continue;
            if (apeach[i] >= lion[i]) apeachSum += 10 - i;
            else lionSum += 10 - i;
        }
        return lionSum - apeachSum;
    }

    private static class Diff {
        int maxDiff = 0;
        int[] maxDiffArr = new int[]{-1};

        void updateDiff(int diff, int[] diffArr) {
            maxDiff = diff;
            maxDiffArr = diffArr;
        }

        boolean containsLessLowerPointThan(int[] lion) {
            for (int i = lion.length - 1; i > -1; i--) {
                if (lion[i] > maxDiffArr[i]) return true;
                if (lion[i] < maxDiffArr[i]) return false;
            }
            return false;
        }
    }
}
