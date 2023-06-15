class Solution {
  List<int> twoSum(List<int> nums, int target) {
    Map<int, int> numMap = Map<int, int>();

    for (int i = 0; i < nums.length; i++) {
      numMap[nums[i]] = i;
    }

    for (int i = 0; i < nums.length; i++) {
      if (numMap.containsKey(target - nums[i]) && i != numMap[target - nums[i]]) {
        return [i, numMap[target - nums[i]]!];
      }
    }
    
    return [];
  }
}

void main() {
  Solution solution = Solution();
  print(solution.twoSum([2, 7, 11, 15], 9));
  print(solution.twoSum([3, 2, 4], 6));
}
