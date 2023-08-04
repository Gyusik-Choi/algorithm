# 백준

## 1715

이것이 코딩테스트다 교재에 수록된 문제다. 정렬 유형의 문제로 우선순위 큐를 활용했다.

값을 두개씩 더해나가는데, 이때 더한 값을 포함해서 남은 숫자들 중에서 가장 작은 두개를 다시 더하는 방식으로 진행한다. 정렬을 사용하게 되면 최소 값 뿐만 아니라 나머지 요소들도 모두 정렬이 되므로 우선순위 큐를 이용해서 필요한 최소값 두개만 얻는다.

반례는 [이분](https://www.acmicpc.net/board/view/72799)의 글을 참고했다.

주의할 점은 숫자가 하나만 있을 경우는 정답이 0이며, 힙큐를 사용할 경우 숫자를 넣을때는 heappush로 넣어줘야 한다. 처음에 입력받은 숫자를 heappush가 아니라 배열에 append로 넣은 후에 heappop으로 꺼내게 되면 최소값을 제대로 찾을 수 없다.

<br>

https://www.acmicpc.net/board/view/72799

https://www.acmicpc.net/board/view/33201

https://techblog-history-younghunjo1.tistory.com/278

https://claude-u.tistory.com/341

