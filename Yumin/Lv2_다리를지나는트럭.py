# https://daeunginfo.blogspot.com/2020/12/python.html

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    tot_w = 0 #현재 다리 위 모든 트럭의 무게 합
    while truck_weights:
        tot_w -= bridge.pop(0) #맨 앞 트럭 빠져나가기 or 0

        # 새로운 트럭 올릴 수 있는 경우 - 대기 트럭 올리고 다리에 추가& 모든 트럭의 무게 합 update
        if tot_w + truck_weights[0] <= weight:
            a = truck_weights.pop(0)
            bridge.append(a)
            tot_w += a

        # 새로운 트럭 올릴 수 없는 경우 - 다리 길이 유지 위해 0 append
        else:
            bridge.append(0)

        answer += 1

    answer+= bridge_length #마지막 트럭이 다리 건너는 데 걸리는 시간 고려
    return answer