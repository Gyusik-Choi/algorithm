class Node {
  constructor(key, data=null) {
    this.key = key;
    this.data = data;
    this.children = {};
  }
}

class Trie {
  constructor() {
    this.head = new Node(null);
  }

  insert(word) {
    let cur = this.head;

    for (let i = 0; i < word.length; i++) {
      const char = word[i];

      if (!cur.children.hasOwnProperty(char)) {
        cur.children[char] = new Node(char);
      }
      cur = cur.children[char];
    }

    cur.data = word;
  }

  search(word) {
    let cur = this.head;

    for (let i = 0; i < word.length; i++) {
      const char = word[i];

      if (!cur.children.hasOwnProperty(char)) {
        return false;
      }

      cur = cur.children[char];
    }

    if (!cur.data) {
      return false;
    }

    return true;
  }

  startsWithPrefix(prefix) {
    let cur = this.head;
    const words = [];

    for (let i = 0; i < prefix.length; i++) {
      const char = prefix[i];

      if (!cur.children.hasOwnProperty(char)) {
        return [];
      }

      cur = cur.children[char];

      if (cur.data) {
        words.push(cur.data);
      }
    }

    this.findWords(cur, words);
    return words;
  }

  findWords(cur, words) {
    for (const [key, value] of Object.entries(cur.children)) {
      if (value.data) {
        words.push(value.data);

        if (Object.keys(value.children).length > 0) {
          this.findWords(value, words);
        }
      } else {
        this.findWords(value, words);
      }
    }

    return words;
  }
}

const trie = new Trie();
trie.insert('A');
trie.insert('ABC');
trie.insert('ABD');
trie.insert('BCD');
trie.insert('ABCD');
console.log(trie.search('ABC'));
console.log(trie.startsWithPrefix('A'));
