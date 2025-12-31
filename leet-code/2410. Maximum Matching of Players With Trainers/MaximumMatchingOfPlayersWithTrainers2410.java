package com.example;

import java.util.Arrays;

public class MaximumMatchingOfPlayersWithTrainers2410 {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Arrays.sort(players);
        Arrays.sort(trainers);
        int numberOfMatching = 0;
        int playerIdx = 0;
        for (int trainer : trainers) {
            if (playerIdx == players.length) {
                break;
            }
            int player = players[playerIdx];
            if (player > trainer) {
                continue;
            }
            numberOfMatching += 1;
            playerIdx += 1;
        }
        return numberOfMatching;
    }
}
