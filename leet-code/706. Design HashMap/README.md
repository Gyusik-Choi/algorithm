# LeetCode

## 706. Design HashMap

### Python

해시맵을 구현하는 문제다. 파이썬의 defaultdict 를 활용해서 풀이했다.

<br>

### put

해시맵의 사이즈를 1000 으로 설정했고 최대 키가 10 ^ 6 까지 올 수 있어서 키 충돌이 발생할 수 있다.

인자로 받은 key 자체가 중복되면 뒤에 나오는 value 로 덮인다. 

그러나 key 를 size 로 나눈 나머지로 구한 해시맵의 키 k 는 겹치더라도 value 를 각각 보유하기 위해 연결 리스트로 연결한다.

<br>

### get

해시맵에 일치하는 키가 없으면 -1을 리턴한다.

hash_map 이 defaultdict 라 키가 있는지 조회할 때 키가 없어도 키 에러가 발생하지 않는다. 

키가 없으면 해당 키로 디폴트 값을 생성한다. 

해당 키로 값이 존재하는지 볼때는 if self.hash_map[k] is None 이 아니라 if self.hash_map[k].value is None 으로 확인한다. 

if self.hash_map[k].value is None 로 접근할 경우 키가 없어서 디폴트 값을 생성하면 value 가 None 이라서 if 문을 충족할 수 있으나 if self.hash_map[k] is None 로 접근할 경우 if 문을 절대 충족할 수 없다.

<br>

### remove

```python
p = self.hash_map[k]

# 일치하는 키를 바로 찾음
if p.key == key:
    if p.next is None:
        # p = Node()
        # 위의 코드는 self.hash_map[k] 를 변화 시키지 않고
        # p 가 보는 대상이 바뀔 뿐이다
        self.hash_map[k] = Node()
    else:
        self.hash_map[k] = p.next
    return
```

위와 같이 일치하는 키를 바로 찾을 경우 위에서 선언한 p 를 변경하지 않고 self.hash_map[k] 를 변경한다.

p 는 self.hash_map[k] 와 같은 value 객체 (Node) 를 바라보고 있으나 p 를 변경할 경우 p 에 또 다른 변수를 할당하는 것이라 p 와 self.hash_map[k] 가 바라보는 주소값이 변경돼서 서로 다른 객체를 바라보게 된다.

<br>

```python
prev, p = p, p.next

while p:
    if p.key == key:
        prev.next = p.next
        return

    prev, p = p, p.next
```

위위와 달리 위에서는 self.hash_map[k] 가 아닌 prev, p 를 변경한다.

원시값이 아닌 객체의 경우 내부를 바꾸면 해당 객체를 바라보는 주소값 자체는 바뀌지 않는다.

여러 변수로 해당 객체를 바라볼 경우 함께 변경돼서 self.hash_map[k] 로 접근하지 않아도 객체를 변경할 수 있다.

<br>

### Java

#### DesignHashMap706_2

문제에서 key, value 의 범위가 0부터 1000000까지라 nodes 배열의 길이를 1000001로 한다.

이 풀이에서는 배열의 인덱스를 key 를 배열의 길이로 나눈 나머지로 구하므로 서로 다른 키가 동일한 인덱스로 매핑돼서 충돌하는 경우가 발생하지 않는다.

그렇지만 충돌하는 경우를 가정하고 풀이한다.

<br>

####DesignHashMap706_3

로드 팩터, 그로스 팩터 등을 이용해서 배열의 크기를 동적으로 늘려나가려고 했으나 문제가 있었다. 키의 인덱스를 구하는 부분이 문제가 됐다. 키를 현재 배열의 크기로 나눈 값으로 인덱스를 하려 했으나 배열의 크기 자체가 바뀔 수 있어서 동일한 키 인덱스를 구하지 못할 수 있었다. 로드 팩터를 넘어가면 배열의 크기를 그로스 팩터만큼 늘려나가기 때문에 배열의 총 크기는 가변적이다. 배열의 총 크기와 관계없이 일관된 키 인덱스를 구하는 해시 알고리즘이 필요하다.

따라서 해당 풀이에서는 위의 방법을 적용하지 않고 배열의 총 크기를 백만으로 고정했다.

<br>

<참고>

파이썬 알고리즘 인터뷰

자바 알고리즘 인터뷰

