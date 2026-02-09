package com.example;

public class BestTimeToBuyAndSellStock121_4 {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int prev = 10001;
        for (int price : prices) {
            if (prev >= price) {
                prev = price;
                continue;
            }
            profit = Math.max(profit, price - prev);
        }
        return profit;
    }
}
