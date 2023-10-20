# 프로그래머스

## 오픈채팅방

딕셔너리를 활용했다. key error 를 방지하고 보다 편하게 value 를 추가하기 위해 defaultdict 를 사용했다.

record 리스트를 for 문을 돌면서 키가 유저 아이디, 값이 닉네임으로 된 딕셔너리인 nick_dict 에 매번 닉네임을 갱신해준다.

단, 요소가 Leave 일 경우 닉네임이 없기 때문에 기존의 닉네임을 nick_dict 에서 구해서 갱신한다.

요소가 Leave 가 아니라 Enter, Change 인 경우 유저 아이디 정보와 상태 정보(Enter 혹은 Change) 를 리스트로 묶어서 result 리스트에 넣어준다.

record 리스트 for 문을 돌고나서는 result 리스트를 for 문을 돈다. result 요소의 유저 아이디를 통해 nick_dict 에서 닉네임을 조회한 후 상태 값을 확인하여 닉네임과 들어왔는지 나갔는지를 나타내는 구문을 합쳐서 answer 리스트에 담았다.



