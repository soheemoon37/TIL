n, k = map(int, input().split())
key = list(map(int, input().split()))

key.sort(reverse=True)                    # 내림차순 정렬
cha = []                                  # 키차이 리스트
for i in range(len(key)-1):
    cha.append(key[i] - key[i+1])

cha.sort(reverse=True)

print(sum(cha[k-1:]))                     # 경계가 (k-1) 개라서 앞에꺼 (k-1) 개 지우고 합하면 됨