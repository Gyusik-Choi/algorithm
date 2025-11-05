package com.example;

import java.util.HashMap;
import java.util.Map;

public class ImplementTrie208_3 {
    private final Node root = new Node('A');

    public ImplementTrie208_3() {

    }

    public void insert(String word) {
        Node node = root;
        for (char ch : word.toCharArray()) {
            if (!node.next.containsKey(ch)) {
                node.next.put(ch, new Node(ch));
            }
            node = node.next.get(ch);
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        Node node = root;
        for (char ch : word.toCharArray()) {
            if (!node.next.containsKey(ch)) {
                return false;
            }
            node = node.next.get(ch);
        }
        return node.isEnd;
    }

    public boolean startsWith(String prefix) {
        Node node = root;
        for (char ch : prefix.toCharArray()) {
            if (!node.next.containsKey(ch)) {
                return false;
            }
            node = node.next.get(ch);
        }
        return true;
    }

    static class Node {
        char value;
        boolean isEnd = false;
        Map<Character, Node> next = new HashMap<>();

        Node(char value) {
            this.value = value;
        }
    }
}
