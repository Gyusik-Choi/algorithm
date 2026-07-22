package com.example

import kotlin.math.max

class BestTimeToBuyAndSellStockII122_2 {
    fun maxProfit(prices: IntArray): Int {
        return IntRange(1, prices.lastIndex).sumOf { max(0, prices[it] - prices[it - 1]) }
    }
}