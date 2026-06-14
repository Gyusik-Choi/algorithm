package com.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PalindromePairs336_3 {
    /**
     * 기존에 isPalindrome 을 호출할때 substring 을 이용해서 문자열만 넘겼다
     * 그러나 이 부분에 의해서 시간 초과가 발생했다
     * substring 은 문자 배열을 복사하기 때문에 substring 이 아닌
     * 인덱스 정보를 함께 넘기는 방식으로 isPalindrome 을 변경하니 통과할 수 있었다
     */
    public List<List<Integer>> palindromePairs(String[] words) {
        Node reversedTrie = new Node();
        for (int i = 0; i < words.length; i++) {
            String reversedWord = reverseWord(words[i]);
            setUpTrie(reversedTrie, reversedWord, i);
        }

        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            if (word.isEmpty()) {
                // 빈 문자열이 있으면 나머지 문자 중에 자신이 팰린드롬인지 체크
                addPalindromePairsOfEmptyString(answer, words, i);
                continue;
            }
            addPalindromePairs(reversedTrie, word, answer, i);
        }
        return answer;
    }

    private void setUpTrie(Node t, String word, int idx) {
        char[] wArr = word.toCharArray();
        for (int i = 0; i < wArr.length; i++) {
            char w = wArr[i];
            if (!t.children.containsKey(w)) {
                t.children.put(w, new Node());
            }
            t = t.children.get(w);
            if (i == wArr.length - 1 || isPalindrome(word, i + 1, word.length() - 1)) {
                t.palindromeList.add(idx);
            }
        }
        t.wordIdxList.add(idx);
    }

    private void addPalindromePairs(Node t, String word, List<List<Integer>> answer, int idx) {
        for (int i = 0; i < word.length(); i++) {
            char w = word.charAt(i);
            if (!t.children.containsKey(w)) {
                return;
            }
            t = t.children.get(w);
            if (!t.wordIdxList.isEmpty() && i < word.length() - 1 && isPalindrome(word, i + 1, word.length() - 1)) {
                t.wordIdxList.forEach(j -> answer.add(List.of(idx, j)));
            }
        }
        for (int index : t.palindromeList) {
            if (idx != index) {
                answer.add(List.of(idx, index));
            }
        }
    }

    private void addPalindromePairsOfEmptyString(List<List<Integer>> answer, String[] words, int idx) {
        for (int i = 0; i < words.length; i++) {
            if (idx == i) {
                continue;
            }
            if (isPalindrome(words[i], 0, words[i].length() - 1)) {
                answer.add(List.of(idx, i));
                answer.add(List.of(i, idx));
            }
        }
    }

    private boolean isPalindrome(String word, int start, int end) {
        while (start < end) {
            if (word.charAt(start) != word.charAt(end)) {
                return false;
            }
            start += 1;
            end -= 1;
        }
        return true;
    }

    private String reverseWord(String word) {
        return new StringBuilder(word).reverse().toString();
    }

    private static class Node {
        // 트라이
        Map<Character, Node> children = new HashMap<>();
        // 현재 문자 뒤의 문자열이 팰린드롬인 idx
        List<Integer> palindromeList = new ArrayList<>();
        // 중복된 문자열이 있을 수 있어서 문자열의 인덱스 정보
        List<Integer> wordIdxList = new ArrayList<>();
    }
}

