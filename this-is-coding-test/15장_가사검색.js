class Node {
  constructor(data = null) {
    this.data = data;
    this.len = 0;
    this.children = {};
  }
}

class Trie {
  constructor() {
    this.head = new Node();
  }

  insert(word) {
    let node = this.head;
    node.len += 1;

    for (const w of word) {
      if (!node.children.hasOwnProperty(w)) {
        node.children[w] = new Node();
      }

      node = node.children[w];
      node.len += 1;
    }

    node.data = word;
  }

  startWithPrefix(prefix) {
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

    return node.len;
  }
}

const reverseWord = (word) => {
  let reversedWord = '';

  for (const w of word) {
    reversedWord = w + reversedWord;
  }

  return reverseWord;
}

const solution = (words, queries) => {
  const tries = {};
  const reversedTries = {};

  // const trie = new Trie();
  // const reversedTrie = new Trie();

  words.forEach(word => {
    const wordLength = word.length;

    if (!tries.hasOwnProperty(wordLength.toString())) {
      tries[wordLength] = new Trie();
    }

    tries[wordLength].insert(word)

    const reversedWord = word.split('').reverse().join('');

    if (!reversedTries.hasOwnProperty(wordLength.toString())) {
      reversedTries[wordLength] = new Trie();
    }

    reversedTries[wordLength].insert(reversedWord);
  });

  return queries.map(query => {
    const queryLength = query.length;

    if (query[0] === "?") {
      if (!reversedTries.hasOwnProperty(queryLength)) {
        return 0;
      }

      return reversedTries[queryLength].startWithPrefix(query.split('').reverse().join(''));
    }
    
    if (!tries.hasOwnProperty(queryLength)) {
      return 0;
    }

    return tries[queryLength].startWithPrefix(query);
  });
}
