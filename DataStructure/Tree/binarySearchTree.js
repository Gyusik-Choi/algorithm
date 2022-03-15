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

BinarySearchTree.prototype._search = function(cur, value) {
    if (cur.value > value) {
        if (cur.left === null) {
            return false;
        }
        return this._search(cur.left, value);
    } else {
        if (cur.right === null) {
            return false;
        }
        return this._search(cur.right, value);
    }
}

BinarySearchTree.prototype.add = function(value) {
    if (this.head.value === null) {
        this.head.value = value;
    } else {
        return this._add(this.head, value);
    }
}

BinarySearchTree.prototype._add = function(cur, value) {
    if (cur.value > value) {
        if (cur.left === null) {
            cur.left = new Node(value);
        } else {
            return this._add(cur.left, value);
        }
    } else {
        if (cur.right === null) {
            cur.right = new Node(value);
        } else {
            return this._add(cur.right, value);
        }
    }
}

BinarySearchTree.prototype.remove = function(value) {
    if (this.head.value === value) {
        if (this.head.left === null && this.head.right === null) {
            this.head = new Node(null);
        } else if (this.head.left !== null && this.head.right === null) {
            this.head = this.head.left;
        } else if (this.head.left === null && this.head.right !== null) {
            this.head = this.head.right;
        } else {
            const cur = this.findMostLeftNodeFromRightChild(this.head.right);
            this.head.value = cur.value;
            this._remove(this.head, this.head.right, this.head.value);
        }
    } else {
        if (this.head.value > value) {
            return this._remove(this.head, this.head.left, value);
        } else {
            return this._remove(this.head, this.head.right, value);
        }
    }
}

BinarySearchTree.prototype._remove = function(parent, cur, value) {
    if (cur === null) {
        return false;
    }

    if (cur.value === value) {
        if (cur.left === null && cur.right === null) {
            if (parent.left === cur) {
                parent.left = null;
            } else {
                parent.right = null;
            }
        } else if (cur.left !== null && cur.right === null) {
            cur = cur.left;
        } else if (this.head.left === null && this.head.right !== null) {
            cur = cur.right;
        } else {
            // 무조건 루트 노드가 기준이 아니라 (물론 루트 노드가 기준이 될 수도 있다)
            // 현재 노드를 기준으로 직계 오른쪽 자식 노드를 구성하는 트리에서 가장 왼쪽 노드를 찾는 것이다
            const node = this.findMostLeftNodeFromRightChild(cur.right);
            cur.value = node.value;
            // cur의 값은 cur의 오른쪽 자식 트리에서 가장 왼쪽 노드의 값으로 바꿨고
            // 이제 아까 찾은 오른쪽 자식 트리에서 가장 왼쪽 노드를 제거해야 한다
            this._remove(cur, cur.right, cur.value);
        }
    } else {
        if (cur.value > value) {
            return this._remove(cur, cur.left, value);
        } else {
            return this._remove(cur, cur.right, value);
        }
    }
}

BinarySearchTree.prototype.findMostLeftNodeFromRightChild = function(cur) {
    if (cur.left !== null) {
        return this.findMostLeftNodeFromRightChild(cur.left);
    }
    return cur;
}

BinarySearchTree.prototype.preOrder = function() {
    if (this.head.value === null) {
        return false;
    }
    return this._preOrder(this.head);
}

BinarySearchTree.prototype._preOrder = function(cur) {
    this.preOrderArr.push(cur.value);

    if (cur.left !== null) {
        this._preOrder(cur.left);
    }

    if (cur.right !== null) {
        this._preOrder(cur.right);
    }
}

BinarySearchTree.prototype.inOrder = function() {
    if (this.head.value === null) {
        return false;
    }
    return this._inOrder(this.head);
}

BinarySearchTree.prototype._inOrder = function(cur) {
    if (cur.left !== null) {
        this._inOrder(cur.left);
    }
    
    this.inOrderArr.push(cur.value);

    if (cur.right !== null) {
        this._inOrder(cur.right);
    }
}

BinarySearchTree.prototype.postOrder = function() {
    if (this.head.value === null) {
        return false;
    }
    return this._postOrder(this.head);
}

BinarySearchTree.prototype._postOrder = function(cur) {
    if (cur.left !== null) {
        this._postOrder(cur.left);
    }

    if (cur.right !== null) {
        this._postOrder(cur.right);
    }

    this.postOrderArr.push(cur.value);
}

const bst = new BinarySearchTree();
bst.add(10);
bst.add(5);
bst.add(15);
bst.add(3);
bst.add(7);
bst.add(13);
bst.add(17);
bst.add(1);
bst.add(4);
bst.add(6);
bst.add(9);
bst.add(11);
bst.add(14);
bst.add(16);
bst.add(19);
bst.remove(15);
bst.postOrder();
console.log(bst.postOrderArr);
