package com.example;

import java.util.List;

public class SelectionSort {

    public List<Integer> selectionSort(List<Integer> list) {
        for (int i = 0; i < list.size() - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < list.size(); j++) {
                if (list.get(minIdx) > list.get(j)) minIdx = j;
            }
            if (minIdx != i) swap(list, i, minIdx);
        }
        return list;
    }

    private void swap(List<Integer> list, int i, int j) {
        int temp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, temp);
    }

    public int[] selectionSort(int[] list) {
        for (int i = 0; i < list.length - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < list.length; j++) {
                if (list[minIdx] > list[j]) minIdx = j;
            }
            if (minIdx != i) swap(list, i, minIdx);
        }
        return list;
    }

    private void swap(int[] list, int i, int j) {
        int temp = list[i];
        list[i] = list[j];
        list[j] = temp;
    }
}
