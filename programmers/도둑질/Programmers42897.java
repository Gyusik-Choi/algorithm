package com.example;

public class Programmers42897 {
    public int solution(int[] money) {
        int[][] dp = new int[2][money.length];
        dp[1][1] = money[1];
        for (int i = 2; i < money.length; i++) {
            dp[0][i] = Math.max(dp[0][i - 2] + money[i], dp[0][i - 1]);
            dp[1][i] = Math.max(dp[1][i - 2] + money[i], dp[1][i - 1]);
        }
        // https://school.programmers.co.kr/questions/9297
        // dp[0][0] 에 money[0] 을 설정하면 안 된다
        // dp[1][1] 에 money[1] 을 설정하는 것과 차이는
        // 2번 인덱스(dp[0][2] 혹은 dp[1][2]) 를 구할 때
        // dp[0][0] 의 경우 직전 인덱스 대신
        // 전전의 인덱스와 현재 인덱스를 합을 선택하면 전전의 인덱스도 포함이 된다
        // dp[1][1] 의 경우 직전 인덱스 대신
        // 전전의 인덱스와 현재 인덱스를 합을 선택하면 전전의 인덱스가 포함되지 않는다
        // 왜냐하면 dp[1][0] 은 0으로 설정했기 때문에 사실 선택하지 않았다
        // 그래서 dp[1][0] + money[2] 는 money[2] 를 선택하는 것과 같다
        // 0번, 1번 인덱스 모두 선택하지 않는게 된다
        // 반면에 dp[0][0] + money[2] 는 0번 인덱스를 선택한게 된다
        //
        // [10, 2, 2, 100, 2]
        // money 배열이 위와 같을 때
        // 3번째 인덱스를 구할 때 100을 선택하고 10과 더해야 한다
        // dp[0] -> [0, 0, 2, 100, 100]
        // dp[1] -> [0, 2, 2, 102, 102]
        // 위와 같은 결과가 돼서 최종적으로 100 에 10을 더해서 110이 리턴된다
        // 그런데 만약에 dp[0][0] 에 money[0] 을 할당하면
        // dp[0] -> [10, 0, 12, 100, 100]
        // dp[1] -> [0, 2, 2, 102, 102]
        // 위와 같은 결과가 돼서 최종적으로 102가 리턴된다
        // 물론
        // dp[0][0] 에 money[0] 의 할당 여부와 관계없이
        // dp[0] 의 뒤쪽 값은 100, 100 이다
        // 그런데 의미는 다르다
        // dp[0][0] 에 money[0] 를 할당한 경우는
        // dp[0][3] 에게 dp[0][0] 을 선택할 기회가 주어지지 않지만
        // dp[0][0] 에 money[0] 를 할당하지 않은 경우는
        // dp[0][3] 에게 dp[0][0] 을 선택할 기회가 주어진다
        //
        // dp[0][0] 에 money[0] 을 할당하지 않고
        // 추후에 money[0] 과 dp[0][money.length - 2] 를 더한다
        return Math.max(money[0] + dp[0][money.length - 2], dp[1][money.length - 1]);
        // return Math.max(dp[0][money.length - 2], dp[1][money.length - 1]);
    }
}
