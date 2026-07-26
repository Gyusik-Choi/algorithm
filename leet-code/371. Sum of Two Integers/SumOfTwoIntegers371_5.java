package com.example;

public class SumOfTwoIntegers371_5 {
    // 4비트 단위로
    // carry lookahead 와 ripple carry 결합한 형태로 구현한다
    public int getSum(int a, int b) {
        // generate
        int G = a & b;
        // propagate
        int P = a ^ b;
        int result = 0;
        int carry = 0;
        // 총 32비트를 8번에 걸쳐서 4비트씩 만들어간다
        for (int block = 0; block < 8; block++) {
            // 곱하기 4 를 해서 shift 할 비트를 늘린다
            // 0, 4, 8, 12 ...
            int shift = block << 2;
            // 32비트에서 맨 하위 4비트부터 4비트 단위로 이동시키고
            // 1111 과 and 연산을 통해 나머지 비트를 0으로 걸러낸다
            // (0xF 는 1111 과 같음)
            int gNibble = (G >>> shift) & 0xF;
            int pNibble = (P >>> shift) & 0xF;

            int[] out = cla4(gNibble, pNibble, carry);
            // 32비트 중 해당하는 자리에 놓기 위해 shift 연산으로 이동시킨다
            result |= out[0] << shift;
            carry = out[1];
        }
        return result;
    }

    private int[] cla4(int g, int p, int cin) {
        // 1비트씩 나누기 위해 >> 과 & 연산 사용한다
        // >> 로 이동시키고 & 로 나머지 비트를 0으로 변환한다
        // 예를 들어,
        // g1 은 우측으로 1비트를 밀고 and 연산으로
        // 나머지 비트를 0으로 변환한다
        int g0 = g & 1, p0 = p & 1;
        int g1 = (g >> 1) & 1, p1 = (p >> 1) & 1;
        int g2 = (g >> 2) & 1, p2 = (p >> 2) & 1;
        int g3 = (g >> 3) & 1, p3 = (p >> 3) & 1;

        // ci+1 = gi | (pi & ci)
        // ex>
        // 아래는 이해를 돕기 위한 표기로 OR을 +로, AND를 *로 바꿔서 씀
        // c2 에서 c1 의 자리에 g0 +(p0 * c0) 를 대입할 수 있다
        // c1 = g0 +(p0 * c0)
        // c2 = g1 + (p1 * c1)
        // c2 = g1 + (p1 * (g0 +(p0 * c0)))
        // c2 = g1 + (p1 * g0) + (p1 * p0 * c0)
        int c1 = g0 | (p0 & cin);
        int c2 = g1 | (p1 & g0) | (p1 & p0 & cin);
        int c3 = g2 | (p2 & g1) | (p2 & p1 & g0) | (p2 & p1 & p0 & cin);
        int cout = g3 | (p3 & g2) | (p3 & p2 & g1) | (p3 & p2 & p1 & g0) | (p3 & p2 & p1 & p0 & cin);

        // 4비트의 각 비트별로 합을 구한다
        // sum 은 a ^ b ^ carry 로 구하는데
        // p 는 이미 a ^ b 로 구했기 때문에 carry 만 ^ 로 추가 계산한다
        int s0 = p0 ^ cin, s1 = p1 ^ c1, s2 = p2 ^ c2, s3 = p3 ^ c3;
        // s0, s1, s2, s3 를 4비트 단위로 합치기 위해 각 자리에 << 연산으로 이동시킨다
        int sumNibble = s0 | (s1 << 1) | (s2 << 2) | (s3 << 3);

        return new int[]{sumNibble, cout};
    }
}
