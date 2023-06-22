class Solution {
  List<List<int>> threeSum(List<int> nums) {
    nums.sort();
    List<List<int>> answer = [];

    for (int i = 0; i < nums.length - 2; i++) {
      if (i > 0 && nums[i - 1] == nums[i]) {
        continue;
      }

      int left = i + 1;
      int right = nums.length - 1;

      while (left < right) {
        int sums = nums[i] + nums[left] + nums[right];

        if (sums > 0) {
          right -= 1;
          continue;
        }

        if (sums < 0) {
          left += 1;
          continue;
        }

        answer.add([nums[i], nums[left], nums[right]]);

        while (left < right && nums[left] == nums[left + 1]) {
          left += 1;
        }

        while (left < right && nums[right] == nums[right - 1]) {
          right -= 1;
        }

        left += 1;
        right -= 1;
      }
    }

    return answer;
  }
}

void main() {
  Solution solution = Solution();
  print(solution.threeSum([-1, 0, 1, 2, -1, -4]));
  print(solution.threeSum([0, 0, 0, 0]));
}
