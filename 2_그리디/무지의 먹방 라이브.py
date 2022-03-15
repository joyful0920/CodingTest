import heapq

def solution(food_times, k):
    
    # 네트워크 장애시간(멈춘 시간)보다 전체 음식을 먹는 시간이 짧은 경우
    if sum(food_times) <= k:
        return -1
    
    # 우선 순위 큐를 활용하여 가장 빨리 먹을 수 있는 음식부터 제외
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1)) # 튜플 형태로 해당 음식의 먹는 데 필요한 시간과 순번 삽입
        
    time = 0 # 현재까지 먹는 데 사용한 시간
    pre = 0 # 다 먹은 음식 중 가장 마지막 음식의 시간
    length = len(food_times) # 음식의 (남은) 개수
    
    while (q[0][0] - pre) * length <= k - time: # (현재 음식 시간 - 이전에 다 먹은 음식 시간) * 현재 음식 개수 <= k - 현재까지 걸린 시간
        now = heapq.heappop(q)[0]
        time += (now - pre) * length
        length -= 1
        pre = now
        
    result = sorted(q, key=lambda x:x[1])
    answer = result[(k - time) % length][1]
    return answer