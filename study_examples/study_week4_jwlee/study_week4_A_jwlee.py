
def solution(arr):
    stack = []
    result = [arr[0]]       # 배열의 첫 값을 초기값으로
    for num in arr:
        if stack:               # 스택 비어있지 않으면
            curr = stack.pop()      # 스택 상단 내용 확인
            if curr != num:         # pop한 값이 리스트에 없으면 result에 추가
                result.append(num)      

        stack.append(num)       # 스택비었으면
    return result
    
arr=[1,1,3,3,0,1,1]     # [1,3,0,1]
print(solution(arr))

arr=[4,4,4,3,3]           # [4,3]
print(solution(arr))



