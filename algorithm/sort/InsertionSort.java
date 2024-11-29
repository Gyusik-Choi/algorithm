package com.example.sort;

import java.util.List;

public class InsertionSort {

    public List<Integer> insertionSort(List<Integer> list) {
        for (int i = 1; i < list.size(); i++) {
            int idx = i;
            int num = list.get(idx);

            while (idx > 0 && list.get(idx - 1) > num) {
                list.set(idx, list.get(idx - 1));
                idx -= 1;
            }
            list.set(idx, num);
        }
        return list;
    }

    public int[] insertionSort(int[] list) {
        for (int i = 1; i < list.length; i++) {
            int idx = i;
            int num = list[idx];
            while (idx > 0 && list[idx - 1] > num) {
                list[idx] = list[idx - 1];
                idx -= 1;
            }
            list[idx] = num;
        }
        return list;
    }
}
