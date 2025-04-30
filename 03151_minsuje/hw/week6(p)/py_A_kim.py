def count_num_pow(num: int):
    count = 0
    while num % 2 == 0:  # 2로 나눌 수 있을 때까지 나누기
        num //= 2
        count += 1
    return num, count

def Collatz_def(num: int) -> int:
    count = 0

    if num == 1:
        return 0  # 이미 1이면 0 반환

    num, step_count = count_num_pow(num)  # 2의 거듭제곱 처리
    count += step_count  # count 갱신

    while num != 1:
        if num % 2 == 0:
            num, step_count = count_num_pow(num)
            count+=step_count
        else:
            num = (3 * num + 1) // 2  # 3n+1 후 바로 //2 적용하여 최적화
            count += 2  # 두 단계 줄였으므로 추가

        if count >= 500:
            return -1  # 500번 초과 시 -1 반환

    return count

print(Collatz_def(6))
print(Collatz_def(16))
print(Collatz_def(626331))
print(Collatz_def(12412591235012358120581058105))