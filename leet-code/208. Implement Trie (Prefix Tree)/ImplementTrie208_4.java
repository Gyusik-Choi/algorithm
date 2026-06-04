package com.example;

import java.util.HashMap;
import java.util.Map;

public class ImplementTrie208_4 {
    private final Node root = new Node('0');

    public void insert(String word) {
        Node cur = root;
        for (char w : word.toCharArray()) {
            if (!cur.children.containsKey(w)) {
                cur.children.put(w, new Node(w));
            }
            cur = cur.children.get(w);
        }
        cur.isWord = true;
        cur.word = word;
    }

    public boolean search(String word) {
        Node cur = root;
        for (char w : word.toCharArray()) {
            if (!cur.children.containsKey(w)) {
                return false;
            }
            cur = cur.children.get(w);
        }
        return cur.isWord;
    }

    public boolean startsWith(String prefix) {
        Node cur = root;
        for (char w : prefix.toCharArray()) {
            if (!cur.children.containsKey(w)) {
                return false;
            }
            cur = cur.children.get(w);
        }
        return true;
    }

    private static class Node {
        final Map<Character, Node> children = new HashMap<>();
        final char character;
        boolean isWord = false;
        String word = "";

        Node(char character) {
            this.character = character;
        }
    }
}
