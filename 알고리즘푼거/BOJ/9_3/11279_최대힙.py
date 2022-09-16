import heapq

# 일단 힙큐는 기본으로 최소값을 출력하는 형태임
# 근데 마이너스를 붙여서 먼저 최소값 result 에 넣고 - 붙여서 최대값을 출력하면돼

n = int(input())
heap = []
result = []

for _ in range(n):
    data = int(input())
    if data == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, -data)

for data in result:
    print(-data)