package com.example.sort;

import java.util.Arrays;
import java.util.List;

public class CountingSort {

    public List<Integer> countingSort(List<Integer> list) {
        int maxNum = getMaxNum(list);
        int[] count = new int[maxNum + 1];
        for (Integer i : list) count[i]++;
        for (int i = 0; i < count.length - 1; i++) count[i + 1] += count[i];
        int[] answer = new int[list.size()];
        for (Integer i : list) {
            count[i] -= 1;
            answer[count[i]] = i;
        }
        return Arrays.stream(answer).boxed().toList();
    }

    private int getMaxNum(List<Integer> list) {
        if (list.isEmpty()) throw new IllegalArgumentException();
        int maxNum = list.get(0);
        for (int i = 1; i < list.size(); i++) {
            if (maxNum < list.get(i)) maxNum = list.get(i);
        }
        return maxNum;
    }

    public int[] countingSort(int[] arr) {
        int[] count = new int[arr.length + 1];
        for (int i : arr) count[i]++;
        for (int i = 0; i < count.length - 1; i++) count[i + 1] += count[i];
        int[] answer = new int[arr.length];
        for (int i : arr) {
            count[i] -= 1;
            answer[count[i]] = i;
        }
        return answer;
    }
}
