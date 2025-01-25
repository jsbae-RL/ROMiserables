'''중요한 도로 코드 작성
작성 사유 : ROKEY 스터디 코드 리뷰용 코드 작성
작성자 : 제민수
진행하는곳 : ROKEY 3기 스터디 중
작성 날짜 :2025.01.19~
ver : 2.0ver
작성 언어 :python
이외 프로그램 작성 중 정리 문서는 prepare2slove_program 문서를 참조 한다.
 - 코드 작성의 전반적인 방향성, 변수 기록 등등 참고 자료로 작성함.
 버전 1은 일반 테스트 4개는 통과 하였으나 제출 및 풀이에서 시간 초과라는 결과와 실패 등이 포함되어 나왔다.
 이에 대한 문제를 해결해 보고자 2.0ver으로 관리 해보고자 한다.
'''

## 아직 수정 못함함

class ImportRoad():
    """
    n개의 이동 지점과 도로의 정보(도로의 길이, 교통량)를 입력받아 최단 거리를 계산
    또한 계산된 최단 거리가가 교통량의 변화에 따라 최단 거리가 바뀌는 것을 찾아 최단거리에
    영향을 주는 도로를 출력 하는 프로그램.
    """
    #고정 변수 선언
    __MAX_LOCATION_NUM = 50000
    __MIN_LOCATION_NUM = 2
    __MAX_ROADS_LEN = 200000
    __MIN_U_POINT = 1
    __MIN_V_POINT = __MIN_U_POINT+1
    __MIN_ROAD_COST = 1
    __MAX_ROAD_COST = 10**9
    __MIN_TRAFFIC = 0
    __MAX_TRAFFIC = 10**9

    ##### 생성자 최단 경로 자체는 필요 없으나 만드는 사람 입장에서 최단 경로도 확인 하고 싶을때가 있을거라 생각되서 추가함.
    def __init__(self,location_num:int, roads:list):
        '''초기화
        location_num : 이동 가능한 지점의 수 2보다 크고 50000보다 작음
        roads : 도로의 정보를 담은 리스트[[u 지점, v 지점, 도로의 이동 시간 비용, 도로의 트레픽],...]
        이외 고정 변수 혹은 내부에서 사용될 변수 선언 및 초기 맵 제작 함수 동작
        '''
        #입력 변수
        self.location_num = location_num
        self.roads = roads

        #입력 변수에 따라 변하는 고정 변수
        self.__MIN_ROADS_LEN = location_num-1
        self.__MAX_V_POINT = location_num
        self.__MAX_U_POINT = location_num-1

        # 맵그리기용 빈 맵 생성
        self.road_map = {location:[] for location in range(1, self.location_num+1)}    #1 부터 n까지 빈 리스트 생성

        #맵 생성
        self.__map_maker()
    
    
    ### 맵 그리기 함수
    def __map_maker(self):
        '''맵그리기기(클래스 내부에서만 쓰는 함수)
        함수이름에 _를 두개 쓰면 외부에서 호출이 불가능
        '''
        self.road_map = {location:[] for location in range(1, self.location_num+1)}    #다시 그릴때 초기화 되야함.
        for u_point, v_point, road_cost, traffic in self.roads:
            self.road_map[u_point].append((v_point, road_cost+traffic))  #도로 길이시간에 트래픽을 더함
            self.road_map[v_point].append((u_point,road_cost+traffic))   #양방향이므로 반대 포인트에서 오는것도 저장
    

    ### 최단 경로 찾기 함수
    def __shortest_path(self):
        '''최단 시간의 경로(들) 찾기(클래스 내부에서만 쓰는 함수)
        현재의 최단 경로와 걸린 시간 값을 알아야 하나의 도로의 traffic이 변경 되었을때 최단 경로의 변화를 찾을 수 있다.
        현재 함수에서 다익스트라 알고리즘 흐름은 다음과 같다.
        초기 큐를 생성하고 큐의 요소가 빌때까지 아래내용을 반복한다.
        큐에서 가장 작은 누적 시간을 가진 값을 꺼내서 현재 지점으로 설정한다.
        현재 지점에 인접한 지점을 탐색 하고 그 지점을 큐에 추가한다.

        '''
        #다익스트라 알고리즘을 이용하여 최단 시간을 알아야 해서 경로의 최단시간만 알면 됨
        
        #queue의 역할을 할 변수 location_info 작성-시간과 지역 값을 확인하며 리스트에 튜플로 작성한 이유는 임의로 변경 하면 안되기때문
        
        # 최단 시간 변수
        #shorest_time 에 location키의 벨류 값은 short_time의 최대값을 넣어야 최초 비교때 최솟 값을 넣을 수 있음
        #따라서 도로의 최소수(1-2-3-4-5이런식으로 하나씩만 연결됬고 모든 도로를 지나야 될때 이게 제일 큰값임)*2*트레픽 최대값을 넣어줌.
        shortest_time = {location: self.__MIN_ROADS_LEN*2*ImportRoad.__MAX_TRAFFIC for location in range(1, self.location_num + 1)}  # 최단 시간 초기화 내부의 키를 location이라 칭한것은 해당 위치까지 가는 최단 시간을 찾는 것이기 때문
        shortest_time[1] = 0  #1번지점에서 1번지점 이동 시간은 0임

        # 선언된 값 자체가 변경되면안됨. queue의 역활로서 삭제되거나 추가될 순 있어도 들어온 값 자체가 수정 되어서는 안됨  
        location_info =  [(0,1)] #시간, 지역 변수 초기화 최초엔 1번 위치에서 0시간소모 경로는 1만 통과 했으므로
        
        #queue 역할을 하는 locationvector의 요소가 없을때 while문은 실행되지 않는다.
        while location_info:
            #location_info에서 가장 작은 누적 시간 찾기
            min_index_num = 0       #location_info에서 가장 작은 누적시간을 가진 index를 찾기위해 해당 인덱스 초기화
            for i in range(1,len(location_info)):
                if(location_info[i][0]<location_info[min_index_num][0]):
                    min_index_num = i   #가장 작은 누적시간을 가질수있는 index값을 for문을 통해 찾음.
            #가장 작은 누적 시간을 가진 튜플을 현재 시간과 현재 지점으로 저장하고 큐에서 제거
            current_time , current_location = location_info.pop(min_index_num)  #pop은 내장 함수로 해당 인덱스의 값을 리턴하고 변수 내부에서 해당 인덱스 삭제를 함.
            # 만약 self.shortest_time[curret_location]에 저장된 값이 current_time보다 작으면 아래 동작을 수행 할 필요가 없음
            # 같은 경우는 다른 경로 일 수도 있으니 할 이유는 있음.
            if(current_time>shortest_time[current_location]):
                continue
            
            #현재와 인접한 노드를 탐색해서 queue즉 location_info에 새로운 경로를 추가해야 한다.
            #새로운 지역 탐색
            for neighbor_location, move_cost in self.road_map[current_location]:
                new_time = current_time+move_cost   #새로운 경로의 시간
                #새로운 경로의 시간이 짧은경로 시간에 저장된 값보다 작으면 시간을 갱신해 주고 location_info에 새로운 경로 시간과 지역을 저장
                if new_time < shortest_time[neighbor_location]:
                    shortest_time[neighbor_location] = new_time
                    location_info.append((new_time, neighbor_location))
        #위와 같이 queue(location_info)에 저장된 값을 꺼내어 지역과 시간값을 근처 지역과 총걸린 시간을 더해가면서 반복하여
        #location_info에 더이상 새로운 이동경로 시간과 근처 지역에 대한 정보를 저장 하지 못하면 결국은 location_info의 요소는 모두 비어버리고
        #sortest_time에 location_num를 키값으로 넣으면 location의 마지막 번호 까지의 최단 시간을 불러 올수 있다.
        return shortest_time[self.location_num]
        #해당값을 통해 최초 시점 최단 시간과, 트레픽 변경으로 인한 최단 시간이 변경되는지 비교를 통해 도로 번호를 찾는 함수에 가져다 주면
        #목표 출력에 도달 한다.
    
    
    ### 트레픽 변경시 최단 시간 변경에 영향을 주는 도로 출력 함수
    def find_affected_roads(self):
        '''트레픽 변경에 따라 최단시간이 바귀는 도로 번호 찾기 함수
        __shortest_path를 이용하여 최초 최단 시간을 찾고
        for문을 통해  트레픽값을 0 과 __TRAFFIC_MAX값으로 변경한 도로정보를 수정하여 계산되어 나온 값이 최초 시간과 다르다면
        해당 도로는 영향을 주는 도로로 저장하고 최종 적으로 찾은 모든 영향을 주는 도로를 return 하면 끝
        '''
        affected_roads = []
        #최초 최단 시간
        first_short_time = self.__shortest_path()
        # 각도로의 트래픽을 0 또는 최대 값으로 변경하여 비교하여 최단 시간이 변경되면 해당 도로번호를 affected_roads에 저장한다.
        # enumeraten으로 for문 리스트를 하면 키값으로 index를 생성할 수 있고 해당 index는 for문을 돌때 마다 1씩 증가한다.
        for index_num,(u_point,v_point,road_cost,traffic)  in enumerate(self.roads):
            #traffic을 최소 값으로 변경 했을때
            self.roads[index_num][3] = ImportRoad.__MIN_TRAFFIC    #traffic의 값을 최솟값으로 변경
            self.__map_maker()                                     #변갱된 맵 적용
            update_short_time = self.__shortest_path()             #변경된 최단 시간 값 저장
            
            if first_short_time != update_short_time:       #최초 최단 시간과 업데이트된 최단 시간이 다르면 영향을 주는 도로임
                affected_roads.append(index_num+1)          #index_num+1이 도로의 번호임 index_num은 0부터 시작하는데 해당 자리가 1번 도로 에 관한거 같이 1씩 증가함

            #traffic을 최대 값으로 변경 했을때
            self.roads[index_num][3] = ImportRoad.__MAX_TRAFFIC    #traffic의 값을 최솟값으로 변경
            self.__map_maker()                                     #변경된 맵 적용
            update_short_time = self.__shortest_path()             #변경된 최단 시간 값 저장

            if first_short_time != update_short_time:       #최초 최단 시간과 업데이트된 최단 시간이 다르면 영향을 주는 도로임
                affected_roads.append(index_num+1)          #index_num+1이 도로의 번호임 index_num은 0부터 시작하는데 해당 자리가 1번 도로 에 관한거 같이 1씩 증가함

            self.roads[index_num][3] = traffic      #기존의 값으로 변경해줘야 다음 도로 확인때 문제가 발생하지 않음.
        affected_roads = list(set(affected_roads))  #중복 제거거
        #만약 경로에 영향을 미치는 도로가 없으면 affected_roads는 [-1]값을 가지고 반환 되야함
        if not affected_roads:
            affected_roads.append(-1)
        #이제 모든 과정을 마쳤으니 affected_roads를 반환하면 끝
        return affected_roads

def solution(n, roads):
    city = ImportRoad(n,roads)
    answer = city.find_affected_roads()
    return answer


roads_1 = [
    [1, 2, 10, 0], [2, 4, 8, 0], [1, 3, 9, 0], [3, 4, 9, 0], [3, 5, 10, 6], [2, 5, 10, 2], [4, 5, 2, 0]
]
n_1 = 5

roads_2 = [
    [1, 2, 10, 10], [2, 3, 10, 10], [3, 4, 10, 10]
]
n_2 = 4

roads_3 = [
    [1, 2, 5, 0], [2, 4, 5, 0], [1, 3, 5, 0], [3, 4, 5, 0]
]
n_3 = 4

roads_4 = [
    [1, 2, 5, 0], [2, 4, 5, 0], [1, 3, 5, 0], [3, 4, 5, 0], [1, 4, 5, 5]
]
n_4 = 4

# 결과 출력
print(solution(n_1, roads_1))

print(solution(n_2, roads_2))

print(solution(n_3, roads_3))

print(solution(n_4, roads_4))