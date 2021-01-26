# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    ans= re.sub('[^a-z0-9\-_.]', '', new_id.lower())
    ans= re.sub('\.+', '.', ans)
    ans= re.sub('^[.]|[.]$', '', ans)
    ans='a' if len(ans)==0 else ans[:15]
    ans= re.sub('^[.]|[.]$', '', ans)
    ans= ans if len(ans) > 2 else ans + "".join([ans[-1] for i in range(3-len(ans))])
    return ans

# 나중에 보기 편하라고 단계별로 적었당
