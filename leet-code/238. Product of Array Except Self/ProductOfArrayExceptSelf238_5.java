package com.example;

public class ProductOfArrayExceptSelf238_5 {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] arr = new int[length];
        int[] toRight = nums.clone();
        int[] toLeft = nums.clone();
        for (int i = 1; i < length; i++) toRight[i] *= toRight[i - 1];
        for (int i = length - 2; i >= 0; i--) toLeft[i] *= toLeft[i + 1];
        arr[0] = toLeft[1];
        arr[length - 1] = toRight[length - 2];
        for (int i = 1; i < length - 1; i++) arr[i] = toRight[i - 1] * toLeft[i + 1];
        return arr;
    }
}
