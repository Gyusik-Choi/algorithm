package com.example;

public class ImplementTrie208 {

    private TrieNode root;

    public ImplementTrie208() {
        this.root = new TrieNode(null);
    }

    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 97;
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode(Character.toString(c));
            }
            node = node.children[idx];
        }
        node.word = word;
    }

    public boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 97;
            if (node.children[idx] == null) {
                return false;
            }
            node = node.children[idx];
        }

        if (node.word == null) return false;
        return node.word.equals(word);
    }

    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            int idx = c - 97;
            if (node.children[idx] == null) {
                return false;
            }
            node = node.children[idx];
        }
        return true;
    }

    private static class TrieNode {
        private final String character;
        private String word;
        private TrieNode[] children;

        TrieNode(String character) {
            this.character = character;
            this.word = null;
            this.children = new TrieNode[26];
        }

        TrieNode(String character, String word) {
            this.character = character;
            this.word = word;
            this.children = new TrieNode[26];
        }
    }
}
