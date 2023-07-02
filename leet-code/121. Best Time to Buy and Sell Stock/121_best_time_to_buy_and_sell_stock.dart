import 'dart:math';

class Solution {
  int maxProfit(List<int> prices) {
    int minPrice = 100001;
    int profit = 0;

    for (int i = 0; i < prices.length; i++) {
      int curPrice = prices[i];
      minPrice = min(minPrice, curPrice);
      profit = max(profit, curPrice - minPrice);
    }

    return profit;
  }
}

void main() {
  Solution solution = Solution();
  print(solution.maxProfit([7, 1, 5, 3, 6, 4]));
  print(solution.maxProfit([7, 6, 4, 3, 1]));
  print(solution.maxProfit([6, 1, 5, 8, 7, 9]));
}
