package com.example;

import java.util.Arrays;

public class ShellSort2 {
    // 첫번째 인덱스를 구한뒤 인덱스를 줄여가면서 gap 을 구한다
    // gap 은 정해져 있고 gap 목록에서 시작점을 구한뒤
    // gap 목록의 첫번째 인덱스까지 인덱스를 줄여가면서 정렬한다
    // gap 은 knuth sequence 를 이용했다
    public int[] sort(int[] arr) {
        int[] copiedArr = Arrays.copyOf(arr, arr.length);
        int gapIdx = getGapMaxIdx(copiedArr.length);
        while (gapIdx > 0) {
            int gap = getGapFromIdx(gapIdx);
            insertionSortWithGap(copiedArr, gap);
            gapIdx -= 1;
        }
        return copiedArr;
    }

    private int getGapMaxIdx(int length) {
        int idx = 0;
        while (getGapFromIdx(idx + 1) < length) {
            idx += 1;
        }
        return idx;
    }

    private int getGapFromIdx(int idx) {
        return ((int) Math.pow(3, idx) - 1) / 2;
    }

    private void insertionSortWithGap(int[] arr, int gap) {
        for (int i = gap; i < arr.length; i += gap) {
            int idx = i;
            int num = arr[i];
            while (idx - gap >= 0 && arr[idx - gap] > num) {
                arr[idx] = arr[idx - gap];
                idx -= gap;
            }
            arr[idx] = num;
        }
    }
}
