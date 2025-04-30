def solution(numbers,target):
    if (sum(numbers)+target)%2==1:
        return 0
    sum_target = int((sum(numbers)+target)/2)
    # 1 1 1 1 1
    dp = {0: 1}
    for num in numbers:
        for sub_sum in range(sum_target, num - 1, -1):  #4 1
            dp[sub_sum] = dp.get(sub_sum, 0) + dp.get(sub_sum - num, 0)
            print(sub_sum,end =" : ")
            print(dp[sub_sum])
    
    print(dp)
    return dp.get(sum_target, 0)


print(solution([1,1,1,1,1],3))
print(solution([4, 1, 2, 1],4))
# 2**len(numbers)의 경우의 수를 가진 합
# 2의 2**20 이거만 해도 경우의 수가 너어어무 많아서 이건 아니다 싶음.

# 수로 하다가 머리 빠질거 같아서 문자로함
# a,b,c,d,e와 타겟이 있다고 치자
# 그중에 a+b-c-d-e=target(numbers)+targ이 성립 한다면 뭔가의 양의값 = (전체값의 핪+ 타겟)/2
# 2(a+b)=sumet이 성립된다. 이건 아예 안되는놈 빼는 경우로 써먹을수 있겠다.
# 왜냐하면 뭐가 됬든 첫 식이 성립 한다 쳤을때 (sum(numbers)+target)%2를 했을때 나머지가 1이면 애초에 성립되지 않는 식이된다.
# 좌측식이 a+b 든 a 든 뭐든 간에 위의 조건이 안맞으면 수학적으로 되지 않으므로 애초에 과정을 할 필요 없이 개수 0 이라고 해도 맞다.

# 그럼 다시 보자 x = (sum(numbers)+target)/2는 조건에 성립하는 식이다. 그럼 이제 x에 들어가는 합을 찾으면 좀 더 쉽지 않을까...?
# 일딴 빼기의 경우가 다 사라졌다. 충분히 줄어 들었지만 여기서 하나더 생각 할 수 있다
# 이제 일반적인 경우의 수에서 (sum(numbers)+target)/2보다 커지는 순간 더이상 계산할 이유가 없다 작거나 같을때 계속 다음 동작을 하면되는 것이다.
# 여기서 또 막힘..ㅎ 막힌 이유.... 6개에 120개인데 물론 합이 넘어가는걸 안빼긴함 여튼 그래도 많아보여서.... 의미가 없어 보임... 대강 합이 타겟넘어간다? 넘겨! 하기엔.... 이것도 사실 비효율적 이라고 보는게 결국 넘어가는거까지 확인을 하니까까......
# 그래서 gpt씨에게 물어봄
# DP 동적 계획 법이란게 있다고 하네요.... 한번 구한 값을 계속 활용 해서 여러번 반복 안한다고 해요...
# 이해하고 쓴건 아니고 동작 방식에 대해서 정도만 이해한 상태로 작성 했습니다 감안 부탁드립니다.

# 우선 딕셔너리를 통해서 진행하는데 모든 수의 합이 0인 경우는 아무것도 선택안한 상태 밖에 없어서 1이고 초기 값을 입력한것 입니다.
# 우선 모든 number의 수를 대입해서 확인은 해야겠죠? 그래서 for문을 저렇게 활용 했습니다.
# 이제 타겟 부터 현재 선택된 수에 대해 탐색을 시작하는데 정순으로 올라가면 시작값이 뒤에 값에 영향을 줘서 반대로 역순으로 가면 시작값이 영향을 전혀 못줍니다.
# 첫과정에서 sub_sum이란 키값에 sub_sumdml 제일 작은수 즉 num에 1이란 값이 들어갑니다. 이제 이 이후에 영향을 주게 되겠죠.
# 여기서 왜 1이 들어가느냐 하면 get(x,0)은 딕셔너리 x키값에 value값이 존재하면 해당 값을 반환 하고 아니면 ,뒤의 값 즉 0을 반환 합니다.

# 그럼 두번째 과정에서는 num의 키에 1이 추가되고 첫번째 과정에서 1이 들어갔던 키값을 부르는 곳 거기서 또 1이 추가 되겠죠?
# 이걸 반복해서 모든 과정을 거치고, sumtarget에 값을 확인해보면 합쳤을때 해당 키값에 도달 할수 있다면 1이 추가 됩니다. 만약 비었다면 get함수에 의해 0을 반환 하구요.
# 




## 아래식은 제가 defaultdict이 잘 이해가 안되서 고대로 나둬봅니다.
# from collections import defaultdict

# def solution(numbers, target):
#     total_sum = sum(numbers)
    
#     # target을 만들 수 없는 경우 (S + target이 홀수인 경우)
#     if (total_sum + target) % 2 == 1:
#         return 0
    
#     target_sum = (total_sum + target) // 2
    
#     # DP 방식으로 부분집합 합의 개수 찾기
#     dp = defaultdict(int)
#     dp[0] = 1  # 합이 0이 되는 경우의 수는 1 (아무것도 선택하지 않은 경우)
    
#     for num in numbers:
#         for sub_sum in range(target_sum, num - 1, -1):
#             dp[sub_sum] += dp[sub_sum - num]
    
#     return dp[target_sum]

# # 예제 테스트
# print(solution([1, 1, 1, 1, 1], 3))  # 5
# print(solution([4, 1, 2, 1], 4))  # 2


## 참고 시간 비교용
# 테스트 1 〉	통과 (2.60ms, 10.3MB)
# 테스트 2 〉	통과 (2.48ms, 10.2MB)
# 테스트 3 〉	통과 (1.02ms, 10.3MB)
# 테스트 4 〉	통과 (1.29ms, 10.1MB)
# 테스트 5 〉	통과 (1.25ms, 10.1MB)
# 테스트 6 〉	통과 (1.42ms, 10.4MB)
# 테스트 7 〉	통과 (0.50ms, 10.3MB)
# 테스트 8 〉	통과 (1.10ms, 10.1MB)

#우석님꺼
# 테스트 1 〉	통과 (630.08ms, 10.2MB)
# 테스트 2 〉	통과 (514.51ms, 10.3MB)
# 테스트 3 〉	통과 (0.49ms, 10.2MB)
# 테스트 4 〉	통과 (1.90ms, 10.1MB)
# 테스트 5 〉	통과 (14.85ms, 10.3MB)
# 테스트 6 〉	통과 (1.95ms, 10.1MB)
# 테스트 7 〉	통과 (0.63ms, 10.3MB)
# 테스트 8 〉	통과 (3.84ms, 10.1MB)