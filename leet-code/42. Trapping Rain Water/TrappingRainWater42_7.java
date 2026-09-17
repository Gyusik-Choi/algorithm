package com.example;

public class TrappingRainWater42_7 {
    public int trap(int[] height) {
        int sums = 0;
        int left = 0, right = height.length - 1;
        int leftMax = height[left], rightMax = height[right];
        while (left < right) {
            if (height[left] <= height[right]) {
                if (leftMax > height[left]) {
                    sums += leftMax - height[left];
                } else {
                    leftMax = height[left];
                }
                left++;
            } else {
                if (rightMax > height[right]) {
                    sums += rightMax - height[right];
                } else {
                    rightMax = height[right];
                }
                right--;
            }
        }
        return sums;
    }
    // 왼쪽과 오른쪽 중에서
    // 왼쪽이 작거나 같으면 왼쪽을 이동하고
    // 그렇지 않으면 오른쪽을 이동한다
    // 이동해서 기존의 값보다 작은 값이면
    // 차이를 누적한다
}
