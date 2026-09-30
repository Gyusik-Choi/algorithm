int maxProfit(int* prices, int pricesSize) {
    int profit = 0;
    int min_price = prices[0];
    for (int i = 1; i < pricesSize; i++) {
        if (min_price >= prices[i]) {
            min_price = prices[i];
        } else {
            if (profit < prices[i] - min_price) {
                profit = prices[i] - min_price;
            }
        }
    }
    return profit;
}