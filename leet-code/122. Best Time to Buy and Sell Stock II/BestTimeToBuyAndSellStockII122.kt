package com.example

class BestTimeToBuyAndSellStockII122 {
    fun maxProfit(prices: IntArray): Int {
        var maxProfit = 0
        for (i in 0 until prices.size - 1) {
            if (prices[i] < prices[i + 1]) {
                maxProfit += prices[i + 1] - prices[i]
            }
        }
        return maxProfit
    }
}
