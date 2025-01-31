def solution(bridge_length, weight, truck_weights):
    answer = 0              # 경과 시간
    total_weight = 0        # 현재 다리 위 트럭 무게의 합  
    bridge = []
    for _ in range(bridge_length):  
        bridge.append(0)    # 다리 길이만큼 0으로 채워진 큐

    while bridge:           # 다리가 빌 동안 반복
        answer += 1         # 경과 시간을 1초씩 증가가
        exited_truck = bridge.pop(0)    # 다리에서 빠져나간 트럭
        total_weight -= exited_truck    # 빠져나간 트럭의 무게를 현재 무게에서 뺀다.
        if truck_weights:               # 만약 대기 트럭이 있고,
            if total_weight + truck_weights[0] <= weight:   # 트럭의 무게를 견딜 수 있다면,
                new_truck = truck_weights.pop(0)
                bridge.append(new_truck)                    # 새 트럭이 다리에 오르고,
                total_weight += new_truck                   # 현재 무게에 올라라온 트럭의 무게를 더한다.
            else:
                bridge.append(0)        # 트럭이 못 올라오면 빈 공간을 유지한다.
    return answer


bridge_length = int(input("bridge_length: "))
weight = int(input("weight: "))
truck_weights = list(map(int, input("truck_weights: ").split()))
answer = solution(bridge_length, weight, truck_weights)
print(f"{answer}초 소요")