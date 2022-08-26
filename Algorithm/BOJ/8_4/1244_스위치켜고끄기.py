# 실버3. 2시간걸림

N = int(input())
arr = list(map(int, input().split()))
student_number = int(input())
student = []
for i in range(student_number):
    a = list(map(int, input().split()))
    student.append(a)

for i in range(len(student)):
    if student[i][0] == 1:
        for n in range(1, N+1):
            if n % student[i][1] == 0:
                if arr[n-1] == 1:
                    arr[n-1] = 0
                else:
                    arr[n-1] = 1

    if student[i][0] == 2:
        center_index = student[i][1]-1

        for m in list(range(N)):
            if center_index-m >= 0 and center_index+m < N:
                if arr[center_index-m] == arr[center_index+m]:
                    if arr[center_index-m] == 1:
                        arr[center_index - m] = arr[center_index+m] = 0
                    else:
                        arr[center_index - m] = arr[center_index+m] = 1
                else:
                    break
            else:
                break

if len(arr) >= 20:
    for i in range(0, len(arr), 20):
        if len(arr) - i > 20:
            for j in range(20):
                print(arr[i+j], end=' ')
            print()
        else:
            for j in range(len(arr) - i):
                print(arr[i + j], end=' ')
            print()
else:
    for i in range(len(arr)):
        print(arr[i], end=' ')



