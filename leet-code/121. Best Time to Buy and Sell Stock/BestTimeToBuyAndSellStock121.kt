package com.example

import kotlin.math.max

class BestTimeToBuyAndSellStock121 {
    fun maxProfit(prices: IntArray): Int {
        // 작으면 갱신, 크면 일단 뺀다
        var minPrice = prices[0]
        var maxProfit = 0
        for (i in prices.indices) {
            if (minPrice >= prices[i]) {
                minPrice = prices[i]
            } else {
                maxProfit = max(maxProfit, prices[i] - minPrice)
            }
        }
        return maxProfit
    }
}
