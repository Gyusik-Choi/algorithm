package com.example;

import java.util.List;

public class BubbleSort {

    public List<Integer> bubbleSort(List<Integer> list) {
        for (int i = 1; i < list.size(); i++) {
            boolean swapped = false;
            for (int j = 0; j < list.size() - i; j++) {
                if (list.get(j) > list.get(j + 1)) {
                    swap(list, j, j + 1);
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
        return list;
    }

    private void swap(List<Integer> list, int i, int j) {
        int temp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, temp);
    }

    public int[] bubbleSort(int[] list) {
        for (int i = 1; i < list.length; i++) {
            boolean swapped = false;
            for (int j = 0; j < list.length - i; j++) {
                if (list[j] > list[j + 1]) {
                    swap(list, j, j + 1);
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
        return list;
    }

    private void swap(int[] list, int i, int j) {
        int temp = list[i];
        list[i] = list[j];
        list[j] = temp;
    }
}
