import sys

sys.stdin = open("1213_string.txt", encoding='UTF-8')

# 고지식한 알고리즘

def BruteForce(pattern, source):
    count = 0
    for idx in range(len(source) - len(pattern) + 1):
        for j in range(len(pattern)):                   # 이거 for-else 문임.. 알아두기!!!!! break가 안되면 else로 넘어가고 다시 계속돔
            if source[idx + j] != pattern[j]:           # for 문이 다 돌아야 s로 가는거임. 그러니깐, 글자가 다 맞아야 else로 가는거니까 헷갈리지 않게 주의하기
                break
        else:
            count += 1                                  # 글자가 맞으면 count에 1 더하기
    return f'#{test_case} {count}'


for test_case in range(1, 11):
    N = int(input())
    pattern = input()
    source = input()
    print(BruteForce(pattern, source))