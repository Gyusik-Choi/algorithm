package com.example

class MaximumMatchingOfPlayersWithTrainers2410 {
    fun matchPlayersAndTrainers(players: IntArray, trainers: IntArray): Int {
        players.sort()
        trainers.sort()
        var match = 0
        var playerIdx = 0
        var trainerIdx = 0
        while (playerIdx < players.size && trainerIdx < trainers.size) {
            if (players[playerIdx] <= trainers[trainerIdx]) {
                match++
                playerIdx++
            }
            trainerIdx++
        }
        return match
    }
}
