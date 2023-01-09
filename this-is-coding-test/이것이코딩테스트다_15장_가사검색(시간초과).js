class Node {
  constructor(data = null) {
    this.data = data;
    this.len = [];
    this.children = {};
  }
}

class Trie {
  constructor() {
    this.head = new Node();
  }

  insert(word) {
    let node = this.head;

    for (const w of word) {
      if (!node.children.hasOwnProperty(w)) {
        node.children[w] = new Node();
      }

      node.len.push(word.length);
      node = node.children[w];
    }

    node.data = word;
  }

  startWithPrefix(prefix, qLength) {
    let node = this.head;
    
    for (const p of prefix) {
      if (p === "?") {
        break;
      }

      if (!node.children.hasOwnProperty(p)) {
        return 0;
      }

      node = node.children[p];
    }

    return node.len.filter(v => v === qLength).length;
  }
}

const solution = (words, queries) => {
  const trie = new Trie();
  const reversedTrie = new Trie();

  words.forEach(word => trie.insert(word));
  words.map(word => word.split('').reverse().join('')).forEach(w => reversedTrie.insert(w));

  return queries.map(query => {
    const queryLength = query.length;

    if (query[0] === "?") {
      return reversedTrie.startWithPrefix(query.split('').reverse().join(''), queryLength);
    }

    return trie.startWithPrefix(query, queryLength);
  });
}

console.log(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]));
console.log(solution(["pro"], ["pro?"]));
// => [0]
console.log(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["?????"]));
// => [5]
