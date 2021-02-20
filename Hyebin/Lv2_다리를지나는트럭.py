def solution(bridge_length, weight, truck_weights):
    # answer = 0
    time = 0
    br = [0] * bridge_length

    while len(br) != 0:
        time += 1
        br.pop(0)
        if truck_weights:
            if sum(br) + truck_weights[0] <= weight:
                br.append(truck_weights.pop(0))
            else:
                br.append(0)
            # print(br)
    # answer = time
    return time

bridge_length= 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))