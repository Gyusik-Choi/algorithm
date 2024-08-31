public class DesignCircularQueue622_2 {
    private final int[] circularQ;
    private final int maxSize;
    private int length = 0;
    private int front = 0;
    // 최초로 circularQ 에 요소를 넣을때
    // front 와 rear 가 같은 인덱스를 바라볼 수 있도록 한다
    private int rear = -1;

    public DesignCircularQueue622_2(int k) {
        circularQ = new int[k];
        maxSize = k;
    }

    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }

        rear = (rear + 1) % maxSize;
        circularQ[rear] = value;
        length += 1;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }

        front = (front + 1) % maxSize;
        length -= 1;
        return true;
    }

    public int Front() {
        return isEmpty() ? -1 : circularQ[front];
    }

    public int Rear() {
        return isEmpty() ? -1 : circularQ[rear];
    }

    public boolean isEmpty() {
        return length == 0;
    }

    public boolean isFull() {
        return length == maxSize;
    }
}
