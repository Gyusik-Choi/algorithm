// leetcode 서버가 고장나서 정답 확인은 추후 서버가 복구되면 할 예정

class Solution {
  int arrayPairSum(List<int> nums) {
    nums.sort();
    int sums = 0;

    for (int i = 0; i < nums.length; i++) {
      if (i % 2 == 0) {
        sums += nums[i];
      }
    }

    return sums;
  }
}

void main() {
  Solution solution = Solution();
  print(solution.arrayPairSum([1, 4, 3, 2]));
}
