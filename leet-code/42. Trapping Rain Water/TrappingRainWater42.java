public class TrappingRainWater42 {
    public int trap(int[] height) {
        int sums = 0;
        int left = 0;
        int leftMax = height[left];
        int right = height.length - 1;
        int rightMax = height[right];

        while (left < right) {
            // 최대값 갱신
            leftMax = Math.max(leftMax, height[left]);
            rightMax = Math.max(rightMax, height[right]);

            // 물은
            // 현재 값이
            // 양쪽 최대값 보다 작으면서
            // 양쪽 최대값 중 더 작은 값과의 차이만큼 담길 수 있다
            //
            // 최대값이 더 작은 쪽이 이동한다
            // (최대값이 같을 경우 둘 중 하나만 이동한다)
            if (leftMax <= rightMax) {
                // 최대값이 현재값 보다 큰 경우
                // 최대값에서 현재값을 뺀 값을 총합에 더한다
                if (leftMax > height[left]) {
                    sums += leftMax - height[left];
                }
                left += 1;
            } else {
                if (rightMax > height[right]) {
                    sums += rightMax - height[right];
                }
                right -= 1;
            }
        }

        return sums;
    }
}
