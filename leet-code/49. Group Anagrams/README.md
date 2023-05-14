# Leet Code

## 49. Group Anagrams

### 49_group_anagrams.py

파라미터 strs 를 for loop 돌면서 오름차순으로 정렬하여 defaultdict 에 넣어줬다.

<br>

### 49_group_anagrams.dart

49_group_anagrams.py 와 방식 자체는 같으나defaultdict 가 아닌 Map 을 사용했기 때문에 key error 가 발생하지 않도록 해당 key 가 존재하는지 확인하는 작업이 추가됐다.