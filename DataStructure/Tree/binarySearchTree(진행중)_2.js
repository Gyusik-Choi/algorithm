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
    if (this.head.value === value) {
        return true;
    }
    return this._search(this.head, value);
}

BinarySearchTree.prototype._search = function(head, value) {
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
    if (this.head.value === null) {
        this.head.value = value;
    } else {
        return this._add(this.head, value);
    }
}

BinarySearchTree.prototype._add = function(head, value) {
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

BinarySearchTree.prototype.remove = function(value) {
    if (this.head.value === value) {
        if (this.head.left === null && this.head.right === null) {
            this.head = new Node(null);
        } else if (this.head.left !== null && this.head.right === null) {

        } else if (this.head.left === null && this.head.right !== null) {

        } else {

        }
    } else {
    ]   this._remove(this.head, value);
    }
}

BinarySearchTree.prototype._remove = function(head, value) {

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
