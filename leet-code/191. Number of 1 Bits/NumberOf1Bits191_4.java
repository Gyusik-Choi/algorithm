package com.example;

public class NumberOf1Bits191_4 {
    public int hammingWeight(int n) {
        // 이진수에서 1을 빼면 반드시 최소 하나는
        // 비트가 반전된다
        // 0에서 1을 빼면
        // 상위의 1이 첫번째로 나오는 비트까지 모두 반전된다
        // 1에서 1을 빼면
        // 해당 비트만 반전된다
        // 특정 숫자와 특정 숫자에서 1을 뺀 숫자를
        // and 연산하면 해당 자리수까지는 모두 0이 되기 때문에
        // 결과적으로 전체 비트의 1의 갯수가 한개 줄어든다
        int count = 0;
        while (n > 0) {
            count += 1;
            n = n & (n - 1);
        }
        return count;
    }
}
