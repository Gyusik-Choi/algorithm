

### 첫번째 풀이

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

<참고>

[파이썬 알고리즘 인터뷰](https://www.yes24.com/Product/Goods/91084402)

https://lktprogrammer.tistory.com/59

https://eunjinii.tistory.com/59

