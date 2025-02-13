# def solution(arr):
#     check = []
#     check.append(arr[0])
#     for i in arr[1:]:
#         if check[-1] != i:
#             check.append(i)
#     return check

# print(solution([4, 4, 4, 3, 3]))


arr = [4, 4, 4, 3, 3]
result1 = set(arr)
print(f"set(arr)      : {result1}")

result2 = list(result1)  # list(set(arr))
print(f"list(set(arr) : {result2}")