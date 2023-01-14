class Node {
  constructor(char, data = null) {
    this.char = char;
    this.data = data;
    this.children = {};
  }
}

class Trie {
  constructor() {
    this.head = new Node(null);
  }

  insert(word) {
    let node = this.head;
    
    for (const w of word) {
      if (!node.children.hasOwnProperty(w)) {
        node.children[w] = new Node(w);
      }

      node = node.children[w];
    }

    node.data = word;
  }

  search(word) {
    let node = this.head;

    for (const w of word) {
      if (!node.children.hasOwnProperty(w)) {
        return false;
      }

      node = node.children[w];
    }

    if (!node.data) {
      return false;
    }

    return true;
  }

  startsWithPrefix(prefix) {
    let node = this.head;

    for (const p of prefix) {
      if (!node.children.hasOwnProperty(p)) {
        return [];
      }

      node = node.children[p];
    }

    const words = [];

    if (node.data) {
      words.push(node.data);
    }

    return this.#_findWordsStartWithPrefix(node, words);
  }

  #_findWordsStartWithPrefix(n, words) {
    const node = n;

    for (const [key, value] of Object.entries(node.children)) {
      if (value.data) {
        words.push(value.data);

        // https://ipex.tistory.com/130
        // ABC 이후에 ABCD 도 탐색하려면
        // value 의 children 존재 여부를 검사해서
        // 존재하면 _findWordsStartWithPrefix 를 value 에 대해서 수행해야 한다
        if (Object.keys(value.children).length > 0) {
          this.#_findWordsStartWithPrefix(value, words);
        }

        continue;
      }
        
      this.#_findWordsStartWithPrefix(value, words);
    }

    return words;
  }
}

const trie = new Trie();
trie.insert('A');
trie.insert('ABC');
trie.insert('ABD');
trie.insert('BCD');
trie.insert('CDE');
trie.insert('ABCD');
console.log(trie.head);
console.log(trie.search('ABC'));
console.log(trie.startsWithPrefix('A'));