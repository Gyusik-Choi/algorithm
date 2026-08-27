package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Programmers92341_3 {
    public int[] solution(int[] fees, String[] records) {
        Map<String, List<Integer>> park = new HashMap<>();
        for (String r : records) {
            String[] info = r.split(" ");
            int time = convertToMinute(info[0]);
            String car = info[1];
            park.putIfAbsent(car, new ArrayList<>());
            park.get(car).add(time);
        }
        fillOutTime(park);
        Map<String, Integer> fee = new HashMap<>();
        for (Map.Entry<String, List<Integer>> entry : park.entrySet()) {
            fee.put(entry.getKey(), calculateParkFee(fees, entry.getValue()));
        }
        return fee.keySet().stream()
                .sorted()
                .mapToInt(fee::get)
                .toArray();
    }

    private int convertToMinute(String timeStr) {
        String[] t = timeStr.split(":");
        int hour = Integer.parseInt(t[0]);
        int minute = Integer.parseInt(t[1]);
        return hour * 60 + minute;
    }

    private void fillOutTime(Map<String, List<Integer>> parkInfo) {
        for (Map.Entry<String, List<Integer>> entry : parkInfo.entrySet()) {
            if (entry.getValue().size() % 2 == 1) {
                entry.getValue().add(convertToMinute("23:59"));
            }
        }
    }

    private int calculateParkFee(int[] fees, List<Integer> parkTime) {
        int totalTime = 0;
        for (int i = 0; i < parkTime.size(); i += 2) {
            totalTime += parkTime.get(i + 1) - parkTime.get(i);
        }
        return totalTime <= fees[0]
                ? fees[1]
                : fees[1] + (int) Math.ceil((double) (totalTime - fees[0]) / fees[2]) * fees[3];
    }
}
