package com.example;

public class BestTimeToBuyAndSellStock121_3 {
    public int maxProfit(int[] prices) {
        // 최소값 보다 작은 값이 나오면 최소값 갱신
        // 최소값 보다 크거나 같은 값이 나오면 최소값과 빼서 최대값 비교
        int minStock = 10000;
        int maxProfit = 0;
        for (int price : prices) {
            if (minStock > price) {
                minStock = price;
            } else {
                maxProfit = Math.max(maxProfit, price - minStock);
            }
        }
        return maxProfit;
    }
}