// 4)
//package com.example;
//
//import java.util.ArrayList;
//import java.util.HashMap;
//import java.util.List;
//import java.util.Map;
//
//public class PalindromePairs336_3 {
//    // 시간 초과 발생
//    public List<List<Integer>> palindromePairs(String[] words) {
//        // 내가 더 긴 경우는 나머지 본인의 문자열이 팰린드롬인지 확인하기
//        Node reversedTrie = new Node();
//        // [aa, a] [a, ab]
//        for (int i = 0; i < words.length; i++) {
//            String reversedWord = reverseWord(words[i]);
//            setUpTrie(reversedTrie, reversedWord, i);
//        }
//
//        List<List<Integer>> answer = new ArrayList<>();
//        for (int i = 0; i < words.length; i++) {
//            String word = words[i];
//            if (word.isEmpty()) {
//                // 빈 문자열이 있으면 나머지 문자 중에 문자 자신이 팰린드롬인지 체크
//                addPalindromePairsOfEmptyString(answer, words, i);
//                continue;
//            }
//            addPalindromePairs(reversedTrie, word, answer, i);
//        }
//        return answer;
//    }
//
//    private void setUpTrie(Node t, String word, int idx) {
//        char[] wArr = word.toCharArray();
//        for (int i = 0; i < wArr.length; i++) {
//            char w = wArr[i];
//            if (!t.children.containsKey(w)) {
//                t.children.put(w, new Node());
//            }
//            t = t.children.get(w);
//            if (i == wArr.length - 1 || isPalindrome(word.substring(i + 1))) {
//                t.palindromeMap.put(idx, true);
//            }
//        }
//        t.wordIdxList.add(idx);
//    }
//
//    private void addPalindromePairs(Node t, String word, List<List<Integer>> answer, int idx) {
//        boolean isBreak = false;
//        for (int i = 0; i < word.length(); i++) {
//            char w = word.charAt(i);
//            if (!t.children.containsKey(w)) {
//                isBreak = true;
//                break;
//            }
//            t = t.children.get(w);
//            if (!t.wordIdxList.isEmpty() && i < word.length() - 1 && isPalindrome(word.substring(i + 1))) {
//                t.wordIdxList.forEach(j -> answer.add(List.of(idx, j)));
//            }
//        }
//        if (isBreak) {
//            return;
//        }
//        for (Map.Entry<Integer, Boolean> entry : t.palindromeMap.entrySet()) {
//            if (entry.getKey() != idx && entry.getValue() == true) {
//                answer.add(List.of(idx, entry.getKey()));
//            }
//        }
//    }
//
//    private void addPalindromePairsOfEmptyString(List<List<Integer>> answer, String[] words, int idx) {
//        for (int i = 0; i < words.length; i++) {
//            if (idx == i) {
//                continue;
//            }
//            if (isPalindrome(words[i])) {
//                answer.add(List.of(idx, i));
//                answer.add(List.of(i, idx));
//            }
//        }
//    }
//
//    private boolean isPalindrome(String word) {
//        return word.contentEquals(reverseWord(word));
//    }
//
//    private String reverseWord(String word) {
//        return new StringBuilder(word).reverse().toString();
//    }
//
//    private static class Node {
//        // idx, 현재 문자 뒤의 문자열의 팰린드롬 여부
//        Map<Integer, Boolean> palindromeMap = new HashMap<>();
//        // 트라이
//        Map<Character, Node> children = new HashMap<>();
//        // 중복된 문자열이 있을 수 있어서 문자열의 인덱스 정보
//        List<Integer> wordIdxList = new ArrayList<>();
//    }
//}

