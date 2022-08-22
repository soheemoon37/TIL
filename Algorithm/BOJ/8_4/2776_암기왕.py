# 8/22. 실버4
# 이진탐색

def binary_search(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:                        
        center = (start+end) // 2              
        if a[center] == key:                   
            return 1
        elif a[center] < key:                  
            start = center + 1
        else:                                  
            end = center - 1
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    M = int(input())
    arr2 = list(map(int, input().split()))
    for i in arr2:
        print(binary_search(arr, i))
