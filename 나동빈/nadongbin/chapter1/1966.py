# 8월 7일에 공부한거. 나동빈 챕터1, 2번째 pdf 문제.
# 내용어려움/// 이거도 승태한테 과외받음./
# 실버3

test_case = int(input())

for i in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0) 
        else:
            queue.append(queue.pop(0))






