public class BestTimeToBuyAndSellStock121 {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int max = prices[0];
        int min = prices[0];
        for (int i = 1; i < prices.length; i++) {
            int cur = prices[i];

            if (min > cur) {
                max = cur;
                min = cur;
                continue;
            }

            if (max < cur) {
                max = cur;
//                profit 을 구한 후
//                기존의 min 보다 더 작은 cur 이 나와서
//                min 이 갱신되면 max 도 함께 갱신된다
//                이후 max 보다 큰 cur 이 나오면
//                max - min 을 하는데
//                이 값이 기존의 profit 보다 작을 수 있다
//                그래서 Math.max 로 둘 중 더 큰 값을 설정한다
//                profit = max - min;
                profit = Math.max(profit, max - min);
            }
        }
        System.out.println(profit);
        return profit;
    }
}
