def solution(record):
    answer = []
    
    id_hash = {}

    for r in record:
        sent = list(r.split())
        status = sent[0]
        uid = sent[1]
        if status != 'Leave':
            if uid not in id_hash:
                id_hash[uid] = sent[2]
            else:
                id_hash[uid] = sent[2]
    
    for r in record:
        sent = list(r.split())
        status = sent[0]
        uid = sent[1]
        if status == "Leave":
            answer.append(id_hash[uid]+"님이 나갔습니다.")
        elif status != "Change":
            answer.append(id_hash[uid]+"님이 들어왔습니다.")

    return answer