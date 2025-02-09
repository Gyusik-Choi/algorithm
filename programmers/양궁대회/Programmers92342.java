package com.example;

public class Programmers92342_Fail {

    private int lionNumMax;

    private int[] lionNumMaxArr;

    public int[] solution(int n, int[] info) {
        lionNumMax = -1;
        lionNumMaxArr = new int[info.length];
        recursion(n, info, new int[info.length], 0);
        if (lionNumMax == -1) {
            return new int[]{-1};
        }
        return lionNumMaxArr;
    }

    private void recursion(int n, int[] apeach, int[] lion, int startIdx) {
        if (n < 0) {
            return;
        }

        if (n == 0) {
            compare(apeach, lion);
            return;
        }

        for (int i = startIdx; i < apeach.length; i++) {
            if (apeach[i] > 0) {
                lion[i] += apeach[i] + 1;
                recursion(n - lion[i], apeach, lion, i + 1);
                lion[i] -= apeach[i] + 1;
            } else {
                lion[i] += 1;
                recursion(n - 1, apeach, lion, i + 1);
                lion[i] -= 1;
            }
        }
    }

    private void compare(int[] apeach, int[] lion) {
        int apeachNum = 0;
        int lionNum = 0;
        for (int i = 0; i < apeach.length; i++) {
            if (apeach[i] >= lion[i]) {
                if (apeach[i] == 0 && lion[i] == 0) {
                    continue;
                }
                apeachNum += 10 - i;
            } else {
                lionNum += 10 - i;
            }
        }

        if (apeachNum >= lionNum) {
            return;
        }

        if (lionNum > lionNumMax) {
            lionNumMax = lionNum;
            System.arraycopy(lion, 0, lionNumMaxArr, 0, lion.length);
        } else if (lionNum == lionNumMax) {
            if (canUpdateLionNumMaxArr(lion)) {
                System.arraycopy(lion, 0, lionNumMaxArr, 0, lion.length);
            }
        }
    }

    private boolean canUpdateLionNumMaxArr(int[] lion) {
        for (int i = lion.length - 1; i > -1; i--) {
            if (lionNumMaxArr[i] > lion[i]) {
                return false;
            } else if (lionNumMaxArr[i] < lion[i]) {
                return true;
            }
        }
        return false;
    }
}
