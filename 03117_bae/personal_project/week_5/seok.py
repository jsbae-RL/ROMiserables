from collections import deque

def bfs(x, y, field, visited):
    """BFS를 사용하여 같은 색의 뿌요를 찾고 그룹을 반환"""
    queue = deque([(x, y)])
    color = field[x][y]
    positions = [(x, y)]
    visited[x][y] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and field[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))
                positions.append((nx, ny))
    
    return positions

def apply_gravity(field):
    """중력을 적용하여 뿌요를 아래로 내림"""
    for col in range(6):
        queue = deque()
        # 아래에서부터 뿌요들을 큐에 저장
        for row in range(11, -1, -1):
            if field[row][col] != '.':
                queue.append(field[row][col])
        
        # 다시 아래에서부터 채우기
        for row in range(11, -1, -1):
            if queue:
                field[row][col] = queue.popleft()
            else:
                field[row][col] = '.'

def puyo_puyo(field):
    """연쇄반응을 수행하고 총 연쇄 횟수를 반환"""
    chain_count = 0
    
    while True:
        visited = [[False] * 6 for _ in range(12)]
        to_remove = []
        
        # 터질 뿌요 그룹 찾기
        for i in range(12):
            for j in range(6):
                if field[i][j] != '.' and not visited[i][j]:
                    group = bfs(i, j, field, visited)
                    if len(group) >= 4:
                        to_remove.extend(group)
        
        # 터질 뿌요가 없다면 종료
        if not to_remove:
            break
        
        # 뿌요 터뜨리기
        for x, y in to_remove:
            field[x][y] = '.'
        
        # 중력 적용
        apply_gravity(field)
        
        # 연쇄 횟수 증가
        chain_count += 1
    
    return chain_count

# 입력 받기
field = [list(input().strip()) for _ in range(12)]

# 결과 출력
print(puyo_puyo(field))