def solution(id_list, report, k):
    answer = []

    report_table = {}
    for id in id_list:
        if id not in report_table: 
            report_table[id] = []
    
    # 유저가 신고한 사람들 
    for sent in report:
        s = sent.split()
        reporter = s[0]
        reported_id = s[1]
        if reported_id not in report_table[reporter]:
            report_table[reporter].append(reported_id)
    
    # 신고를 받은 유저들 
    reported_id_table = dict()
    for sent in report: 
        s = sent.split()
        reporter =s[0]
        reported_id = s[1]
        if reported_id not in reported_id_table:
            reported_id_table[reported_id] = []

        if reporter not in reported_id_table[reported_id]:
            reported_id_table[reported_id].append(reporter)
    
    c = list()
    for i in reported_id_table :
        if len(reported_id_table[i]) >= k:
            c.append(i)
    
    # id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수 
    for id in id_list:
        cnt = 0 
        for i in report_table[id]:
            if i in c:
                cnt += 1 
        answer.append(cnt)
        
    return answer