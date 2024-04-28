### Q. readline 함수에 괄호를 안주는 이유

```python
import sys
input = sys.stdin.readline
```

- ### A. 
    - #### input 변수에 입력받은 문자열을 대입하는것이 아니라, input 함수를 다시 정의하고 있는 것이기 때문입니다.

    - #### 파이썬에서 함수 이름에 괄호를 붙이지 않으면 함수의 주소값이 되는데, <br> input의 함수 주소값을 입력속도가 빠른 sys.stdin.readline 의 주소값으로 바꾸어서 <br> 평소 입력 받듯이 input() 을 호출하면 sys.stdin.readline()이 호출되도록 하기 위함입니다.

        ```python
        print("original input = ", input) # 원래 파이썬의 input

        import sys
        input = sys.stdin.readline
        print("changed input = ", input) # input의 주소가 속도가 빠른 함수로 바뀌었음
        ```

        ```
        original input =  <built-in function input>
        changed input =  <bound method StdInputFile.readline of <idlelib.run.StdInputFile object at 0x0000019D4DBE92A0>>
        ```

    - #### 이제 input()을 호출하면 sys.stdin.readline() 이 호출됩니다.

<br>

---

<br>

### Q. input 변수에 괄호를 사용한 이유

```python
n = int(input().rstrip())
```

- #### 파이썬에서 함수를 호출할 때 함수이름(매개변수)를 사용하기 때문에 <br> sys.stdin.readline()을 호출하여 입력된 한 줄을 읽어들이기 위해 사용했습니다.

<br>

---

<br>

### Q.
```python
input = sys.stdin.readline()
n = int(input.rstrip())

for _ in range(n):
    a, b = list(map(int, input.rstrip().split()))

...
```

- #### 위 코드에서는 입력을 단 한번 맨 위에서만 받고있습니다

- #### 한 줄씩 입력을 받고싶을 때 마다

    ```python
    input().rstrip()
    ```
    #### 을 호출해야합니다.

    <br>

- ### A.
    ```python
    n = int(input().rstrip())
    for _ in range(n):
        a, b = list(map(int, input().rstrip().split()))
    ...
    ```