// 3)
//package com.example;
//
//import java.util.ArrayList;
//import java.util.HashMap;
//import java.util.List;
//import java.util.Map;
//
//public class PalindromePairs336_3 {
//    public List<List<Integer>> palindromePairs(String[] words) {
//        Node trie = new Node();
//        for (int i = 0; i < words.length; i++) {
//            String word = reverseWord(words[i]);
//            Node t = trie;
//            char[] wArr = word.toCharArray();
//            for (int j = 0; j < wArr.length; j++) {
//                char w = wArr[j];
//                if (!t.children.containsKey(w)) {
//                    t.children.put(w, new Node());
//                }
//                t = t.children.get(w);
//                if (j == wArr.length - 1 || isPalindrome(word.substring(j + 1))) {
//                    t.palindromeMap.put(i, true);
//                }
//            }
//        }
//
//        List<List<Integer>> answer = new ArrayList<>();
//        for (int i = 0; i < words.length; i++) {
//            String word = words[i];
//            Node t = trie;
//            if (word.isEmpty()) {
//                // 빈 문자열이 있으면 나머지 문자 중에 문자 자신이 팰린드롬인지 체크
//                for (int k = 0; k < words.length; k++) {
//                    if (i == k) {
//                        continue;
//                    }
//                    if (isPalindrome(words[k])) {
//                        answer.add(List.of(i, k));
//                        answer.add(List.of(k, i));
//                    }
//                }
//            }
//            boolean isBreak = false;
//            for (char w : word.toCharArray()) {
//                if (!t.children.containsKey(w)) {
//                    isBreak = true;
//                    break;
//                }
//                t = t.children.get(w);
//            }
//            if (isBreak) {
//                continue;
//            }
//            for (Map.Entry<Integer, Boolean> entry : t.palindromeMap.entrySet()) {
//                if (entry.getKey() != i && entry.getValue() == true) {
//                    answer.add(List.of(i, entry.getKey()));
//                }
//            }
//        }
//        return answer;
//    }
//
//    private boolean isPalindrome(String word) {
//        return word.contentEquals(reverseWord(word));
//    }
//
//    private String reverseWord(String word) {
//        return new StringBuilder(word).reverse().toString();
//    }
//
//    private static class Node {
//        // idx, 현재 문자 뒤의 문자열의 팰린드롬 여부
//        Map<Integer, Boolean> palindromeMap = new HashMap<>();
//        Map<Character, Node> children = new HashMap<>();
//    }
//}

// 2)
//package com.example;
//
//import java.util.ArrayList;
//import java.util.HashMap;
//import java.util.List;
//import java.util.Map;
//
//public class PalindromePairs336_3 {
//    public List<List<Integer>> palindromePairs(String[] words) {
//        // ["sslll","lss"] -> [[1,2]]
//        // ["abcd","dcba","lls","s","sssll"] -> [[0,1],[1,0],[3,2],[2,4]]
//        //
//        // 각 문자열을 문자 역순으로 트라이에 넣기
//        // words 를 루프 돌면서 트라이의 (본인이 아닌 다른) 문자와 비교
//        //
//        // 트라이에 넣을때 각 문자 이후가 팰린드롬인지 체크
//        // 비교할때 길이가 짧거나 같은 문자에서 팰린드롬 여부를 검사하게 되고
//        // 길이가 더 긴 문자에서는 팰린드롬 여부를 확인하지 못한다
//        Node trie = new Node();
//        for (int i = 0; i < words.length; i++) {
//            String word = reverseWord(words[i]);
//            Node t = trie;
//            if (word.isEmpty()) {
//                for (int k = 0; k < 26; k++) {
//                    // 트라이.children.get((char) num) 구문에 의해
//                    // 계속 자식 노드로 타고 들어가지 않도록
//                    // 여기서 tr 변수가 루트를 보도록 새로 선언한다
//                    Node tr = trie;
//                    int num = k + 97;
//                    if (!tr.children.containsKey((char) num)) {
//                        tr.children.put((char) num, new Node());
//                    }
//                    tr = tr.children.get((char) num);
//                    tr.palindromeMap.put(i, true);
//                }
//                continue;
//            }
//            char[] wArr = word.toCharArray();
//            for (int j = 0; j < wArr.length; j++) {
//                char w = wArr[j];
//                if (!t.children.containsKey(w)) {
//                    t.children.put(w, new Node());
//                }
//                t = t.children.get(w);
//                if (j == wArr.length - 1 || isPalindrome(word.substring(j + 1))) {
//                    t.palindromeMap.put(i, true);
//                }
//            }
//        }
//
//        List<List<Integer>> answer = new ArrayList<>();
//        for (int i = 0; i < words.length; i++) {
//            String word = words[i];
//            Node t = trie;
//            if (word.isEmpty()) {
//                for (int k = 0; k < 26; k++) {
//                    Node tr = trie;
//                    int num = k + 97;
//                    if (!tr.children.containsKey((char) num)) {
//                        continue;
//                    }
//                    tr = tr.children.get((char) num);
//                    for (Map.Entry<Integer, Boolean> entry : tr.palindromeMap.entrySet()) {
//                        if (entry.getKey() != i && entry.getValue() == true) {
//                            answer.add(List.of(i, entry.getKey()));
//                        }
//                    }
//                }
//                continue;
//            }
//            boolean isBreak = false;
//            for (char w : word.toCharArray()) {
//                if (!t.children.containsKey(w)) {
//                    isBreak = true;
//                    break;
//                }
//                t = t.children.get(w);
//            }
//            if (isBreak) {
//                continue;
//            }
//            for (Map.Entry<Integer, Boolean> entry : t.palindromeMap.entrySet()) {
//                if (entry.getKey() != i && entry.getValue() == true) {
//                    answer.add(List.of(i, entry.getKey()));
//                }
//            }
//        }
//        return answer;
//    }
//
//    private boolean isPalindrome(String word) {
//        return word.contentEquals(reverseWord(word));
//    }
//
//    private String reverseWord(String word) {
//        return new StringBuilder(word).reverse().toString();
//    }
//
//    private static class Node {
//        // idx, isPalindromeNext
//        Map<Integer, Boolean> palindromeMap = new HashMap<>();
//        Map<Character, Node> children = new HashMap<>();
//    }
//}

