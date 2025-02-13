from collections import deque

def solution(numbers, target):
    stack = deque([(0, 0)])
    count = 0

    while stack:
        current_sum, index = stack.pop()

        if index == len(numbers):
            if current_sum == target:
                count += 1
        else:
            stack.append((current_sum + numbers[index], index + 1))
            stack.append((current_sum - numbers[index], index + 1))

    return count