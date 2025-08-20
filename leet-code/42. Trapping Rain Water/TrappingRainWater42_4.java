package com.example;

public class TrappingRainWater42_4 {
    public int trap(int[] height) {
        int amount = 0;
        int maxLeft = height[0], maxRight = height[height.length - 1];
        int left = 0, right = height.length - 1;
        while (left < right) {
            if (height[left] <= height[right]) {
                amount += maxLeft - height[left];
                left += 1;
                maxLeft = Math.max(maxLeft, height[left]);
            } else {
                amount += maxRight - height[right];
                right -= 1;
                maxRight = Math.max(maxRight, height[right]);
            }
        }
        return amount;
    }
}
