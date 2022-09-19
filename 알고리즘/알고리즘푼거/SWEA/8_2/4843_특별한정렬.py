import sys

sys.stdin = open("4843_특별한정렬.txt")

def selection_sort(a, N):
    for i in range(N-1):
        if i == 0 or i % 2 == 0:                              # i 가 0 이거나 짝수일 때는, 최대값으로 위치 바꾸기
            maxidx = i
            for j in range(i+1, N):
                if a[maxidx] < a[j]:
                    maxidx = j
            a[i], a[maxidx] = a[maxidx], a[i]
        else:                                                 # i 가 홀수일 때는 최소값으로 위치 바꾸기
            minidx = i
            for j in range(i+1, N):
                if a[minidx] > a[j]:
                    minidx = j
            a[i], a[minidx] = a[minidx], a[i]
    return f"#{test_case} {' '.join(list(map(str, a[:10])))}" # join 이용해서 출력값 맞추기

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    print(selection_sort(a, N))