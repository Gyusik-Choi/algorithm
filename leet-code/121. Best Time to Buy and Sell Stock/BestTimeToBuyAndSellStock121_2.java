public class BestTimeToBuyAndSellStock121_2 {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int minPrice = prices[0];
        for (int price : prices) {
            minPrice = Math.min(minPrice, price);
            profit = Math.max(profit, price - minPrice);
        }
        return profit;
    }
}
