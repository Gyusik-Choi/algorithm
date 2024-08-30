public class DesignCircularQueue622 {
    private final int[] circularQ;
    private final int maxSize;
    private int front = 0;
    private int rear = 0;

    public DesignCircularQueue622(int k) {
        circularQ = new int[k];
        maxSize = k;
        // 문제의 요구사항 중 하나가 비었으면 -1을 리턴하는 것이라
        // 배열을 -1로 초기화한다
        // deQueue 로 제거해도 해당 인덱스를 -1로 변경한다
        for (int i = 0; i < maxSize; i++) {
            circularQ[i] = -1;
        }
    }

    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        // 비었으면 front, rear 모두 이동
        // 비었는데 rear 만 이동하면
        // front 는 계속 빈 값을 보고 있어서
        // Front() 로 조회하면 빈 값을 리턴하게 된다
        if (isEmpty()) {
            front = move(front);
        }
        rear = move(rear);
        circularQ[rear] = value;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        circularQ[front] = -1;
        // 비어있지 않으면 front 를 이동
        // 비어있어도 front 를 이동해도 되지만 이때는 rear 도 함께 이동해야 한다
        if (!isEmpty()) {
            front = move(front);
        }
        return true;
    }

    public int Front() {
        return circularQ[front];
    }

    public int Rear() {
        return circularQ[rear];
    }

    public boolean isEmpty() {
        return front == rear && circularQ[front] == -1;
    }

    public boolean isFull() {
        // 둘 중에 하나라도 -1이 아니면 인덱스가 1칸 차이라도 다 찬 상태가 아니다
        return (rear + 1) % maxSize == front && circularQ[front] != -1 && circularQ[rear] != -1;
    }

    public int move(int idx) {
        return (idx + 1) % maxSize;
    }
}
