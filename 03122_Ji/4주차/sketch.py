
Nlist =[4,1,2,1]
N = len(Nlist)
class Node:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
        
    def __repr__(self):
        return str(self.item)
    
class BinaryTree:
    def __init__(self):
        self.root = None


def make_itemlist(nums):
    nums.insert(0,0)
    item_list = []

    for i,num in enumerate(nums):
        for j in range(2**i):
            if j % 2 != 0:
                item_list.append(-num)
            else:
                item_list.append(num)
    return item_list
            
item_list =make_itemlist(Nlist)

def make_Nodelist(itemlist):
  node_list = []
  for i in itemlist:
    node_list.append(Node(i))
  return node_list

node_list = make_Nodelist(item_list)
# print(node_list[1].item)

def make_Tree(Node_list):
    global N
    tree = BinaryTree()
    tree.root= Node_list[0]
    for i,node in enumerate(Node_list[0:-(2**N)]):
        node.left = Node_list[2*i+1]
        node.right = Node_list[2*i+2]
    return tree

tree = make_Tree(node_list)
# print(tree.root.left)


# def find_Target(node):
#     if node.left.item == None:
#         if sum(answer) == target_num:
#             answer_list.append(answer)
#         return
    
#     answer.append(node.left.item)   
#     find_Target(node.left.item)
#     answer.pop()
    
#     answer.append(node.right.item)
#     find_Target(node.right.item)
#     answer.pop()

target_num = 3  # 원하는 타겟 값
answer_count = 0  # 타겟을 만족하는 경우의 수를 저장할 변수

def find_Target(node, current_sum=0):
    global answer_count

    if node is None:
        return
    
    # 현재 노드의 값을 더함
    current_sum += node.item

    # 리프 노드에 도달했을 때, 합이 target_num이면 경우의 수 증가
    if node.left is None and node.right is None:
        if current_sum == target_num:
            answer_count += 1
        return  # 리프 노드에서는 더 이상 탐색할 필요 없음

    # 왼쪽, 오른쪽 자식 노드로 탐색 진행
    find_Target(node.left, current_sum)
    find_Target(node.right, current_sum)

# DFS 실행 (트리의 루트부터 시작)
find_Target(tree.root)

# 결과 출력
print(answer_count)


# 어? 너무 비효율적임...

# 팀원들 코드 확인해보기

# 문제 그대로 구현하기 보다 쉽게 하는 방법을 찾아