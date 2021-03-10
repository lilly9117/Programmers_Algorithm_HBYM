def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [s.lower() for s in cities]

    if cacheSize != 0:
        for s in cities:
            if not s in cache:
                if len(cache) < cacheSize:
                    cache.append(s)
                    answer +=5
                else:
                    cache.pop(0)
                    cache.append(s)
                    answer +=5
            else:
                cache.pop(cache.index(s))
                cache.append(s)
                answer +=1
    else:
        answer += len(cities) * 5

    return answer

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))


