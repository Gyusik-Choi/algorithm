package com.example.sort;

import java.util.List;

public class QuickSort {

    public List<Integer> quickSort(List<Integer> list) {
        quickSort(list, 0, list.size() - 1);
        return list;
    }

    private void quickSort(List<Integer> list, int low, int high) {
        if (low >= high) return;
        int pivot = partition(list, low, high);
        quickSort(list, low, pivot - 1);
        quickSort(list, pivot + 1, high);
    }

    /**
     * pivot 보다 작은 값을
     * left 와 바꾸고 left 를 1 증가 시켜서
     * left 아래로는 pivot 보다 작은 값만 있도록 한다.
     * <br>
     * right 가 pivot 보다 계속 컸다면
     * left 는 갱신되지 않고 제자리에 있는다.
     * 그러다 right 가 pivot 보다 작은 경우가 나오면
     * right 값이 갱신되지 않은 left 위치로 이동한다.
     * left 는 1이 증가되고 left 아래는 pivot 보다
     * 작은 값이 위치하게 된다.
     * <br>
     * right 가 pivot 보다 계속 작으면
     * left 는 갱신된다.
     * left 와 right 를 바꾸고 left 는 1 증가한다.
     * left 아래는 pivot 보다 작은 값이 위치하게 된다.
     * 처음부터 right 가 pivot 보다 작았다면
     * left, right 는 처음에 값이 같아서
     * 서로 바꾸더라도 같은 인덱스라 변화는 없다.
     * 다만 left 아래는 pivot 보다 작은 값이 위치하게 된다.
     */
    private int partition(List<Integer> list, int low, int high) {
        int pivot = list.get(high);
        int left = low;
        for (int right = low; right < high; right++) {
            if (list.get(right) < pivot) {
                swap(list, left, right);
                left += 1;
            }
        }
        swap(list, left, high);
        return left;
    }

    private void swap(List<Integer> list, int left, int right) {
        int temp = list.get(left);
        list.set(left, list.get(right));
        list.set(right, temp);
    }

    public int[] quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
        return arr;
    }

    private void quickSort(int[] arr, int low, int high) {
        if (low >= high) return;
        int pivot = partition(arr, low, high);
        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }

    private int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int left = low;
        for (int right = low; right < high; right++) {
            if (arr[right] >= pivot) continue;
            swap(arr, left, right);
            left += 1;
        }
        swap(arr, left, high);
        return left;
    }

    private void swap(int[] arr, int left, int right) {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
    }
}
