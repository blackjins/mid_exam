'''
위 코드를 이용하여 아래 조건을 만족시키는 
`guessing_numbers()` 함수를 구현하라.

- 하나의 파라미터 `n` 을 사용한다.
- 인자 n 은 10,000 보다 큰 값을 사용하며, 그렇지 않은 경우 오류가 발생해야 한다. 
- 함수가 인자 n 과 함께 실행되면 1과 n 사이에서 임의로 선택된 수를 알아맞히는 게임을 시작한다. 
- 게임이 시작되면 사용자가 아닌 컴퓨터 스스로 임의로 선택된 수를 알아맞힐 때까지 숫자를 무작위로 추측하는 과정을 반복한다.
    단, 이진탐색 알고리즘을 활용하다.
- 수를 맞히면 추측 횟수와 맞힌 수를 튜플로 반환하며 게임이 종료된다.

단, 재귀는 사용하지 않으며 `while` 반복문을 사용한다.

참고: [이진탐색 개념 및 구현](https://yoongrammer.tistory.com/75)
'''


from random import randint
import math
from turtle import settiltangle


def guessing_numbers(n):
    counting = 0
    print("수 알아맞히기 게임에 환영합니다.")
    if n < 10000:
        raise Exception("10000이상의 수를 입력해주세요.")
    else:
        answer = randint(1, n)
        mid_number = math.ceil((1+n)/2)
        if answer > mid_number:
            end_number = n
            start_number = mid_number
            mid_number = math.ceil((start_number+end_number)/2)
            counting = counting + 1
            print(answer, counting, start_number, mid_number, end_number)
        elif answer < mid_number:
            end_number = mid_number
            start_number = 1
            mid_number = math.ceil((start_number+end_number)/2)
            counting = counting + 1
            print(answer, counting, start_number, mid_number, end_number)
        while answer != mid_number:
            if answer > mid_number:
                start_number = mid_number
                mid_number = math.ceil((start_number+end_number)/2)
                if mid_number > answer:
                    end_number = mid_number
                counting = counting + 1
            elif answer < mid_number:
                end_number = mid_number
                mid_number = math.ceil((start_number+end_number)/2)
                if mid_number < answer:
                    start_number = mid_number
                counting = counting + 1
        return (answer, counting)

for _ in range(10):
    final_count = guessing_numbers(10000)[0]
    assert  final_count <= math.ceil(math.log2(10000))