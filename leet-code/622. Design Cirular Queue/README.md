

# LeetCode

## [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

### Python

[파이썬 알고리즘 인터뷰](https://www.yes24.com/Product/Goods/91084402) 교재의 풀이 방식을 참고했다.

<br>

#### 장점

장점은 원형큐의 모든 인덱스에 요소를 채울 수 있다는 점이다.

원형큐 구현하는 다른 방식들을 보면 인덱스 하나를 비워두는 경우를 많이 보았는데 이 풀이는 그렇지 않다.

<br>

#### en_queue

인덱스 하나를 비워두는 구현의 경우 시작점을 비워둔 채로 enQueue 를 진행한다.

즉 end 를 한칸 이동하고 그 위치에 요소를 넣는데, 이 풀이는 end 현재 위치에 요소를 넣은 후에 end 를 한칸 이동한다.

<br>

#### de_queue

start 인덱스에 값이 None 이면 꺼낼 요소가 없기 때문에 False 를 리턴한다.

start 인덱스에 값이 None 이 아니면 해당 인덱스를 None 으로 바꾸고 True 를 리턴한다.

<br>

### front

큐가 비었으면 -1을 리턴하고, 그렇지 않으면 현재 start 가 있는 위치의 값을 리턴한다.

<br>

#### rear

큐가 비었으면 -1을 리턴하고, 그렇지 않으면 rear 에서 한 칸 이전의 값을 리턴한다. 

실제로는 이를 구현하기 위해 rear 에서 size - 1 만큼 이동한다.

<br>

#### is_empty

start 요소가 None 이고 start 와 end 가 같은 인덱스에 있을 때 비었다고 판단한다. 

(start 와 end 가 같다는 조건이 없더라도 start 요소의 None 조건만 있어도 isEmpty 를 알 수 있다고 생각한다. start 와 end  를 비교하는 이유에 대해서 좀 더 파악이 필요하다.)

<br>

#### is_full

start 요소가 None 이 아니고 start 와 end 가 같은 인덱스에 있을 때 가득찼다고 판단한다. 

<br>

<br>

### 두번째 풀이

첫번째 풀이와 달리 큐의 한칸을 비워둔다.

<br>

#### en_queue

end 를 한칸 이동 후 요소를 넣는다. 

<br>

#### de_queue

start 를 한칸 이동 후 요소를 None 으로 한다.

<br>

#### front

큐가 비었으면 -1을 리턴하고, 그렇지 않으면 start 를 한 칸 이동한 위치의 값을 리턴한다.

<br>

#### rear

큐가 비었으면 -1을 리턴하고, 그렇지 않으면 end 가 위치한 값을 리턴한다.

<br>

#### is_empty

start 와 end 가 같으면 큐가 비어있다.

<br>

#### is_full

end 가 한칸 이동하면 start 와 같아질 경우 큐가 가득찼다.

<br>

### Java

#### DesignCircularQueue622

직접 풀이했다.

<br>

#### DesignCircularQueue622_2

교재의 풀이를 참고했다. 

length 변수를 별도로 두어서 현재 배열에 몇개의 요소가 들어왔는지 확인한다. length 변수를 별도로 사용하지만 DesignCircularQueue622 풀이보다 훨씬 더 간결하게 구현한다.

rear 를 0이 아닌 -1로 초기값을 설정해서 최초에 원형 큐에 요소를 입력하면 rear 를 0으로 만들어서 front 도 최초로 입력한 값을 바라볼 수 있도록 한다. 만약에 rear 를 0으로 했다면 이때는 예외처리 등의 방법을 통해 front, rear 값을 조정해야 한다.

<br>

#### DesignCircularQueue622_3

큐의 크기를 k 보다 1 크게 설정하고 큐를 최대 k 갯수만큼 채울 수 있도록 한다.

큐에 요소를 넣을 때는 rear 를 한칸 이동한 뒤에 넣고, 큐에 요소를 뺄 때는 현재 front 인덱스 값을 -1로 초기화 하고 front 를 한칸 이동한다.

큐가 비었다면 front 와 rear 가 같은 인덱스고, 큐가 가득찼다면 rear 에서 한칸 이동했을 때 front 와 같아진다.

DesignCircularQueue622_2 와 달리 length 변수를 별도로 사용하지 않지만 큐의 크기를 k 보다 1 크게 사용해서 약간의 공간을 더 사용한다.

<br>

#### DesignCircularQueue622_4

연결리스트를 사용해서 구현했다.

head, tail 변수를 사용해서 tail.next 가 head 를 보도록 했다.

그리고 maxSize 와 size 변수를 두어서 큐에 요소를 더하면 size 를 1 더하고 큐에 요소를 빼면 size 를 1 뺀다. maxSize 가 size 와 같으면 큐가 가득찬 상태고 size 가 0 이면 큐가 빈 상태다.

<br>

#### DesignCircularQueue622_5

배열을 사용했다. 

k + 1 크기만큼 배열을 만들고 큐가 다 찼을 때 한 칸은 비어있도록 했다. enQueue 는 end 를 이동하고 deQueue 는 start 를 이동한다.

큐가 다 찼을 때 한 칸을 비운다고 했는데 큐가 다 찼으면 end 가 front 보다 한 칸 앞에 있다. 반면에 큐가 비었다면 start 와 end 가 같다.

<br>

<참고>

[파이썬 알고리즘 인터뷰](https://www.yes24.com/Product/Goods/91084402)

https://lktprogrammer.tistory.com/59

https://eunjinii.tistory.com/59

[자바 알고리즘 인터뷰](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=324537416)

