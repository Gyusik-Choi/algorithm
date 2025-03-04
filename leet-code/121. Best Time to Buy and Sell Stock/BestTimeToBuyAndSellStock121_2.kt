package com.example

class BestTimeToBuyAndSellStock121_2 {
    fun maxProfit(prices: IntArray): Int {
        var minPrice = prices[0]
        var maxProfit = 0
        for (i in prices.indices) {
            minPrice = minPrice.coerceAtMost(prices[i])
            maxProfit = maxProfit.coerceAtLeast(prices[i] - minPrice)
        }
        return maxProfit
    }
}
