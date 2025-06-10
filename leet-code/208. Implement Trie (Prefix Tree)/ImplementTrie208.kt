package com.example

import kotlin.text.iterator

class ImplementTrie208 {
    val root = Node('\n')

    fun insert(word: String) {
        var head = root
        for (w in word) {
            if (!head.children.containsKey(w)) {
                head.children[w] = Node(w)
            }
            head = head.children[w]!!
        }
        head.isWord = true
    }

    fun search(word: String): Boolean {
        var head = root
        for (w in word) {
            if (!head.children.containsKey(w)) {
                return false
            }
            head = head.children[w]!!
        }
        return head.isWord
    }

    fun startsWith(prefix: String): Boolean {
        var head = root
        for (p in prefix) {
            if (!head.children.containsKey(p)) {
                return false
            }
            head = head.children[p]!!
        }
        return true
    }

    class Node(val character: Char) {
        var isWord = false
        val children: MutableMap<Char, Node> = mutableMapOf()
    }
}
