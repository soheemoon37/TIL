# whiteBall_x, whiteBall_y : 흰 공의 X, Y 좌표를 나타내기 위해 사용한 변수
whiteBall_x = balls[0][0]
whiteBall_y = balls[0][1]

# targetBall_x, targetBall_y : 목적구의 X, Y 좌표 나타내는 변수
targetBall_x = balls[1][0]
targetBall_y = balls[1][1]

# width, height : 목적구와 흰 공의 X 좌표 간의 거리, Y 좌표 간의 거리
width = abs(targetBall_x - whiteBall_x)
height = abs(targetBall_y - whiteBall_y)

# 목적구가 흰 공의 우측, 일직선상에 위치했을 때
if whiteBall_y == targetBall_y and whiteBall_x < targetBall_x:
    angle = 90

# distance : 두 점(좌표) 사이의 거리를 계산
distance = math.sqrt(width**2 + height**2)

# power : 거리 distance 에 따른 힘의 세기를 계산
power = distance * 0.5
