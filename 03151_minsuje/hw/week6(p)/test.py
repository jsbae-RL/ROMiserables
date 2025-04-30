import numpy as np
import pandas as pd
import seaborn as sns
from scipy.optimize import curve_fit

# Seaborn의 tips 데이터셋 로드
df = sns.load_dataset("tips")

# 독립변수: 총 금액(total_bill), 종속변수: 팁(tip)
X = df["total_bill"].values
y = df["tip"].values

# 팁을 예측할 선형 함수 정의
def linear_model(x, a, b):
    return a * x + b

# 최적의 계수 찾기
params, _ = curve_fit(linear_model, X, y)
a_opt, b_opt = params

# 최대 팁을 받을 수 있는 총 금액 계산
max_total_bill = X.max()
max_tip = linear_model(max_total_bill, a_opt, b_opt)
 
print(f"최대 팁을 받을 수 있는 총 금액: {max_total_bill:.2f}")
print(f"예상 최대 팁: {max_tip:.2f}")
