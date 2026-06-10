package com.example;

public class CountingSort2 {
    public int[] sort(int[] arr) {
        int maxValue = getMaxValue(arr);
        int[] countArr = new int[maxValue + 1];
        for (int i = 0; i < arr.length; i++) {
            countArr[arr[i]] += 1;
        }
        for (int i = 1; i < countArr.length; i++) {
            countArr[i] += countArr[i - 1];
        }
        int[] answer = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            countArr[arr[i]] -= 1;
            answer[countArr[arr[i]]] = arr[i];
        }
        return answer;
    }

    private int getMaxValue(int[] arr) {
        int maxValue = arr[0];
        for (int i = 1; i < arr.length; i++) {
            maxValue = Math.max(maxValue, arr[i]);
        }
        return maxValue;
    }
}
