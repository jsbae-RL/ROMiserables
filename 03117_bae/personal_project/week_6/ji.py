# 각 유저는  신고 제한 없음
# k 번 이상 신고된 유저는 게시판 이용 정지, 해당 유저를 신고한, 모든 유저에서 정지 사실 메일 전송
# 마지막에 한번에 이용 정지 하면저 정지 메일 발송

def solution(id_list, report, k):
    check_email = {name: 0 for name in id_list}
    get_renum = {name: 0 for name in id_list}
    report_name = {name: [] for name in id_list}

    report_set = set(report)

    for i in report_set:
        re_name, get_re = i.split(' ')
        report_name[re_name].append(get_re)
        get_renum[get_re] += 1

    for name, count in get_renum.items():
        if count >= k:
            for user, check_email_value in report_name.items():
                if name in check_email_value:
                    check_email[user] += 1

    return list(check_email.values())


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))