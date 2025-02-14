def solution(answers):
    # 1번 12345
    # 2번 21 23 24 25
    # 3번 33 11 22 44 55
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    score = [0,0,0]       # 1~3번의 점수 매길 리스트


    for index, A in enumerate(answers):     # answers 요소를 순회하며 pattern과 비교
        if A == pattern1[index]:
            score[0] += 1
        if A == pattern2[index]:
            score[1] += 1
        if A == pattern3[index]:
            score[2] += 1

#가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return
    max_point = max(score)
    winner = [i+1 for i, j in enumerate(score) if j == max_point]  
 
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요
    sorted_win = sorted(winner)
    
    return sorted_win

answers = [1,2,3,4,5]
print(solution(answers))

answers = [1,3,2,4,2]
print(solution(answers))
