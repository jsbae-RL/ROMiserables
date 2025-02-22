from collections import defaultdict

def solution(id_list, report, k):
    report = set(report)  # 중복 신고 제거
    reports_by_user = defaultdict(set)  # 각 유저가 신고한 ID 저장
    reported_count = defaultdict(int)  # 각 유저가 신고당한 횟수 저장

    # 신고 데이터 처리
    for r in report:
        reporter, reported = r.split()
        if reported not in reports_by_user[reporter]:  # 중복 신고 방지
            reports_by_user[reporter].add(reported)
            reported_count[reported] += 1

    # 정지된 유저 목록
    banned_users = {user for user, count in reported_count.items() if count >= k}

    # 결과 메일 개수 계산
    result = []
    for user in id_list:
        result.append(len(reports_by_user[user] & banned_users))

    return result

# 테스트 예시
id_list1 = ["muzi", "frodo", "apeach", "neo"]
report1 = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k1 = 2
print(solution(id_list1, report1, k1))  # [2, 1, 1, 0]

id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3
print(solution(id_list2, report2, k2))  # [0, 0]
