package com.example;

public class SortColors75 {
    public void sortColors(int[] nums) {
        int red = 0;
        int white = 0;
        int blue = nums.length - 1;

        while (white <= blue) {
            if (nums[white] < 1) {
                swap(nums, red, white);
                red++;
                white++;
            } else if (nums[white] > 1) {
                swap(nums, white, blue);
                blue--;
            } else {
                white++;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
