# 9/4. 11866. 실버5. 요세푸스문제0

N, K = map(int, input().split())
queue = list(range(1, N+1)) # 처음 큐에 집어넣어진 사람들

queue2 = [] # 제거된 사람들(요세푸스 순열)

while True:
    if len(queue) == 0:
        break
    for i in range(K-1):
        if len(queue) != 1:
            a = queue.pop(0)
            queue.append(a)
            # print(queue)
            # print(queue2)
        else:
            break
    b = queue.pop(0)
    queue2.append(b)
print("<", ', '.join(str(i) for i in queue2), ">", sep = '')
    