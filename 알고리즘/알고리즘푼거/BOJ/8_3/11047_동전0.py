# 8/15. 실버4. 동전0. 11047번
# 오 내가 동전 문제를 풀 수 있었다니 ㅎㅎㅎ 캬
# 일단 K보다 큰지 작은지로 나누고 작으면 몫만큼 곱한거를 더해줌
# 그리고 count 세고 K에다가 더한 값만큼 빼줘서 또 나머지에서 비교해야됨.

N, K = list(map(int, input().split()))
list1 = []
for n in range(N):
    a = int(input())
    list1.append(a)
val = 0
cnt = 0
for i in range(N-1, -1, -1):
    if list1[i] > K:
        continue
    if list1[i] <= K:
        val = val + list1[i] * (K // list1[i])
        cnt += K // list1[i]
        K -= list1[i] * (K // list1[i])
        if K == 0:
            print(cnt)

