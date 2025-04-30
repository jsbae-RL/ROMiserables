import torch
def make_diagonally_symmetric_matrix(n):
    matrix = torch.arange(1, n+1).repeat(n, 1)  #1,2,3,4,5,6,7,8...n을 모든행에 입력
    res_matrix=torch.triu(matrix) + torch.tril(matrix.T, diagonal=-1)
    #torch.triu(matrix) 대각선 포함 윗쪽 형태 유지 및 아래 0
    #torch.tril(matrix.T, diagonal=-1) 대각선 기준 뒤집고 행렬 대각선 미포함 유지 및 위는 0
    # 원하는 매트릭스 완성.
    return res_matrix

def Conver_onerow_matrix(matrix_n):
    matrix = make_diagonally_symmetric_matrix(matrix_n)
    one_row=matrix.view(-1)
    return one_row

def soulution(n,left,right):
    array = Conver_onerow_matrix(n)
    list_array = array.tolist()
    return list_array[left:right+1]

print(soulution(3,2,5))
print(soulution(4,7,14))