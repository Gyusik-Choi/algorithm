package com.example;

import java.util.Arrays;

public class Programmers92342_2 {

    private int maxScoreGap;
    private int[] lionMaxArr;

    public int[] solution(int n, int[] info) {
        maxScoreGap = -1;
        lionMaxArr = new int[info.length];
        recursion(n, info, new int[info.length], 0);
        return maxScoreGap == -1 ? new int[]{-1} : lionMaxArr;
    }

    private void recursion(int n, int[] apeach, int[] lion, int idx) {
        if (apeach.length == idx) {
            lion[idx - 1] = n;
            compare(apeach, lion);
            return;
        }

        if (apeach[idx] < n) {
            lion[idx] = apeach[idx] + 1;
            recursion(n - lion[idx], apeach, lion, idx + 1);
            lion[idx] = 0;
        }
        recursion(n, apeach, lion, idx + 1);
    }

    private void compare(int[] apeach, int[] lion) {
        int apeachScore = 0, lionScore = 0;
        for (int i = 0; i < apeach.length; i++) {
            if (apeach[i] == 0 && lion[i] == 0) continue;
            if (apeach[i] >= lion[i]) apeachScore += 10 - i;
            else lionScore += 10 - i;
        }

        if (apeachScore >= lionScore) return;

        int scoreGap = lionScore - apeachScore;
        if (maxScoreGap < scoreGap) {
            maxScoreGap = scoreGap;
            lionMaxArr = Arrays.copyOf(lion, lion.length);
        } else if (maxScoreGap == scoreGap) {
            if (canUpdateLionNumMaxArr(lion)) lionMaxArr = Arrays.copyOf(lion, lion.length);
        }
    }

    private boolean canUpdateLionNumMaxArr(int[] lion) {
        for (int i = lion.length - 1; i > -1; i--) {
            if (lionMaxArr[i] > lion[i]) return false;
            if (lionMaxArr[i] < lion[i]) return true;
        }
        return false;
    }
}
