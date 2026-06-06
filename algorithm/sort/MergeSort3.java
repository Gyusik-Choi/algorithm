package com.example;

import java.util.ArrayList;
import java.util.List;

public class MergeSort3 {
    /**
     * 파라미터로 들어오는 리스트는 수정하지 않고
     * 정렬한 새 리스트를 반환
     */
    public List<Integer> sortList(List<Integer> list) {
        List<Integer> copiedList = new ArrayList<>(list);
        sortList(copiedList, 0, copiedList.size() - 1);
        return copiedList;
    }

    private void sortList(List<Integer> list, int low, int high) {
        if (low >= high) {
            return;
        }
        int mid = low + (high - low) / 2;
        sortList(list, low, mid);
        sortList(list, mid + 1, high);
        int l = low;
        int h = mid + 1;
        List<Integer> sortedList = new ArrayList<>();
        while (l <= mid && h <= high) {
            if (list.get(l) > list.get(h)) {
                sortedList.add(list.get(h));
                h += 1;
            } else {
                sortedList.add(list.get(l));
                l += 1;
            }
        }
        while (l <= mid) {
            sortedList.add(list.get(l));
            l += 1;
        }
        while (h <= high) {
            sortedList.add(list.get(h));
            h += 1;
        }
        for (int i = 0; i < sortedList.size(); i++) {
            list.set(i + low, sortedList.get(i));
        }
    }
}
