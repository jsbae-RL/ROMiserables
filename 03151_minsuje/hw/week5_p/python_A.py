from turtle_gui import draw_path
import turtle
import pandas as pd
import numpy as np

logistics_map = np.array([
    [  2,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [  0,  3,  0,  4,  0,  5,  0,  6,  0,  0],
    [  0,  0,  0,  0,  7,  0,  0,  8,  0,  0],
    [  0,  9,  0, 10,  0, 11,  0, 12,  0,  0],
    [  0,  0,  0,  0, 13,  0,  0,  0, 14,  0],
    [  0, 15,  0, 16,  0, 17,  0, 18,  0,  0],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
])
logistics_map_df = pd.DataFrame(logistics_map)
#맵확인
print("물류창고 맵 데이터프레임:")
print(logistics_map_df)



lhdp = draw_path(logistics_map)
lhdp.draw_move_path("green",10)
lhdp.draw_move_path("red",14)
lhdp.draw_move_path("yellow",18)

turtle.done()