'''
아래 조건을 만족하는 `find()` 함수를 정의하라.

* `word1`, `word2`, `position` 세 개의 인자를 받는다.
* `word1`, `word2`는 문자열을 입력값으로 기대한다.
* `word1`이 `word2`를 부분문자열로 포함할 경우 부분문자열의 시작위치를, 포함하지 않을 경우 -1을 리턴한다.
* `position` 매개변수는 정수를 입력값으로 기대하며, 0을 키워드 인자로 사용한다. 
* `position`을 통해 전달된 정수는 탐색을 시작할 위치를 나타낸다.
'''

def find(word1, word2, position=0):
  if word2 in word1:
    a = word1[position:]
    while len(a) < len(word1):
      a = " " + a
    a = a.find(word2)
    return a
  elif word2 not in word1:
    return -1

assert find('python', 'yt') == 1
assert find("I love you!", 'o', 4)
assert find("hello world", 'elo') == -1