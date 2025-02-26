import kotlin.math.max

class TrappingRainWater42 {
    fun trap(height: IntArray): Int {
        var sums: Int = 0
        var left: Int = 0
        var leftMax: Int = height[left]
        var right: Int = height.size - 1
        var rightMax: Int = height[right]

        while (left < right) {
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if (leftMax <= rightMax) {
                if (leftMax > height[left]) {
                    sums += leftMax - height[left]
                }
                left += 1
            } else {
                if (rightMax > height[right]) {
                    sums += rightMax - height[right]
                }
                right -= 1
            }
        }
        return sums
    }
}
