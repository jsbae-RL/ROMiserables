def solution(numbers, target):
    stack = [(0, 0)]  # (현재 인덱스, 합계) 튜플을 사용하면 한번에 두개의 값을 스택에 저장 가능합니다.
    count = 0  # 타겟 넘버를 만족하는 경우의 개수
    
    while stack:
        index, sum = stack.pop()

        # 모든 숫자를 사용한 경우
        if index == len(numbers):
            if sum == target:
                count += 1
        else:
           
            # + 연산 경우
            plus = sum + numbers[index]
            stack.append((index + 1, plus))
            
            # - 연산 경우
            minus = sum - numbers[index]
            stack.append((index + 1, minus))
            print(stack)
    
    return count

print(solution([4,1,2,1],4))