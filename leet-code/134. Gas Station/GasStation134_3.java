package com.example;

public class GasStation134_3 {
    // gas 총합보다 cost 총합이 더 크면 유효한 출발점을 찾을 수 없다.
    // gas[i] - cost[i] 의 누적합이 음수가 나오면
    // 다음 인덱스부터 새로 누적합을 구한다.
    // 누적합이 양수가 되면 해당 양수 누적합을 시작한 지점이 정답이다.
    //
    // [3, 5, 0, 4, 5, 0, 6] - gas
    // [3, 3, 3, 4, 4, 2, 3] - cost
    // [0, 2, -1,          ]
    // [         0, 1, -1, ] -> -1 과 -1을 더하면 누적합 -2
    // [                  3] -> 누적합 -2 와 3을 더하면 1이라 가능
    // 위의 gas 와 cost 를 기준으로 누적합을 구하면
    // 2번 인덱스에서 -1이 된다.
    // 그러면 3번 인덱스부터 새로 누적합을 구하면
    // 5번 인덱스에서 -1이 된다.
    // 이 누적합을 더하면 -2가 되고
    // 남은 누적합은 3이 되는데
    // 3이 -2 보다 크기 때문에 남은 누적합의 시작점인
    // 6번 인덱스가 정답이 된다.
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int answer = 0;
        int start = 0;
        int priorSum = 0;
        while (start < gas.length) {
            int tempSum = 0;
            while (start < gas.length && tempSum >= 0) {
                tempSum += gas[start] - cost[start];
                start += 1;
            }
            priorSum += tempSum;
            if (start == gas.length && priorSum >= 0) {
                return answer;
            }
            // 마지막 인덱스까지 도달하지 않았으면
            // answer 를 갱신해서 새 시작점을 갱신한다
            answer = start;
        }
        // gas 총합 보다 cost 총합이 더 큰 경우
        return -1;
    }
}
