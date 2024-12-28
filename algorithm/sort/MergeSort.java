package com.example.sort;

import java.util.ArrayList;
import java.util.List;

public class MergeSort {

    public List<Integer> mergeSort(List<Integer> list) {
        mergeSort(list, 0, list.size() - 1);
        return list;
    }

    private void mergeSort(List<Integer> list, int left, int right) {
        if (left >= right) return;
        int mid = (left + right) / 2;
        mergeSort(list, left, mid);
        mergeSort(list, mid + 1, right);

        int l = left;
        int r = mid + 1;
        List<Integer> temp = new ArrayList<>();
        while (l <= mid && r <= right) {
            if (list.get(l) <= list.get(r)) temp.add(list.get(l++));
            else temp.add(list.get(r++));
        }
        while (l <= mid) temp.add(list.get(l++));
        while (r <= right) temp.add(list.get(r++));

        for (int i = 0; i < temp.size(); i++) list.set(left + i, temp.get(i));
    }

    public int[] mergeSort(int[] arr) {
        mergeSort(arr, 0, arr.length - 1);
        return arr;
    }

    private void mergeSort(int[] arr, int left, int right) {
        if (left >= right) return;
        int mid = (left + right) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        int idx = 0;
        int l = left;
        int r = mid + 1;
        int[] temp = new int[right - left + 1];
        while (l <= mid && r <= right) {
            if (arr[l] <= arr[r]) temp[idx++] = arr[l++];
            else temp[idx++] = arr[r++];
        }
        while (l <= mid) temp[idx++] = arr[l++];
        while (r <= right) temp[idx++] = arr[r++];

        for (int i = 0; i < temp.length; i++) arr[i + left] = temp[i];
    }
}
