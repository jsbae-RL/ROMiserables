# https://school.programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list,report,k):
    report_dict = {key:set() for key in id_list}                    # id_list에 있는 유저 네임으로 set()을 가지는 딕셔너리 생성(유저-신고한id 저장하기 위함)
    
    for user in report:
        report_dict[user.split(' ')[0]].add(user.split(' ')[1])     # 유저: (신고한 아이디) 형태로 딕셔너리에 저장한다(set 형식이므로 한 유저가 같은 유저를 몇번 신고해도 한번 들어감)
        
    reported_dict = dict.fromkeys(id_list, 0)                       # 유저 별 신고당한 횟수를 저장하는 딕셔너리 생성(기본값 0)
    for reported_user in report_dict.values():                      # 유저-신고한 id 딕셔너리의 value 값에서 등장한 만큼 각 유저의 신고당한 횟수 +1
        for name in reported_user:                                  
            reported_dict[name] += 1
    
    email_dict = dict.fromkeys(id_list,0)                           # 이메일 받는 횟수를 저장할 딕셔너리 생성
    for id, reported_count in reported_dict.items():                # 유저 별로 신고당한 횟수가 k 이상일 경우우
        if reported_count >= k:
            email_reci= [key for key in email_dict.keys() if id in report_dict[key]] # 이메일 수신자를 결정한다
            for key in email_reci:                                              # ((신고 k회 이상 당한 id가 아니면서)이건 자진신고 못하니까 빼고고 , 이 id를 신고한 적 잇는 유저 대상)
                email_dict[key]+=1                                              # 횟수 +1

    
    return list(email_dict.values())
                


id = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

print(solution(id,report,2))
        