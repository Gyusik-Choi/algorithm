package com.example.sort;

import java.util.List;

public class ShellSort {
    /**
     * ciura sequence 대신 knuth sequence 를 사용했다.<br>
     * ciura sequence 는 고정된 값으로 sequence 가 구성되어 있는데<br>
     * knuth sequence 는 수식으로 sequence 를 구할 수 있어서 선택했다.<br>
     * 수식 => 3^k - 1 / 2 <br>
     * <a href=https://en.wikipedia.org/wiki/Shellsort>wikipedia</a><br>
     * <a href=https://oeis.org/A003462>oeis</a><br>
     * <a href=https://st-lab.tistory.com/209>tistory</a>
     */
    public List<Integer> shellSort(List<Integer> list) {
        int gapIdx = getGapIdx(list.size());
        while (gapIdx >= 0) {
            int gap = getGapFromIdx(gapIdx);
            insertionSortByGap(list, gap);
            gapIdx -= 1;
        }
        return list;
    }

    private int getGapIdx(int length) {
        int i = 1;
        int sequence = 1;
        while (sequence < length) {
            i += 1;
            sequence = ((int)Math.pow(3, i) - 1) / 2;
        }
        if (i > 1) i -= 1;
        return i;
    }

    private int getGapFromIdx(int gap) {
        return ((int)Math.pow(3, gap) - 1) / 2;
    }

    private void insertionSortByGap(List<Integer> list, int gap) {
        for (int i = 0; i < gap; i++) {
            for (int j = i + gap; j < list.size(); j += gap) {
                int idx = j;
                int num = list.get(idx);
                while (idx - gap >= 0 && list.get(idx - gap) > num) {
                    list.set(idx, list.get(idx - gap));
                    idx -= gap;
                }
                list.set(idx, num);
            }
        }
    }

    public List<Integer> shellSort2(List<Integer> list) {
        int gapIdx = getGapIdx(list.size());
        while (gapIdx > 0) {
            int gap = getGapFromIdx(gapIdx);
            insertionSortByGap2(list, gap);
            gapIdx -= 1;
        }
        return list;
    }

    private void insertionSortByGap2(List<Integer> list, int gap) {
        for (int i = gap; i < list.size(); i++) {
            for (int j = i; j >= gap; j -= gap) {
                if (list.get(j) > list.get(j - gap)) continue;
                swap(list, j, j - gap);
            }
        }
    }

    private void swap(List<Integer> list, int i, int j) {
        int temp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, temp);
    }
}

