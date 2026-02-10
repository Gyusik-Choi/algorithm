package com.example

class BestTimeToBuyAndSellStock121_3 {
    fun maxProfit(prices: IntArray): Int {
        var profit = 0
        var prev = 10001
        for (price in prices) {
            prev = prev.coerceAtMost(price)
            profit = profit.coerceAtLeast(price - prev)
        }
        return profit
    }
}
