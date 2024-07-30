public class ProductOfArrayExceptSelf238_2 {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];

        int total = 1;
        for (int i = 0; i < nums.length; i++) {
            answer[i] = total;
            total *= nums[i];
        }

        total = 1;
        for (int i = nums.length - 1; i > - 1; i--) {
            answer[i] *= total;
            total *= nums[i];
        }

        return answer;
    }
}
