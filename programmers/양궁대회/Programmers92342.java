package com.example;

import java.util.Arrays;

public class Programmers92342_2 {

    private int lionMax;

    private int[] lionMaxArr;

    public int[] solution(int n, int[] info) {
        lionMax = -1;
        lionMaxArr = new int[info.length];
        recursion(n, info, new int[info.length], 0);
        return lionMax == -1 ? new int[]{-1} : lionMaxArr;
    }

    private void recursion(int n, int[] apeach, int[] lion, int idx) {
        if (apeach.length - 1 == idx) {
//            if (n > 0) {
//                lion[idx] = n;
//            }
//            n 가 남았을 수 있다
//            그러나 위와 같이
//            n > 0 인 경우만 마지막 인덱스에 n 을 할당하면 안 된다
//            재귀로 호출되기 때문에
//            recursion(n - lion[idx], apeach, lion, idx + 1);
//            여기서 n > 0 이면 마지막 인덱스에 n 을 할당하게 된다
//            lion[idx] = 0; 이후에
//            recursion(n, apeach, lion, idx + 1);
//            여기서 n = 0 이면 마지막 인덱스에 n 을 할당하지 않으면서
//            마지막 인덱스가 0으로 초기되지 못한다
            lion[idx] = n;
//             점수 비교
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

        if (lionNum > lionMax) {
            lionMax = lionNum;
            System.arraycopy(lion, 0, lionMaxArr, 0, lion.length);
        } else if (lionNum == lionMax) {
            if (canUpdateLionNumMaxArr(lion)) {
                System.arraycopy(lion, 0, lionMaxArr, 0, lion.length);
            }
        }
    }

    private boolean canUpdateLionNumMaxArr(int[] lion) {
        for (int i = lion.length - 1; i > -1; i--) {
            if (lionMaxArr[i] > lion[i]) {
                return false;
            } else if (lionMaxArr[i] < lion[i]) {
                return true;
            }
        }
        return false;
    }
}
