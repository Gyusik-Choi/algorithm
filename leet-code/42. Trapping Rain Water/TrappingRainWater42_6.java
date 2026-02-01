package com.example.algorithm;

public class TrappingRainWater42_6 {
    public int trap(int[] height) {
        int sums = 0;
        int leftMax = height[0];
        int rightMax = height[height.length - 1];
        int leftIdx = 0;
        int rightIdx = height.length - 1;
        while (leftIdx < rightIdx) {
            if (height[leftIdx] <= height[rightIdx]) {
                sums += Math.max(0, leftMax - height[leftIdx]);
                leftMax = Math.max(leftMax, height[leftIdx]);
                leftIdx += 1;
            } else {
                sums += Math.max(0, rightMax - height[rightIdx]);
                rightMax = Math.max(rightMax, height[rightIdx]);
                rightIdx -= 1;
            }
        }
        return sums;
    }
}
