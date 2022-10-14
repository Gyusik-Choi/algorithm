# Python Unit Test

### unittest

javascript 에서 jest 등을 설치해서 사용하는 것과 달리 python 자체에 단위 테스트 모듈을 갖고 있다.

unittest 모듈을 사용해서 단위 테스트를 진행할 수 있다.

<br>

### 단위 테스트를 수행하기 위해 unittest 모듈을 import 해야 한다.

```python
import unittest
```

<br>

### 별도의 테스트 파일로 테스트를 수행한다면 테스트할 파일을 import 해야 한다.

```python
# 테스트할 파일의 이름이 guido.py 라면
import guido
```

<br>

### unittest.TestCase 를 상속한 클래스를 생성한다

```python
class GuidoTest(unittest.TestCase):
```

<br>

### test 함수의 이름은 test_로 시작해야 테스트할 함수로 인식한다

pycharm 에서 테스트를 진행했는데, 함수명에 test_ 를 붙이지 않으니 아예 테스트에 포함되지 않았다. 아래의 경우 첫번째 함수인 test_guido_func 만 테스트를 수행한다.

```python
class GuidoTest(unittest.TestCase):
    def test_guido_func(self):
        pass
    def guido_func2(self):
        pass
```



