package com.example;

public class CountingSort2 {
    public int[] sort(int[] arr) {
        int maxValue = getMaxValue(arr);
        // 음수 값에 대비하여 offset 만큼 인덱스를 양수로 이동한다
        int offset = getMinValue(arr);
        int[] countArr = new int[maxValue - offset + 1];
        for (int i = 0; i < arr.length; i++) {
            countArr[arr[i] - offset] += 1;
        }
        for (int i = 1; i < countArr.length; i++) {
            countArr[i] += countArr[i - 1];
        }
        int[] answer = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            countArr[arr[i] - offset] -= 1;
            answer[countArr[arr[i] - offset]] = arr[i];
        }
        return answer;
    }

    private int getMinValue(int[] arr) {
        int minValue = arr[0];
        for (int i = 1; i < arr.length; i++) {
            minValue = Math.min(minValue, arr[i]);
        }
        return minValue;
    }

    private int getMaxValue(int[] arr) {
        int maxValue = arr[0];
        for (int i = 1; i < arr.length; i++) {
            maxValue = Math.max(maxValue, arr[i]);
        }
        return maxValue;
    }
}
