import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import linalg, optimize

# Seaborn의 'tips' 데이터셋 로드
tips = sns.load_dataset("tips")

# 1. 기본 통계 출력
print("기본 통계 정보:")
print(tips.describe())

# 2. NumPy를 활용한 평균 및 분산 계산
total_bill_mean = np.mean(tips["total_bill"])
total_bill_var = np.var(tips["total_bill"], ddof=1)  # 표본 분산
tip_mean = np.mean(tips["tip"])
tip_var = np.var(tips["tip"], ddof=1)  # 표본 분산

print(f"\nTotal Bill 평균: {total_bill_mean:.2f}, 분산: {total_bill_var:.2f}")
print(f"Tip 평균: {tip_mean:.2f}, 분산: {tip_var:.2f}")

# 3. SciPy를 활용한 선형 방정식 풀이
# 선형 방정식 ax + b = y 설정 (y = tip, x = total_bill)
A = np.array([
    [np.sum(tips["total_bill"] ** 2), np.sum(tips["total_bill"])], 
    [np.sum(tips["total_bill"]), len(tips["total_bill"])]
])
B = np.array([
    np.sum(tips["total_bill"] * tips["tip"]), 
    np.sum(tips["tip"])
])

# SciPy를 사용해 방정식 풀이
a, b = linalg.solve(A, B)

print(f"\nSciPy 선형 방정식 풀이 결과: a = {a:.4f}, b = {b:.4f}")
print(f"예측된 팁 공식: tip = {a:.4f} * total_bill + {b:.4f}")

# 4. Statsmodels를 활용한 회귀 분석
X_sm = sm.add_constant(tips["total_bill"])  # 절편 추가
model = sm.OLS(tips["tip"], X_sm).fit()

print("\nStatsmodels 회귀 분석 결과:")
print(model.summary())

# 5. SciPy 최적화 문제
# 팁을 최대로 받을 수 있는 total_bill 값을 찾기 위해 최적화 문제 설정
# 목표: f(x) = - (a * x + b) 를 최소화하는 x 찾기 (팁 최대화)
objective = lambda x: -(a * x + b)
result = optimize.minimize_scalar(objective, bounds=(min(tips["total_bill"]), max(tips["total_bill"])), method='bounded')

optimal_total_bill = result.x
optimal_tip = -(result.fun)

print(f"\n최대 팁을 받을 수 있는 총 금액: {optimal_total_bill:.2f}")
print(f"예상 최대 팁: {optimal_tip:.2f}")

# 6. 데이터 시각화
plt.figure(figsize=(10, 5))
sns.scatterplot(x="total_bill", y="tip", data=tips, label="Data")
plt.plot(tips["total_bill"], a * tips["total_bill"] + b, color="red", label=f"y = {a:.2f}x + {b:.2f}")
plt.axvline(optimal_total_bill, color="green", linestyle="--", label=f"Optimal Total Bill: {optimal_total_bill:.2f}")
plt.axhline(optimal_tip, color="blue", linestyle="--", label=f"Optimal Tip: {optimal_tip:.2f}")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Total Bill vs Tip with Regression Line")
plt.legend()
plt.show()
