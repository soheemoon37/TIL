# 한 행에서 column을 선택하고 다음 행으로 갈 때마다 이 함수가 불리운다.
# chosen는 앞 선 행에서 선택된 column을 기록하고 있다.

def perm(row, chosen) :
    if row == N :                   # 마지막 열까지 왔으니
        print('row == N(3)', chosen)
        return

    for i in range(N) :             # 한 row에서는 N개을 column을 선택할 수 있다
        if i in chosen :            # 앞의 row에서 이미 이 column을 선택했었으면 이 row에서는 선택할 수 없다
            continue
        chosen[row] = i             # 이 row에서 이 column을 선택했음을 표시하고
        perm(row+1, chosen)         # 다음 row로 간다.
        chosen[row] = -1            # 이번 row에서 선택할 수 있는 것 중 하나를 처리하고 돌아왔으니,
                                    # 방금 갔다온 기록은 삭제한다.

                                    # 다른 선택하는 경우를 처리하러 가려고 한다(for loop 처음으로 가서)

N = 3
data = [['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']]
chosen = [-1 for _ in range(N)]     # 각 행에서 선택한 열을 기록하기 위함

perm(0, chosen)
