package com.example;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class QueueReconstructionByHeight406_3 {
    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, (p1, p2) -> p1[0] == p2[0] ? p1[1] - p2[1] : p2[0] - p1[0]);
        List<int[]> list = new ArrayList<>();
        for (int i = 0; i < people.length; i++) {
            if (people[i][1] >= list.size()) {
                list.add(new int[]{people[i][0], people[i][1]});
            } else {
                list.add(people[i][1], new int[]{people[i][0], people[i][1]});
            }
        }
        return list.toArray(new int[list.size()][]);
    }
}
