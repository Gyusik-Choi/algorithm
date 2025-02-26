package com.example;

public class TrappingRainWater42_3 {

    public int trap(int[] height) {
        int leftMax = height[0], left = 0;
        int rightMax = height[height.length - 1] , right = height.length - 1;
        int trappingWater = 0;
        while (left < right) {
            if (height[left] <= height[right]) {
                left += 1;
                leftMax = Math.max(leftMax, height[left]);
                if (Math.min(leftMax, height[right]) > height[left]) {
                    trappingWater += Math.min(leftMax, height[right]) - height[left];
                }
            } else {
                right -= 1;
                rightMax = Math.max(rightMax, height[right]);
                if (Math.min(height[left], rightMax) > height[right]) {
                    trappingWater += Math.min(height[left], rightMax) - height[right];
                }
            }
        }
        return trappingWater;
    }
}
