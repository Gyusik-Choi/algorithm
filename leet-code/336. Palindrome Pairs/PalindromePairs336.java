package com.example;

import java.util.ArrayList;
import java.util.List;


public class PalindromePairs336 {
    /**
     * 팰린드롬 경우의 수 <br>
     * 1) 두 단어의 길이가 같은 경우 <br>
     * 2) 두 단어 중 비교하는 단어가 비교 대상 단어보다 짧은 경우 <br>
     * 3) 두 단어 중 비교하는 단어가 비교 대상 단어보다 긴 경우
     */
    public List<List<Integer>> palindromePairs(String[] words) {
        List<List<Integer>> result = new ArrayList<>();
        Trie trie = new Trie();
        for (int i = 0; i < words.length; i++) {
            trie.insert(words[i], i);
        }
        for (int i = 0; i < words.length; i++) {
            result.addAll(trie.search(words[i], i));
        }
        return result;
    }

    private static class TrieNode {
        private int wordId = -1;
        private final List<Integer> palindromeWordId = new ArrayList<>();
        private final TrieNode[] children = new TrieNode[26];
    }

    private static class Trie {
        private final TrieNode root = new TrieNode();

        private void insert(String word, int index) {
            TrieNode node = root;
            for (int i = word.length() - 1; i >= 0; i--) {
                char c = word.charAt(i);
                if (isPalindrome(word, 0, i)) node.palindromeWordId.add(index);
                if (node.children[c - 'a'] == null) node.children[c - 'a'] = new TrieNode();
                node = node.children[c - 'a'];
            }
            node.wordId = index;
        }

        private List<List<Integer>> search(String word, int index) {
            List<List<Integer>> result = new ArrayList<>();
            TrieNode node = root;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                // 3) 두 단어 중 비교하는 단어가 비교 대상 단어보다 긴 경우
                // palindromeWordId 리스트를 조회하는게 아닌
                // isPalindrome 함수를 통해 팰린드롬 여부를 조회한다
                // palindromeWordId 리스트에는 insert 에서 검사한 정보가 들어가있고
                // 여기는 새롭게 검사하는 단어다
                // insert 에서 단어를 역순으로 뒤집어서 검사했다면
                // 여기서는 원래 순서로 새롭게 검사하기 때문에
                // 기존 정보에서 조회할 수 없고 새로 팰린드롬 여부를 검사해야 한다
                if (node.wordId >= 0 && isPalindrome(word, i, word.length() - 1)) result.add(List.of(index, node.wordId));
                if (node.children[c - 'a'] == null) return result;
                node = node.children[c - 'a'];
            }
            // 1) 두 단어의 길이가 같은 경우
            if (node.wordId >= 0 && node.wordId != index) result.add(List.of(index, node.wordId));
            // 2) 두 단어 중 비교하는 단어가 비교 대상 단어보다 짧은 경우
            for (Integer id : node.palindromeWordId) result.add(List.of(index, id));
            return result;
        }

        private boolean isPalindrome(String word, int start, int end) {
            while (start < end) {
                if (word.charAt(start) != word.charAt(end)) return false;
                start += 1;
                end -= 1;
            }
            return true;
        }
    }
}
