# 실버3. 후위표기식2
# 와 이문제 대박이네 2시간 넘게 헤맸음
# 일단은 예제2번이 문제였음 A 를 싹 다 1로 바꾸는게 문제라서
# for 문 이용해서 바꿨는데 타입에러가 뜨는거임
# 알고 보니깐 앞쪽에 식에서 만약에 10 으로 바꿨으면
# 10이 2자리니까 문제가 생긴거였음
# 그래서 조건문 하나 넣고 통과함

N = int(input())

arr = list(input())

for i in range(len(arr)):
    if len(arr[i]) == 1 and 65 <= ord(arr[i]) <= 90:
        a = input()
        b = arr[i]
        for x in range(len(arr)):
            if arr[x] == b:
                arr[x] = a

sta = []

for i in arr:
    if i.isdecimal():
        sta.append(float(i))
    else:
        if i == '*' and len(sta) >= 2:
            a = sta.pop()
            b = sta.pop()
            sta.append(a * b)
        elif i == '+' and len(sta) >= 2:
            c = sta.pop()
            d = sta.pop()
            sta.append(c + d)
        elif i == '-' and len(sta) >= 2:
            e = sta.pop()
            f = sta.pop()
            sta.append(f - e)
        elif i == '/' and len(sta) >= 2:
            g = sta.pop()
            h = sta.pop()
            sta.append(h / g)

print(f"{sta.pop():.2f}")

