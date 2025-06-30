package com.example;

public class SortColors75_2 {
    public void sortColors(int[] nums) {
        int red = 0;
        int white = 0;
        int blue = nums.length - 1;

        while (white <= blue) {
            if (nums[white] < 1) {
                swap(nums, red, white);
                red += 1;
                white += 1;
            } else if (nums[white] > 1 ) {
                swap(nums, white, blue);
                blue -= 1;
            } else {
                white += 1;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
