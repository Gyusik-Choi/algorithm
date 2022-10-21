const Node = function(word = null, char = null) {
    this.word = word;
    this.char = char;
    this.children = {};
}

const Trie = function() {
    // this.head = Node();
    // dart 와 혼동하지 말자...!
    this.head = new Node();
}

Trie.prototype.search = function(word) {
    let head = this.head;

    for (let i = 0; i < word.length; i++) {
        const char = word[i];

        if (head.children.hasOwnProperty(char)) {
            head = head.children[char];
        } else {
            return false;
        }
    }

    if (head.word === null) {
        return false;
    }
    
    return true;
}

Trie.prototype.insert = function(word) {
    let head = this.head;

    for (let i = 0; i < word.length; i++) {
        const char = word[i];

        if (head.children.hasOwnProperty(char) === false) {
            head.children[char] = new Node(null, char);
        }

        head = head.children[char];
    }

    head.word = word;
    return true;
}

Trie.prototype.startsWith = function(prefix) {
    let head = this.head;

    for (let i = 0; i < prefix.length; i++) {
        const p = prefix[i];

        if (head.children.hasOwnProperty(p)) {
            head = head.children[p];

        } else {
            return false;
        }
    }

    let wordsStartsWithPrefix = [];
    const words = head.children;
    
    // https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty
    for (const [key, value] of Object.entries(words)) {
        const foundWords = this.dfs(value, []);
        wordsStartsWithPrefix.push(foundWords);
    }

    return wordsStartsWithPrefix;
}

Trie.prototype.dfs = function(obj, foundWords) {
    if (obj.word) {
        foundWords.push(obj.word)
        return foundWords;
    }

    const words = obj.children;
    for (const [key, value] of Object.entries(words)) {
        this.dfs(value, foundWords);
    }

    return foundWords;
}

const trie = new Trie();
trie.insert('ABC');
trie.insert('ABD');
trie.insert('BCD');
trie.search('ABC');
console.log(trie.startsWith('A'));
