class Solution {
  List<int> productExceptSelf(List<int> nums) {
    List<int> answer = [];

    int sums = 1;

    for (int i = 0; i < nums.length; i++) {
      answer.add(sums);
      sums *= nums[i];
    }

    sums = 1;

    for (int i = nums.length - 1; i > -1; i--) {
      answer[i] *= sums;
      sums *= nums[i];
    }

    return answer;
  }
}

void main() {
  Solution solution = Solution();
  print(solution.productExceptSelf([1, 2, 3, 4]));
}
