class Node {
  int? value;
  Node? next;

  Node(this.value);
}

class LinkedList {
  late Node head;
  late Node tail;
  int length = 0;

  LinkedList() {
    head = Node(null);
    tail = head;
  }

  bool isEmtpy() {
    if (head.value == null) {
      return true;
    }

    return false;
  }

  void add(int value) {
    // if (head.value == null && tail.value == null) {
    if (length == 0) {
      head = Node(value);
      tail = head;
    } else {
      Node currentTail = tail;
      tail = Node(value);
      currentTail.next = tail;
    }

    length += 1;
  }

  bool remove(int index) {
    if (index >= length) {
      print('wrong index');
      return false;
    }

    if (index == 0) {
      if (length == 1) {
        head = Node(null);
        tail = head;
      } else {
        head = head.next!;
      }
    } else {
      int idx = 0;
      Node currentNode = head;

      while (idx < index - 1) {
        currentNode = currentNode.next!;
        idx += 1;
      }

      currentNode.next = currentNode.next!.next;

      if (currentNode.next == null) {
        tail = currentNode;
      }
    }

    length -= 1;
    return true;
  }

  void printLinkedList() {
    Node? currentNode = head;
    int idx = 0;

    while (idx < length) {
      print(currentNode!.value);
      currentNode = currentNode.next;
      idx += 1;
    }
  }

  void reverse() {
    if (length > 1) {
      Node? prevNode = null;
      Node? currentNode = head;
      tail = currentNode;

      while (currentNode != null) {
        Node? nextNode = currentNode.next;
        currentNode.next = prevNode;
        prevNode = currentNode;
        currentNode = nextNode;
      }

      head = prevNode!;
    }
  }
}

void main() {
  LinkedList linkedList = LinkedList();
  linkedList.add(1);
  linkedList.add(2);
  linkedList.add(3);
  linkedList.add(4);
  linkedList.add(5);
  
  linkedList.reverse();
  linkedList.printLinkedList();
}