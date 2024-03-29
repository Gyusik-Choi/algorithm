# 백준

## 1655

왜 우선순위큐 문제인지 이해하는게 쉽지 않았다. 그렇다고 정렬로는 시간제한이 짧았기에 통과할 수 없는 문제라고 생각했다.

우선순위큐를 두개-최대힙, 최소힙-를 활용해야 한다는 생각은 전혀 하지 못했기에 새로운 문제였다. 구글링을 통해 두개의 우선순위큐를 활용해야 한다는 것을 알았다. 이분탐색의 방법도 있었으나 우선은 이 문제는 우선순위큐로 분류된 문제라 어떻게 우선순위큐를 활용해 해결할 수 있을지에 좀 더 집중했다.

문제의 아이디어는 최대힙, 최소힙 두개를 활용해서 길이가 같으면 최대힙에 숫자를 넣고, 길이가 다르면 최소힙에 넣었다. 처음에는 둘 다 비어있기에 최대힙에 들어갈 것이고 그 다음은 길이가 맞지 않기에 최소힙에 들어간다. 사실상 길이로 비교하지 않아도 하나씩 번갈아서 들어가기 때문에 홀수짝수로 구분해서 넣어줘도 상관없다.

맨 처음에는 어차피 하나라서 최대힙, 최소힙 어디에 넣든 답은 같은데 그 이후부터가 중요하기에 최대힙에 먼저 넣어준다. 최대힙에 먼저 넣고 그 다음에 최소힙에 넣어주면 양쪽에 하나씩 들어간 상태다. 그 다음에 최대힙에 넣어주면 3개 중의 중간 값을 구할 수 있다. 만약에 최대힙의 첫번째 숫자가 최소힙의 첫번째 숫자보다 더 크더라도 이럴 경우에는 서로 값을 교환하기 때문에 중간값을 구할 수 있다.

100, 99, 98 의 경우를 보면 먼저 최대힙에 100이 들어가고 그 다음에 최소힙에 99가 들어간다. 이때 98이 최대힙에 들어가서 최대힙 - 100, 98 / 최소힙 - 99 이 된다. 여기서 100과 99을 바꿔주기 때문에 99를 구할 수 있게 된다. 

그런데 만약에 문제의 조건을 아예 반대(최소힙에 먼저 넣고, 최대힙에 값이 있으면서 최대힙의 첫번째 숫자보다 최소힙의 첫번째 숫자가 더 크면 교환, 항상 최소힙 첫번째 값이 정답)로 해보면 답을 구하기 어려워진다. 이 조건에 따르면 최대힙 - 99 / 최소힙 - 98, 100 이렇게 되는데 이러면 98이 출력되게 돼서 오답이다. 

힙 구조는 최대힙이건 최소힙이건 첫번째에 위치한 값을 구하는데 최적화돼서 그 이후 인덱스에 위치한 값들의 정렬 상태는 느슨한 정렬 상태라서 첫번째의 원소들로만 비교를 해야 해서 배열의 마지막 값을 비교대상으로 삼을 수도 없다.

그래서 다시 원래의 조건으로 살펴보면 최대힙의 첫번째 숫자, 최소힙의 첫번째 숫자를 비교해서 최대힙의 경우가 더 크면 교환하는 것은 균형을 맞추는 작업이다. 현재까지의 입력 숫자의 갯수가 홀수라면 중앙값을 고를 수 있도록 큰 값을 최소힙쪽으로 치우고 더 작은 값을 최소힙으로 부터 가져와서 최대힙에서 힙정렬이 된 첫번째 숫자가 중앙값이 될 수 있다. 예를들어 최대힙 - 10, 7, 5/ 최소힙 - 8, 9 의 경우면 10과 8이 교환돼서 최대힙 - 8, 7, 5/ 최소힙 9, 10이 되므로 정답인 8을 구할 수 있게 된다.