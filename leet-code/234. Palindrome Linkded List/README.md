# LeetCode

## 234. Palindrome Linked List

양방향이 아닌 단일 연결 리스트가 입력으로 주어진다.

연결 리스트의 맨 앞을 가리키는 변수 2개를 갖고서 하나는 두 칸씩 이동하고 다른 하나는 한 칸씩 이동한다. 두 칸씩 이동하는 변수가 연결 리스트의 맨 끝까지 가면 다른 하나는 연결 리스트의 가운데에 위치하게 되는게 포인트다. 가운데 지점을 알 수 없는 연결 리스트에서 가운데 지점을 찾는 방법으로 활용할 수 있다.

엄밀히 따지면 짝수와 홀수가 조금 다르긴 하다. 일단 홀수와 달리 짝수는 한 가운데 지점이 있을 수 없다. 짝수개 노드가 있는 연결 리스트라면 두 칸씩 이동해서 끝까지 이동 (맨 마지막 노드가 아닌 맨 마지막 노드에서 다음 노드를 가리키는 값이 None 이어서 아예 None 이 되는 상황) 하면 한 칸씩 이동하는 노드는 가운데에 있는 두 칸 중에 한 칸 더 이동한 위치에 있게 된다. 1 2 3 4 가 있다고 하면 3의 위치에 놓인다.

별도의 변수를 통해 한 칸씩 이동하는 변수가 갖는 값에 대해서 역순 연결 리스트를 만들면 한 칸씩 이동하는 변수와 값을 비교하면서 팰린드롬 여부를 알 수 있다. 홀수의 경우 한 칸씩 이동하는 변수가 연결 리스트의 가운데에 위치하게 돼서 팰린드롬 비교에는 가운데 값은 불필요하기 때문에 한 칸 더 이동한 후에 역순 연결 리스트와 비교할 수 있다.

<br>

<참고>

파이썬 알고리즘 인터뷰

https://jaykalia07.medium.com/linked-lists-and-the-runner-technique-8e70e5433389
