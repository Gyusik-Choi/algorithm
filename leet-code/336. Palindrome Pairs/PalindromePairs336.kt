package com.example.algorithm

// 풀이 1)
class PalindromePairs336 {
    fun palindromePairs(words: Array<String>): List<List<Int>> {
        val reversedTrie = Trie('A')
        structureTrie(words, reversedTrie)
        return traverseTrie(words, reversedTrie)
    }

    private fun structureTrie(words: Array<String>, reversedTrie: Trie) {
        for (i in words.indices) {
            var node2 = reversedTrie
            val word2 = words[i].reversed()
            val word2Length = word2.length - 1
            for (j in word2.indices) {
                val w2 = word2[j]
                if (!node2.children.contains(w2)) {
                    node2.children[w2] = Trie(w2)
                }
                if (isPalindrome(word2, j, word2Length)) {
                    node2.palindromeInfo.add(i)
                }
                node2 = node2.children[w2]!!
            }
            node2.isWord = true
            node2.idx = i
        }
    }

    private fun isPalindrome(word: String, start: Int, end: Int): Boolean {
        var left = start
        var right = end
        while (left < right) {
            if (word[left] != word[right]) {
                return false
            }
            left += 1
            right -= 1
        }
        return true
    }

    private fun traverseTrie(words: Array<String>, reversedTrie: Trie): List<List<Int>> {
        val answer = mutableSetOf<List<Int>>()
        for (i in words.indices) {
            if (words[i].isEmpty()) {
                for (k in words.indices) {
                    if (k != i && isPalindrome(words[k], 0, words[k].length - 1)) {
                        answer.add(listOf(i, k))
                        answer.add(listOf(k, i))
                    }
                }
                continue
            }
            val word = words[i]
            var reversedNode = reversedTrie
            val first = word[0]
            if (!reversedNode.children.contains(first)) {
                continue
            }
            reversedNode = reversedNode.children[first]!!

            for (j in word.indices) {
                // 서로 동일
                if (j == word.lastIndex) {
                    if (reversedNode.isWord && i != reversedNode.idx) {
                        answer.add(listOf(i, reversedNode.idx))
                    }
                    // 탐색 대상 단어가 word 보다 더 긴 경우
                    if (reversedNode.palindromeInfo.isNotEmpty()) {
                        for (idx in reversedNode.palindromeInfo) {
                            answer.add(listOf(i, idx))
                        }
                    }
                    break
                }

                // 마지막 인덱스 아닌 경우
                if (reversedNode.isWord && isPalindrome(word, j + 1, word.length - 1)) {
                    answer.add(listOf(i, reversedNode.idx))
                }
                if (!reversedNode.children.contains(word[j + 1])) {
                    break
                }
                reversedNode = reversedNode.children[word[j + 1]]!!
            }
        }
        return answer.toList()
    }

    class Trie(value: Char) {
        var children = mutableMapOf<Char, Trie>()
        // 팰린드롬 인덱스 정보
        var palindromeInfo = mutableListOf<Int>()
        var isWord = false
        var idx = -1
    }
}

// 풀이 2) - 교재 참고
//class PalindromePairs336 {
//    fun palindromePairs(words: Array<String>): List<List<Int>> {
//        val reversedTrie = Trie('A')
//        structureTrie(words, reversedTrie)
//        return traverseTrie(words, reversedTrie)
//    }
//
//    private fun structureTrie(words: Array<String>, reversedTrie: Trie) {
//        for (i in words.indices) {
//            val word = words[i]
//            var node = reversedTrie
//
//            for (j in word.length - 1 downTo 0) {
//                val w = word[j]
//                if (!node.children.contains(w)) {
//                    node.children[w] = Trie(w)
//                }
//                if (isPalindrome(word, 0, j)) {
//                    node.palindromeInfo.add(i)
//                }
//                node = node.children[w]!!
//            }
//
//            node.isWord = true
//            node.idx = i
//        }
//    }
//
//    private fun isPalindrome(word: String, start: Int, end: Int): Boolean {
//        var left = start
//        var right = end
//        while (left < right) {
//            if (word[left] != word[right]) {
//                return false
//            }
//            left += 1
//            right -= 1
//        }
//        return true
//    }
//
//    private fun traverseTrie(words: Array<String>, reversedTrie: Trie): List<List<Int>> {
//        val answer = mutableSetOf<List<Int>>()
//        for (i in words.indices) {
//            if (words[i].isEmpty()) {
//                for (k in words.indices) {
//                    if (k != i && isPalindrome(words[k], 0, words[k].length - 1)) {
//                        answer.add(listOf(i, k))
//                        answer.add(listOf(k, i))
//                    }
//                }
//                continue
//            }
//
//            val word = words[i]
//            var reversedNode = reversedTrie
//            var isBreak = false
//
//            for (j in word.indices) {
//                // 마지막 인덱스 아닌 경우
//                if (reversedNode.isWord && isPalindrome(word, j, word.length - 1)) {
//                    answer.add(listOf(i, reversedNode.idx))
//                }
//                if (!reversedNode.children.contains(word[j])) {
//                    isBreak = true
//                    break
//                }
//                reversedNode = reversedNode.children[word[j]]!!
//            }
//
//            if (isBreak) {
//                continue
//            }
//            if (reversedNode.isWord && i != reversedNode.idx) {
//                answer.add(listOf(i, reversedNode.idx))
//            }
//            // 탐색 대상 단어가 word 보다 더 긴 경우
//            if (reversedNode.palindromeInfo.isNotEmpty()) {
//                for (idx in reversedNode.palindromeInfo) {
//                    answer.add(listOf(i, idx))
//                }
//            }
//        }
//        return answer.toList()
//    }
//
//    class Trie(value: Char) {
//        var children = mutableMapOf<Char, Trie>()
//        // 팰린드롬 인덱스 정보
//        var palindromeInfo = mutableListOf<Int>()
//        var isWord = false
//        var idx = -1
//    }
//}
