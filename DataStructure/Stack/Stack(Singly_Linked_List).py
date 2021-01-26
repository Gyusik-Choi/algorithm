class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            print(self.head.val)
            return self.head.val

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def subtraction(self):
        if self.is_empty():
            print("Nothing to remove")
            return
        else:
            node_to_remove = self.head.val
            self.head = self.head.next
            return node_to_remove

    def __str__(self):
        stack_arr = "["
        cur = self.head
        while cur:
            stack_arr += str(cur.val) + ", "
            cur = cur.next
        stack_arr = stack_arr.rstrip(", ")
        stack_arr += "]"
        return stack_arr


st = Stack()
st.add(1)
st.add(2)
st.add(3)
st.add(4)
st.add(5)
st.subtraction()
st.subtraction()
st.peek()
print(st)

# 참고
# https://daimhada.tistory.com/105
# https://wayhome25.github.io/cs/2017/04/18/cs-20/
# https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9D
