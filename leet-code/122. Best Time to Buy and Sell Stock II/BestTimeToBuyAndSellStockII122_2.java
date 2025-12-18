package com.example;

import java.util.stream.IntStream;

public class BestTimeToBuyAndSellStockII122_2 {
    public int maxProfit(int[] prices) {
        return IntStream.range(1, prices.length)
                // 이 문제를 풀이하기 위해서는 첫번째 인자로 identity 를 0으로 설정해줘야 한다
                // identity 를 제외하고 operator 만 인자로 넣으면
                // operator 연산자의 첫번째 파라미터는 stream 의 첫번째 값이 되고
                // operator 연산자의 두번째 파라미터는 stream 의 두번째 값이 된다
                // 따라서 IntStream 의 시작 범위인 1부터 시작하지 못하고
                // acc 가 1이 되버린채 시작을 2부터 하게 된다
                // 게다가 acc 가 0이 아닌 1이 되어서 1을 초기값으로 두고 시작하게 돼서 정답을 구할 수 없다
                // 아래는 javascript 의 reduce 설명이긴 하지만 원리는 유사하기 때문에 참고하기 좋은 설명이다
                // https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce#%EC%84%A4%EB%AA%85
               .reduce(0, (acc, i) -> acc + Math.max(0, prices[i] - prices[i - 1]));
    }
}
