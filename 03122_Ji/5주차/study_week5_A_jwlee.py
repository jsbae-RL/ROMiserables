# ; 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
# ; 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# ; 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# ; 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# ; 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# ; 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# ; 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# ; 제한 조건
# ; 시험은 최대 10,000 문제로 구성되어있습니다.
# ; 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# ; 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

# ; 입출력 예
# ;         answers	        return
# ; 예 #1    [1,2,3,4,5]	    [1]
# ; 예 #2    [1,3,2,4,2]	    [1,2,3]

# ; 입출력 예 설명
# ; 입출력 예 #1

# ; 수포자 1은 모든 문제를 맞혔습니다.
# ; 수포자 2는 모든 문제를 틀렸습니다.
# ; 수포자 3은 모든 문제를 틀렸습니다.
# ; 따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

# ; 입출력 예 #2

# ; 모든 사람이 2문제씩을 맞췄습니다.

# ; 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# ; 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# ; 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...


def solution(answers):
    N = len(answers)
    
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    
    answer1 = []
    answer2 = []
    answer3 = []
   
    # 1
    i=0
    for _ in range(N):
        i = i % len(pattern1)
        answer1.append(pattern1[i])
        i += 1
    
    # 2
    i=0
    for _ in range(N):
        i = i % len(pattern2)
        answer2.append(pattern2[i])
        i += 1
    
    # 3
    i=0
    for _ in range(N):
        i = i % len(pattern3)
        answer2.append(pattern3[i])
        i += 1
    
    c1 = [a == a1 for a , a1 in zip(answers,answer1)].count(True)
    c2 = [a == a2 for a , a2 in zip(answers,answer2)].count(True)
    c3 = [a == a3 for a , a3 in zip(answers,answer3)].count(True)
    
    c = [c1,c2,c3]
    result = []
    max_c = max(c)
    
    for idx, cs in enumerate(c):
        if cs == max_c:
            result.append(idx+1)
    
    return result

    
print(solution([1,2,3,4,5]))


# pop 을 하면 시간 복잡도가 높아진다.