package com.example;

import java.util.ArrayList;
import java.util.List;

public class PalindromePairs336_2 {
    public List<List<Integer>> palindromePairs(String[] words) {
        Trie trie = new Trie();
        for (int i = 0; i < words.length; i++) {
            trie.insert(i, words[i]);
        }
        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            answer.addAll(trie.search(i, words[i]));
        }
        return answer;
    }

    private static class TrieNode {
        int wordId;
        TrieNode[] children;
        List<Integer> palindromeWordIds;

        TrieNode() {
            wordId = -1;
            children = new TrieNode[26];
            palindromeWordIds = new ArrayList<>();
        }
    }

    private static class Trie {
        TrieNode root;

        Trie() {
            root = new TrieNode();
        }

        public boolean isPalindrome(String word, int start, int end) {
            while (start < end) {
                if (word.charAt(start) != word.charAt(end)) {
                    return false;
                }
                start += 1;
                end -= 1;
            }
            return true;
        }

        public void insert(int wordIdx, String word) {
            TrieNode cur = root;
            for (int i = word.length() - 1; i > -1; i--) {
                if (isPalindrome(word, 0, i)) {
                    cur.palindromeWordIds.add(wordIdx);
                }
                int idx = word.charAt(i) - 'a';
                if (cur.children[idx] == null) {
                    cur.children[idx] = new TrieNode();
                }
                cur = cur.children[idx];
            }
            cur.wordId = wordIdx;
        }

        public List<List<Integer>> search(int wordIdx, String word) {
            TrieNode cur = root;
            List<List<Integer>> list = new ArrayList<>();

            for (int i = 0; i < word.length(); i++) {
                if (cur.wordId >= 0 && isPalindrome(word, i, word.length() - 1)) {
                    list.add(List.of(wordIdx, cur.wordId));
                }
                int idx = word.charAt(i) - 'a';
                if (cur.children[idx] == null) {
                    return list;
                }
                cur = cur.children[idx];
            }

            if (cur.wordId >= 0 && cur.wordId != wordIdx) {
                list.add(List.of(wordIdx, cur.wordId));
            }

            for (int wordId : cur.palindromeWordIds) {
                list.add(List.of(wordIdx, wordId));
            }

            return list;
        }
    }
}
