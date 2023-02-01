class Node {
  constructor(value = null, next = null) {
    this.value = value;
    this.next = next;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = new Node();
  }

  add(value) {
    let node = this.head;

    if (node.value === null) {
      this.head = new Node(value);
      return;
    }

    while (node.next !== null) {
      node = node.next;
    } 

    node.next = new Node(value);
  }

  addFirst(value) {
    let node = this.head;
    
    this.head = new Node(value);
    
    if (node.next !== null) {
      this.head.next = node;
    }
  }

  addByIdx(idx, value) {
    if (idx < 0) {
      return;
    }

    if (idx === 0) {
      return this.addFirst(value);
    }

    let node = this.head;
    let i = 1;

    while (i < idx) {
      if (node.next === null) {
        return;
      }

      node = node.next;
      i += 1;
    }

    if (node.next === null) {
      return this.addLast(value);
    }

    const nextNode = node.next;
    const newNextNode = new Node(value)

    node.next = newNextNode;
    newNextNode.next = nextNode;
  }

  addLast(value) {
    let node = this.head;

    while (node.next !== null) {
      node = node.next;
    }

    node.next = new Node(value);
  }

  remove() {
    let node = this.head;

    if (node.value === null) {
      return;
    }

    while (node.next !== null) {
      node = node.next;
    }

    node.next = null;
  }

  removeFirst() {
    let node = this.head;

    // 삭제할 노드가 없음
    if (node.value === null) {
      return;
    }

    const nextNode = node.next;
    this.head = nextNode;
  }

  removeByIdx(idx) {
    if (idx < 0) {
      return;
    }

    if (idx === 0) {
      return this.removeFirst();
    }
    
    // 해당 노드의 다음 노드를 삭제한다
    let node = this.head;
    let i = 1;

    while (i < idx) {
      if (node.next === null) {
        return;
      }

      node = node.next;
      i += 1;
    }
    
    // 총 노드 숫자 - 1 보다 큰 idx 가 넘어온거라
    // 삭제할 노드가 없다
    if (node.next === null) {
      return;
    }

    if (node.next.next === null) {
      return this.removeLast();
    }

    const newNextNode = node.next.next;
    node.next = newNextNode;
  }

  removeLast() {
    let node = this.head;

    if (node.next === null) {
      this.head = new Node();
    }
    
    while (node.next.next !== null) {
      node = node.next;
    }

    node.next = null;
  }

  reverse() {
    let node = this.head;
    let prev = null;

    // 총 노드가 0개 혹은 1개라 뒤집을 노드가 없음
    if (node.next === null) {
      return;
    }

    while (node) {
      const nextNode = node.next;
      node.next = prev;
      prev = node;
      node = nextNode;
    }

    this.head = prev;
  }

  getNodeList() {
    const nodes = [];
    
    let node = this.head;

    if (node.value === null) {
      return nodes;
    }

    while (node.next !== null) {
      nodes.push(node.value);
      node = node.next;
    }
    
    // 마지막에 남은 노드를 nodes 에 넣어준다
    nodes.push(node.value);
    return nodes;
  }
}

const singlyLinkedList = new SinglyLinkedList();
singlyLinkedList.add(1);
singlyLinkedList.add(2);
singlyLinkedList.add(3);
singlyLinkedList.add(4);
singlyLinkedList.add(5);
singlyLinkedList.addFirst(0);
singlyLinkedList.addLast(6);
singlyLinkedList.removeFirst();
singlyLinkedList.removeLast();
singlyLinkedList.removeByIdx(0);
singlyLinkedList.reverse();
console.log(singlyLinkedList.getNodeList());
