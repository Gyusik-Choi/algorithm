import 'dart:math';

class Solution {
  int trap(List<int> height) {
    int total = 0;

    int left = 0;
    int right = height.length - 1;

    int leftMax = height[left];
    int rightMax = height[right];

    while (left < right) {
      leftMax = max(leftMax, height[left]);
      rightMax = max(rightMax, height[right]);

      if (leftMax <= rightMax) {
        total += leftMax - height[left];
        left += 1;
      } else {
        total += rightMax - height[right];
        right -= 1;
      }
    }

    return total;
  }
}

void main() {
  Solution solution = Solution();
  print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));
  print(solution.trap([4, 2, 0, 3, 2, 5]));
  print(solution.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]));
}
