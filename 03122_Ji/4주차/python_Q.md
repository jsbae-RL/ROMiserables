## 내장 함수 문제

### 1. abs 함수 사용하기
```python
# 입력: -5
# 출력: 5
```

### 2. all 함수로 리스트 검사하기
```python
numbers = [True, True, False]
# 출력: False
```

### 3. any 함수로 값 존재 여부 확인
```python
numbers = [0, 0, 1]
# 출력: True
```

### 4. enumerate 함수로 인덱스와 값 출력
```python
words = ["a", "b", "c"]
# 출력: [(0, "a"), (1, "b"), (2, "c")]
```

### 5. filter 함수로 짝수 필터링
```python
numbers = [1, 2, 3, 4, 5]
# 출력: [2, 4]
```

### 6. len 함수로 리스트 길이 확인
```python
numbers = [1, 2, 3]
# 출력: 3
```

### 7. max 함수로 최대값 찾기
```python
numbers = [10, 20, 30]
# 출력: 30
```

### 8. min 함수로 최소값 찾기
```python
numbers = [10, 20, 30]
# 출력: 10
```

### 9. map 함수로 리스트 요소 제곱
```python
numbers = [1, 2, 3]
# 출력: [1, 4, 9]
```

### 10. pow 함수로 제곱 계산
```python
# 입력: 2, 3
# 출력: 8
```

### 11. range 함수로 숫자 생성
```python
# 입력: range(5)
# 출력: [0, 1, 2, 3, 4]
```

### 12. reversed 함수로 리스트 뒤집기
```python
numbers = [1, 2, 3]
# 출력: [3, 2, 1]
```

### 13. round 함수로 소수점 반올림
```python
# 입력: 3.14159, 2
# 출력: 3.14
```

### 14. sorted 함수로 정렬하기
```python
numbers = [3, 1, 2]
# 출력: [1, 2, 3]
```

### 15. sum 함수로 리스트 합 계산
```python
numbers = [1, 2, 3]
# 출력: 6
```

### 16. type 함수로 데이터 타입 확인
```python
value = 42
# 출력: <class 'int'>
```

### 17. zip 함수로 리스트 병합
```python
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
# 출력: [(1, "a"), (2, "b"), (3, "c")]
```

### 18. eval 함수로 문자열 표현식 계산
```python
expression = "2 + 3 * 4"
# 출력: 14
```

### 19. chr 함수로 아스키 코드 문자 반환
```python
# 입력: 97
# 출력: 'a'
```

### 20. ord 함수로 문자 아스키 코드 반환
```python
# 입력: 'a'
# 출력: 97
```
## 정규 표현식 문제

### 1. 문자열에서 모든 이메일 주소 찾기
```python
text = "Contact us at info@example.com or support@domain.org"
# 출력: ['info@example.com', 'support@domain.org']
```

### 2. 특정 패턴으로 시작하는 단어 추출
```python
text = "apple banana cherry date"
pattern = r"^a"
# 출력: ['apple']
```

### 3. 전화번호 형식 검사
```python
phone = "123-456-7890"
# 출력: True (형식이 올바른 경우)
```

### 4. 문자열에서 숫자만 추출
```python
text = "Order 123 items for $45.67"
# 출력: ['123', '45', '67']
```

### 5. 공백으로 구분된 단어의 개수 세기
```python
text = "This is a test sentence."
# 출력: 5
```

### 6. HTML 태그 제거하기
```python
html = "<p>This is a paragraph.</p>"
# 출력: 'This is a paragraph.'
```

### 7. 특정 단어 포함 여부 확인
```python
text = "Python is fun"
word = "fun"
# 출력: True
```

### 8. 날짜 형식 변환
```python
date = "2025-01-27"
# 출력: '27-01-2025'
```

### 9. 소문자와 대문자 교체
```python
text = "Hello World"
# 출력: 'hELLO wORLD'
```

### 10. IP 주소 형식 검사
```python
ip = "192.168.1.1"
# 출력: True (형식이 올바른 경우)
```

### 11. 문자열에서 모든 URL 추출
```python
text = "Visit https://example.com or http://test.org for info."
# 출력: ['https://example.com', 'http://test.org']
```

### 12. 특정 패턴의 단어 치환
```python
text = "I love cats and dogs"
pattern = r"cats"
replacement = "pets"
# 출력: 'I love pets and dogs'
```

### 13. 문자열에서 연속된 공백 제거
```python
text = "This   is   a  test."
# 출력: 'This is a test.'
```

### 14. 특정 문자열이 파일 경로인지 검사
```python
path = "/user/home/test.txt"
# 출력: True (파일 경로가 올바른 경우)
```

### 15. 영어 단어만 추출하기
```python
text = "123abc!@#def456"
# 출력: ['abc', 'def']
```

### 16. 특정 접미사로 끝나는 단어 찾기
```python
text = "running swimming jumping"
pattern = r"ing"
# 출력: ['running', 'swimming', 'jumping']
```

### 17. 문자열에서 중복된 단어 제거
```python
text = "this this is is a test test"
# 출력: 'this is a test'
```

### 18. 문자열에서 특수 문자 제거
```python
text = "Hello!@#$%^&*()"
# 출력: 'Hello'
```

### 19. 특정 길이의 단어만 추출
```python
text = "cat bat mat"
length = 3
# 출력: ['cat', 'bat', 'mat']
```

### 20. 파일 확장자 추출
```python
filename = "document.pdf"
# 출력: 'pdf'
```