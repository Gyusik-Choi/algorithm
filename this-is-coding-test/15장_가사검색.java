import java.util.HashMap;

class Solution {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] answer = solution.solution(
            new String[]{"frodo", "front", "frost", "frozen", "frame", "kakao"},
            new String[]{"fro??", "????o", "fr???", "fro???", "pro?", "?????"}
        );

        for (int j : answer) {
            System.out.println(j);
        }
    }

    public int[] solution(String[] words, String[] queries) {
        int[] answer = new int[queries.length];

        Trie trie = new Trie();
        Trie reversedTrie = new Trie();

        for (String word: words) {
            trie.add(word);
            reversedTrie.add(reverse(word));
        }

        for (int i = 0; i < queries.length; i++) {
            String query = queries[i];

            if (query.charAt(0) == '?') {
                answer[i] = reversedTrie.searchWithPrefix(reverse(query));
            } else {
                answer[i] = trie.searchWithPrefix(query);
            }
        }

        return answer;
    }

    String reverse(String word) {
        return new StringBuilder(word).reverse().toString();
//        효율성 3, 4번이 시간 초과가 발생 했는데
//        문자열 뒤집는 아래의 코드를 위의 코드로 변경해서
//        효율성 4번을 통과할 수 있었다
//        그러나 효율성 3번은 시간 초과가 발생 했다
//        String reversedWord = "";
//
//        for (int i = 0; i < word.length(); i++) {
//            reversedWord = word.charAt(i) + reversedWord;
//        }
    }
}

class Node {
    char oneLetter;

    HashMap<Integer, Integer> cnt = new HashMap<Integer, Integer>();
//     글자수를 배열에 넣는 방식에서
//     글자수 마다 갯수를 세는 방식으로 바꿨다
//     글자수를 배열에 넣는 방식은
//     추후에 동일한 값을 전체 배열을 돌면서 세야 해서 효율적이지 못했다
//     HashMap 을 통해 동일한 글자수의 갯수가 몇 개 인지 빠르게 찾을 수 있다
//     이를 통해 효율성 3번을 통과할 수 있었다
//    ArrayList<Integer> cnt = new ArrayList<Integer>();

    HashMap<Character, Node> children = new HashMap<Character, Node>();

    Node(char oneLetter) {
        this.oneLetter = oneLetter;
    }
}

class Trie {
    Node head;

    Trie() {
        head = new Node('*');
    }

    void add(String word) {
        Node cur = head;
        int len = word.length();
        cur.cnt.put(len, cur.cnt.getOrDefault(len, 0) + 1);

        for (int i = 0; i < word.length(); i++) {
            char w = word.charAt(i);

            if (!cur.children.containsKey(w)) {
                cur.children.put(w, new Node(w));
            }

            cur = cur.children.get(w);
            cur.cnt.put(len, cur.cnt.getOrDefault(len, 0) + 1);
        }
    }

    int searchWithPrefix(String prefix) {
        Node cur = head;
        int len = prefix.length();

        if (prefix.charAt(prefix.length() - 1) == '?') {
            for (int i = 0; i < prefix.length(); i++) {
                char p = prefix.charAt(i);

                if (p == '?') {
                    return cur.cnt.getOrDefault(len, 0);
                }

                if (!cur.children.containsKey(p)) {
                    return 0;
                }

                cur = cur.children.get(p);
            }
        }

        return cur.cnt.getOrDefault(len, 0);
    }

//    int searchWithPrefix(String prefix) {
//        Node cur = head;
//
//        for (int i = 0; i < prefix.length(); i++) {
//            char p = prefix.charAt(i);
//
//            // 처음부터 안 맞는게 아니라
//            // 중간에 p 가 안 맞을 수도 있다
//            // 그러면 현재 상황은 cur 에서 값을 조회 하므로
//            // 오답이 발생할 수 있다
//            // 조회 자체를 막고 0을 리턴해야 한다
//            if (p != '?' && cur.children.containsKey(p)) {
//                cur = cur.children.get(p);
//            } else {
//                break;
//            }
//        }
//
//        return (int) cur.cnt.stream()
//            .filter(c -> c == prefix.length())
//            .count();
//    }
}

// 참고
// https://girawhale.tistory.com/110
