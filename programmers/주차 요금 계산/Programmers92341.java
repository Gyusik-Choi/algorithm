package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Programmers92341 {

    public int[] solution(int[] fees, String[] records) {
        // 차량번호별 내역
        Map<Integer, List<String>> parking = new HashMap<>();
        for (String r : records) {
            String[] record = r.split(" ");
            String time = record[0];
            int carNumber = Integer.parseInt(record[1]);
            String type = record[2];
            List<String> parkInfo = parking.getOrDefault(carNumber, new ArrayList<>());
            parkInfo.add(time);
            parking.put(carNumber, parkInfo);
        }

        Map<Integer, Integer> parkingFee = new HashMap<>();
        for (Map.Entry<Integer, List<String>> entry : parking.entrySet()) {
            List<String> parkInfo = entry.getValue();
            int totalParkingTime = 0;
            for (int i = 0; i < parkInfo.size(); i += 2) {
                // 마지막 인덱스
                if (i == parkInfo.size() - 1) {
                    totalParkingTime += convertToMinute("23:59") - convertToMinute(parkInfo.get(i));
                } else {
                    totalParkingTime += convertToMinute(parkInfo.get(i + 1)) - convertToMinute(parkInfo.get(i));
                }
            }
            // 총 시간 > 기본 시간
            // 기본 요금 + [총 시간 - 기본 시간] / 단위 시간 * 단위 요금
            // 총 시간 <= 기본 시간
            // 기본 요금
            int fee = 0;
            if (totalParkingTime > fees[0]) {
                fee += fees[1] + (int) Math.ceil((double) (totalParkingTime - fees[0]) / fees[2]) * fees[3];
            } else {
                fee += fees[1];
            }
            parkingFee.put(entry.getKey(), fee);
        }

        // 차량번호만 뽑아서 리스트로 만든 뒤
        // 리스트를 정렬하고
        // 정렬한 리스트의 요소를
        // 요금으로 변경하고
        // 배열로 변환해서 리턴
        return new ArrayList<>(parkingFee.keySet())
                .stream()
                .sorted()
                .map(parkingFee::get)
                .mapToInt(Integer::intValue)
                .toArray();
    }

    private int convertToMinute(String time) {
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }

    // 차량 번호가 작은 자동차부터
    // 청구할 주차 요금을 정수 배열에 담아서 return

    // 우선 차량 정보를 모아야 한다 -> 해시맵
    // Map<Integer, List<String>>
    // 키는 차량번호, 값은 '시간 내역' 문자열을 리스트로 모은다
    // Map 을 loop 돌면서 차량별로 요금 계산
    // 요금에 대한 별도의 해시맵 구성
    // Map<Integer, Integer>
    // 키는 차량번호, 값은 요금
    // 차량번호를 기준으로 정렬하고 요금만 배열로 묶어서 리턴

    // 요금 계산 방법
    // 올바른 입력만 주어진다
    // 출차가 먼저 나오는 경우는 없다
    // 입차가 나오고 또 입차가 나오는 경우도 없다
    // 입차 후에 출차가 없으면 23:59 에서 출차 했다고 간주
    // 입차 후에 출차가 있으면 출차에서 입차 시간을 뺀다
    // 홀수 인덱스 - 입차, 짝수 인덱스 - 출차
    // 0부터 2씩 건너 뛰면서 계산
    // 현재 인덱스가 마지막 인덱스면 23:59 에서 빼고
    // 현재 인덱스가 마지막 인덱스가 아니면 다음 인덱스에서 뺀다

    // fees
    // [기본 시간, 기본 요금, 단위 시간, 단위 요금]
    // records
    // 시간, 차량번호, 내역
    // records -> split(" ")
    // 05:11 1234 IN
    // 시간을 분으로 변경
}
