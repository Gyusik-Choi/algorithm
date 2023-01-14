class Node {
  String? key;
  String? data;
  Map<String, Node> children = {};

  // https://www.bezkoder.com/dart-flutter-constructors/
  Node(this.key, [this.data]);
}

class Trie {
  Node head = Node(null);

  void insert(String word) {
    Node node = head;

    for (int i = 0; i < word.length; i++) {
      String char = word[i];

      if (!node.children.containsKey(char)) {
        node.children[char] = Node(char);
      }

      node = node.children[char]!;
    }

    node.data = word;
  }

  bool exist(String word) {
    Node node = head;

    for (int i = 0; i < word.length; i++) {
      String char = word[i];

      if (!node.children.containsKey(char)) {
        return false;
      }

      node = node.children[char]!;
    }

    if (node.data == null) {
      return false;
    }

    return true;
  }

  List startWithPrefix(String prefix) {
    Node node = head;

    for (int i = 0; i < prefix.length; i++) {
      String p = prefix[i];

      if (!node.children.containsKey(p)) {
        return [];
      }

      node = node.children[p]!;
    }

    List<String> words = <String>[];

    if (node.data != null) {
      words.add(node.data!);
    }

    return searchWordStartWithPrefix(node, words);
  }

  List<String> searchWordStartWithPrefix(Node node, List<String> words) {
    // https://www.codevscolor.com/dart-iterate-map
    for (MapEntry e in node.children.entries) {
      String k = e.key;
      Node n = e.value;

      if (n.data != null) {
        words.add(n.data!);

        // https://api.flutter.dev/flutter/dart-collection/LinkedHashMap-class.html
        // ABC 이후에 ABCD 도 탐색하기 위한 로직
        if (n.children.isNotEmpty) {
          searchWordStartWithPrefix(n, words);
        }
      } else {
        searchWordStartWithPrefix(node.children[k]!, words);
      }
    }

    return words;
  }
}

void main() {
  Trie trie = Trie();
  trie.insert('A');
  trie.insert('ABC');
  trie.insert('ABD');
  trie.insert('BCD');
  trie.insert('CDE');
  trie.insert('ABCD');
  print(trie.startWithPrefix('A'));
}