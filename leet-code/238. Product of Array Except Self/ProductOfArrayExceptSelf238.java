public class ProductOfArrayExceptSelf238 {
    public int[] productExceptSelf(int[] nums) {
        int[] leftToRight = new int[nums.length];
        leftToRight[0] = nums[0];
        for (int i = 1; i < leftToRight.length; i++) {
            leftToRight[i] = leftToRight[i - 1] * nums[i];
        }

        int[] rightToLeft = new int[nums.length];
        rightToLeft[nums.length - 1] = nums[nums.length - 1];
        for (int i = rightToLeft.length - 2; i > - 1; i--) {
            rightToLeft[i] = rightToLeft[i + 1] * nums[i];
        }

        nums[0] = rightToLeft[1];
        nums[nums.length - 1] = leftToRight[nums.length - 2];
        for (int i = 1; i < nums.length - 1; i++) {
            nums[i] = leftToRight[i - 1] * rightToLeft[i + 1];
        }

        return nums;
    }
}
