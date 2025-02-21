package com.example;

import java.util.*;

public class MostCommonWord819_3 {

    public String mostCommonWord(String paragraph, String[] banned) {
        String[] words = paragraph
                .replaceAll("[^a-zA-Z]+", " ")
                .toLowerCase()
//                 trim 을 사용해서 앞뒤 문자열 공백을 제거한다
//                 아래의 paragraph 가 주어졌을 때
//                 "..Bob hit a ball, the hit BALL flew far after it was hit."
//                 trim 을 사용하지 않고 toLowerCase() 까지의 결과는 아래와 같다
//                 " bob hit a ball the hit ball flew far after it was hit "
//                 split(" ") 을 하게 되면 (이 부분은 아직 이해가 잘 안되는데)
//                 마지막 공백은 제거되고 앞 공백은 아래처럼 남는다
//                 [, bob, hit, a, ball, the, hit, ball, flew, far, after, it, was, hit]
//                 그래서 공백을 깔끔하게 모두 제거하기 위해
//                 split 을 하기 전에 trim 으로 앞 뒤 공백을 제거한다
//
//                 java 와 달리 kotlin 은
//                 trim 을 사용하지 않고 split(" ") 까지 했을때
//                 앞의 공백 뿐만 아니라 마지막 공백도 남는다
//                 [, bob, hit, a, ball, the, hit, ball, flew, far, after, it, was, hit, ]
                .trim()
                .split(" ");
        
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) map.put(word, map.getOrDefault(word, 0) + 1);
        for (String bannedWord : banned) map.remove(bannedWord);
        return map.keySet()
                .stream()
                .sorted((o1, o2) -> map.get(o2) - map.get(o1))
                .toList()
                .get(0);
    }
}
