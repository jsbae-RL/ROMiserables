from collections import deque

def solution(s):
    same_stack = deque()
    string_len = 0
    answer = 0
    while string_len < len(s):
        first = s[string_len]
        if len(same_stack) == 0 or first in same_stack:
            same_stack.append(first)
        else :
            same_stack.pop()

        if len(same_stack) == 0:
            answer += 1
        string_len += 1

    if len(same_stack) != 0:
        answer += 1
    else :
        answer

    return answer

print(solution('ababab'))

# def solution(s):
#     string_st = deque(s)
#     same_stack = deque()
#     no_same_stack = deque()
#     string_len = len(string_st)
#     answer = 0
#     while string_len > 0:
#         first = string_st.popleft()
#         if len(same_stack) == 0 or first in same_stack:
#             same_stack.append(first)
#         else :
#             no_same_stack.append(first)

#         if len(same_stack) == len(no_same_stack):
#             answer += 1
#             same_stack.clear()
#             no_same_stack.clear()
#         string_len -= 1

#     if len(same_stack) != 0:
#         answer += 1
#     else :
#         answer

#     return answer
