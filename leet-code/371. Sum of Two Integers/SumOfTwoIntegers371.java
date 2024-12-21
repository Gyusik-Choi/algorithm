package com;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class SumOfTwoIntegers371 {
    /**
     *  carry out
     *  둘 중에 하나라도 1이 있으면 1이 되도록 한다
     *  1. a 와 b 모두 1이 거나 (AND)
     *  2. a + b 를 더한 값과 (XOR) carry in 이 둘다 1이 됐을 경우
     *
     *  입력값이 둘 다 1이어야 AND 연산의 결과가 1이 될 수 있다
     *  a + b 를 더한 값(XOR)과 직전 carry 가 둘 다 1이어야
     *  AND 연산의 결과가 1이 될 수 있다
     *
     *  논리 연산을 생각하지 않고
     *  단순히 덧셈을 한다고 생각하니 좀 더 이해하기 편했다
     *  a + b 를 더해서 자리 올림이 발생하거나
     *  a + b 를 더한 값에 직전 자리 올림을 더하니 자리 올림이 발생하면
     *  자리 올림이 발생한다
     *
     *  a + b 를 더해서 자리 올림이 발생하려면 둘 다 1이어야 하기 때문에
     *  둘 다 1일 때만 1이 되려면 AND 연산이 필요하다
     *  a + b 를 더한 값에 직전 자리 올림을 더해서 자리 올림이 발생하려면
     *  마찬가지로 여기도 둘 (a + b 더한 값, 직전 자리 올림) 다 1일 때만 1이 되려면 AND 연산이 필요하다
     *  둘 중 하나라도 충족하면 자리 올림이 발생할 수 있어서 이를 OR 연산으로 볼 수 있다
     */
    public int getSum(int a, int b) {
        String binaryA = String.format("%32s", Integer.toBinaryString(a)).replace(' ', '0');
        String binaryB = String.format("%32s", Integer.toBinaryString(b)).replace(' ', '0');
        return getBinarySum(binaryA, binaryB);
    }

    private int getBinarySum(String binA, String binB) {
        List<Character> sums = new ArrayList<>();
        int carry = 0;
        for (int i = 31; i > -1; i--) {
            int a = Character.getNumericValue(binA.charAt(i));
            int b = Character.getNumericValue(binB.charAt(i));

            int s1 = a ^ b;
            int c1 = a & b;
            int c2 = s1 & carry;

            int sum = s1 ^ carry;
            carry = c1 | c2;
            sums.add(0, Character.forDigit(sum, 2));
        }
        return Integer.parseUnsignedInt(
                sums.stream()
                        .map(String::valueOf)
                        .collect(Collectors.joining("")),
                2);
    }
}