// 1)
//package com.example;
//
//import java.util.ArrayList;
//import java.util.HashMap;
//import java.util.List;
//import java.util.Map;
//
//public class PalindromePairs336_3 {
//    public List<List<Integer>> palindromePairs(String[] words) {
//        // ["sslll","lss"] -> [[1,2]]
//        // ["abcd","dcba","lls","s","sssll"] -> [[0,1],[1,0],[3,2],[2,4]]
//        //
//        // 각 문자열을 문자 역순으로 트라이에 넣기
//        // words 를 루프 돌면서 트라이의 (본인이 아닌 다른) 문자와 비교
//        //
//        // 트라이에 넣을때 각 문자 이후가 팰린드롬인지 체크
//        // 비교할때 길이가 짧거나 같은 문자에서 팰린드롬 여부를 검사하게 되고
//        // 길이가 더 긴 문자에서는 팰린드롬 여부를 확인하지 못한다
//        Node trie = new Node();
//        for (int i = 0; i < words.length; i++) {
//            String word = reverseWord(words[i]);
//            Node t = trie;
//            char[] wArr = word.toCharArray();
//            for (int j = 0; j < wArr.length; j++) {
//                char w = wArr[j];
//                if (!t.children.containsKey(w)) {
//                    t.children.put(w, new Node());
//                }
//                t = t.children.get(w);
//                if (j == wArr.length - 1) {
//                    t.isPalindromeNext = true;
//                } else {
//                    if (isPalindrome(word.substring(j + 1))) {
//                        t.isPalindromeNext = true;
//                    }
//                }
//            }
//            t.word = word;
//            t.idx = i;
//        }
//
//        List<List<Integer>> answer = new ArrayList<>();
//        for (int i = 0; i < words.length; i++) {
//            String word = words[i];
//            Node t = trie;
//            boolean isBreak = false;
//            for (char w : word.toCharArray()) {
//                if (!t.children.containsKey(w)) {
//                    isBreak = true;
//                    break;
//                }
//                t = t.children.get(w);
//            }
//            if (isBreak) {
//                continue;
//            }
//            if (t.isPalindromeNext && t.idx != -1 && t.idx != i) {
//                answer.add(List.of(i, t.idx));
//            }
//        }
//        return answer;
//    }
//
//    private boolean isPalindrome(String word) {
//        return word.contentEquals(reverseWord(word));
//    }
//
//    private String reverseWord(String word) {
//        return new StringBuilder(word).reverse().toString();
//    }
//
//    private static class Node {
//        char character;
//        boolean isPalindromeNext = false;
//        String word;
//        int idx = -1;
//        Map<Character, Node> children = new HashMap<>();
//
//        Node() {
//        }
//
//        Node(char c) {
//            character = c;
//        }
//    }
//}
