def solution(citations):
    h = len(citations)

    # 모든 논문의 인용 수가 발표한 논문 수보다 많은 경우
    if min(citations) > len(citations):
        return len(citations)

    while h > 0:
        if len([x for x in citations if x >= h]) >= h:
            break
        else:
            h -= 1

    return h