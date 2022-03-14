const Node = function(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
}

const BinarySearchTree = function() {
    this.head = new Node(null);

    this.preOrderArr = [];
    this.inOrderArr = [];
    this.postOrderArr = [];
}

BinarySearchTree.prototype.search = function(value) {
    return this._search(this.head, value);
}

BinarySearchTree.prototype._search = function(head, value) {
    if (head.value === value) {
        return true;
    }

    if (head.value > value) {
        if (head.left === null) {
            return false;
        }
        return this._search(head.left, value);
    } else {
        if (head.right === null) {
            return false;
        }
        return this._search(head.right, value);
    }
}

BinarySearchTree.prototype.add = function(value) {
    return this._add(this.head, value);
}

BinarySearchTree.prototype._add = function(head, value) {
    console.log(this.head === head);
    console.log(this.head);
    console.log(head);
    // if (head.value === null) {
    //     head = new Node(value);
    if (this.head.value === null) {
        this.head = new Node(value);
    } else {
        // 위의 this.head와 아래의 head는 다르다
        // this.head는 BinarySearchTree의 루트 노드다
        // 아래의 head는 this.head 밑에 있는 자식 노드다
        // console.log(this);
        // console.log(head);
        // console.log(value);
        // console.log('-----');
        if (head.value > value) {
            if (head.left === null) {
                head.left = new Node(value);
            } else {
                return this._add(head.left, value);
            }
        } else {
            if (head.right === null) {
                head.right = new Node(value);
            } else {
                return this._add(head.right, value);
            }
        }
    }
    console.log(this.head === head);
    console.log(this.head);
    console.log(head);
    // console.log(head);
    // console.log(this.head);
    // console.log(this);
    console.log('-----');
}

BinarySearchTree.prototype.remove = function() {

}

BinarySearchTree.prototype.preOrder = function() {

}

BinarySearchTree.prototype.inOrder = function() {
    
}

BinarySearchTree.prototype.postOrder = function() {
    
}

const bst = new BinarySearchTree();
bst.add(5);
bst.add(3);
bst.add(7);
bst.add(1);
bst.add(6);
console.log(bst);
