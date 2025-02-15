# 필요한 라이브러리 import
import numpy as np
from collections import deque

# 주어진 map 디자인
map_design = np.array([
    [  2,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [  0,  3,  0,  4,  0,  5,  0,  6,  0,  0],
    [  0,  0,  0,  0,  7,  0,  0,  8,  0,  0],
    [  0,  9,  0, 10,  0, 11,  0, 12,  0,  0],
    [  0,  0,  0,  0, 13,  0,  0,  0, 14,  0],
    [  0, 15,  0, 16,  0, 17,  0, 18,  0,  0],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
])


def start_position(map, start, end):
    # 맵의 x축 길이와 y축 길이 계산
    # 이유 : 로봇이 맵밖으로 탈출하면 안되기때문에 계산
    # 시작 위치와 도착지를 좌표형식으로 표현할수도 있음
    # 만약 numpy array가 아닌 일반 list라면 어떻게 해야할까?
    #       정답 : max_x = len(map), max_y = len(map[0])으로 활용할수 있다.
    max_x = map.shape[0]
    max_y = map.shape[1]

    # 시작 위치와 도착지의 index를 계산
    # 이유 : index를 활용하여 시작위치와 도착위치를 좌표 형식으로 나타내기 위함
    #        예를 들어 우리 지구에서 청와대의 좌표를 특정하려면 북위 37° 32′ 01″, 동경 126° 58′ 40″와 같이 위도와 경도로 표현할수 있습니다.
    #        이처럼 프로그램에서 리스트나 numpy와 같이 나타내진 형태로 시작 위치를 알기 위해서는 index를 활용할수 있음
    for i in range(max_x):
        for j in range(max_y):
            # 이중 for문을 사용해서 x축과 y축으로 좌표를 특정
            # 첫번째 for문 : 행을 순차적으로 입력
            # 두번째 for문 : 입력된 행안에서 열방향으로 순차적으로 입력
            # 이후 아래 if문을 활용해서 시작 지점과 도착지점의 값과 동일한 인덱스를 좌표로 지정
            if map[i][j] == start:
                st_x, st_y = i, j
            if map[i][j] == end:
                ed_x, ed_y = i+1, j+1
    return bfs(map, st_x, st_y, ed_x, ed_y)

# 최단 경로를 구하기 위해서는 BFS를 사용. 이는 수업시간에도 언급
def bfs(map_design, st_x, st_y, ed_x, en_y):
    # 로봇의 이동 가능 지역을 append하기 위해 deque클래스를 초기화
    q = deque()
    # 로봇이 방문했다면 방문했다는 체크를 할수 있는 체크 배열을 생성
    # 단, 저는 본 문제에서 출발지가 2로 고정되어있고, 도착지가 3이상인 숫자임을 보았을때,
    # 전체 지도를 체크 배열로 만드는것이 아닌 출발지와 도착지까지의 배열만 사용하면 된다고 판단(capture1.png파일 참고)
    # 또한, 최단 경로를 계산하기 위해서 1인 배열로 초기화 로봇이 도착할때 마다, +1을 할 예정
    visited = np.array([[1] * en_y for _ in range(ed_x)])
    # 처음 시작지역을 이동가능 deque에 삽입
    q.append((st_x, st_y))

    
    while True:
        # 만약, stack에 아무것도 없다면, 도착지에 도착을 하였거나, 이동 가능한 지역이 없는 것이기에 반복문 종료
        if len(q) == 0:
            break

        # 로봇은 한칸씩 움직일수 밖에 없기 때문에, 로봇의 상대 좌표로 위, 아래, 오른쪽, 왼쪽으로 이동할 수 있게 방향을 지정
        # 예를 들어 로봇의 위치가 (2,3)일때 위로 이동하면? (2,4)
        direction = [(1,0), (-1,0), (0, 1), (0, -1)]
        
        # 현재의 좌표는 이동이 완료 되었기 때문에, 이동가능한 stack에서 pop
        current_x, current_y = q.popleft()
        # 현재 좌표에서 상,하,좌,우로 다 이동하기 위해 for문 사용
        # 로봇은 이동가능지역인지? 아닌지 모르기때문에, 상하좌우로 다 이동해 봐야함
        for x, y in direction:
            # 이제 이동해봅시다. 현재 좌표에서 x, y를 각각 더해주면 이동완료
            # 예를들어 현재 좌표가 (2,3)이라면, 다음 이동할 좌표는 상: (2,4), 하 : (2,2), 우: (3,3), 좌: {1,3} 
            next_x = current_x + x
            next_y = current_y + y

            # 이동한 로봇이 벽이거나, 맵 밖이라면? 그 이동된 좌표는 무시해야하되기때문에 continue
            # break는 반복문을 완전히 빠져나가기 때문에 올바르지 않음
            # 이유 : for문 이기 때문에 위로 이동했을때, 맵밖이나 벽이라면 나머지 하,좌,우는 어떤 상태인지 알수가 없음 
            if next_x < 0 or next_y < 0 or next_x >= ed_x or next_y >= en_y:
                continue
            # 그럼 이제 이동된 좌표에서 체크배열을 확인했을때, 만약 1이라면 여기는 이동 가능한 좌표구나를 판단 가능
            if visited[next_x][next_y] == 1:
                # 이동 가능한 좌표인 stack에 append
                q.append([next_x, next_y])
                # 또한 +1 까지 왜? 최단 경로를 확인할수 있기 때문에(capture2.pdf참고)
                visited[next_x][next_y] = visited[current_x][current_y] + 1
            
            # 만약에 현재 위치의 값이 3보다 크면 도착지에 도착한것이기 때문에, 반복문 종료
            if map_design[current_x][current_y] >= 3:
                break
            # 위 내용을 반복

    # 반복문이 종료되었을때, 도착지에서 체크배열이 1이라면? 아무곳도 이동을 못했다라고 판단 가능
    # 왜? 이동이 가능하면 +1씩 해주는데, +1이 안되었다면, 이동가능한곳이 아무데도 없다라는 뜻이기 때문에
    if visited[ed_x - 1][en_y - 1] == 1:
        return -1
    # 아니라면 체크배열의 값을 return하면서 종료
    else :
        return visited[ed_x - 1][en_y -1]

print(start_position(map_design, 2, 10))