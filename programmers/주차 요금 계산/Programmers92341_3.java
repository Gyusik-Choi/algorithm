package com.example;

import java.util.*;

public class Programmers92341_3 {
    // 건건이 구하는게 아닌 누적 시간으로 요금 구해야 한다
    public int[] solution(int[] fees, String[] records) {
        Map<Integer, List<ParkInfo>> map = new HashMap<>();
        for (String record : records) {
            ParkInfo info = new ParkInfo(record);
            List<ParkInfo> value = map.getOrDefault(info.car, new ArrayList<>());
            value.add(info);
            map.put(info.car, value);
        }
        Map<Integer, Integer> fee = new HashMap<>();
        for (Map.Entry<Integer, List<ParkInfo>> entry : map.entrySet()) {
            int totalParkTime = 0;
            List<ParkInfo> infoList = entry.getValue();
            for (int i = 0; i < infoList.size(); i += 2) {
                ParkInfo in = infoList.get(i);
                ParkInfo out = infoList.size() - 1 < i + 1 ? new ParkInfo("23:59 " + in.car + " OUT") : infoList.get(i + 1);
                totalParkTime += out.time - in.time;
            }
            int totalFee = getFee(fees, totalParkTime);
            fee.put(entry.getKey(), totalFee);
        }
        return fee.keySet().stream()
                .sorted()
                .mapToInt(fee::get)
                .toArray();
    }

    private int getFee(int[] fees, int parkTime) {
        int basicTime = fees[0], basicFee = fees[1], unitTime = fees[2], unitFee = fees[3];
        if (parkTime <= basicTime) {
            return basicFee;
        }
        int leftTime = parkTime - basicTime;
        // double 로 캐스팅 하지 않으면 154 / 10 이 15 가 되어버린다
        // double 로 캐스팅을 해야 15.4 가 되고
        // 이를 Math.ceil 로 올림을 해서 16.0 으로 만들 수 있다
        // 그리고 이를 정수로 변환하기 위해 int 로 캐스팅한다
        return basicFee + (unitFee * (int) Math.ceil((double) leftTime / unitTime));
    }

    static class ParkInfo {
        final int time;
        final int car;
        final CarState state;

        ParkInfo(String record) {
            String[] info = record.split(" ");
            this.time = convertToMinute(info[0]);
            this.car = Integer.parseInt(info[1]);
            this.state = info[2].equals("IN") ? CarState.IN : CarState.OUT;
        }

        private int convertToMinute(String time) {
            String[] t = time.split(":");
            return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
        }
    }

    enum CarState {
        IN,
        OUT,
    }
}
