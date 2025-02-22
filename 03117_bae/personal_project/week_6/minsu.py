import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from scipy.stats import linregress
import statsmodels.api as sm
import pandas as pd

# 1. Seaborn에서 제공하는 'tips' 데이터셋 불러오기
tips = sns.load_dataset('tips')

# 2. total_bill과 tip의 관계 분석 및 선형 방정식 세우기
slope, intercept, r_value, p_value, std_err = linregress(tips['total_bill'], tips['tip'])
linear_eq = f"tip = {slope:.4f} * total_bill + {intercept:.4f}"

# 3. SciPy를 사용하여 선형 방정식 풀기 (X 값으로 특정한 total_bill에 대한 tip 예측)
def predict_tip(total_bill):
    return slope * total_bill + intercept

# 4. 팁을 최대로 받을 수 있는 total_bill 금액 찾기 (최적화 문제 설정 및 해결)
def negative_tip(total_bill):
    return -predict_tip(total_bill)

result = minimize(negative_tip, x0=np.mean(tips['total_bill']), bounds=[(min(tips['total_bill']), max(tips['total_bill']))])
optimal_total_bill = result.x[0]
optimal_tip = -result.fun

# 5. 데이터 분포 시각화
plt.figure(figsize=(10, 6))
sns.scatterplot(x=tips['total_bill'], y=tips['tip'], alpha=0.6, label="Actual Data")
plt.plot(tips['total_bill'], predict_tip(tips['total_bill']), color='red', label='Regression Line')
plt.scatter(optimal_total_bill, optimal_tip, color='green', s=100, label="Optimal Total Bill")
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.title('Total Bill vs Tip Regression Analysis')
plt.legend()
plt.show()

# statsmodels를 활용한 회귀 분석
X = sm.add_constant(tips['total_bill'])  # 상수 추가
model = sm.OLS(tips['tip'], X).fit()
regression_summary = model.summary()

# 데이터프레임으로 정리
results_df = pd.DataFrame({
    'Linear Equation': [linear_eq],
    'R-squared': [r_value ** 2],
    'Optimal Total Bill': [optimal_total_bill],
    'Predicted Maximum Tip': [optimal_tip]
})

# 결과 표시
print(results_df)

'''
선형 방정식: \text{tip} = 0.1270 \times \text{total_bill} + 0.4436
결정계수 (R-squared): 0.6398 (즉, total_bill이 tip의 변동을 약 64% 설명함)
팁을 최대로 받을 수 있는 총 금액 (Optimal Total Bill): 35.26달러
예측된 최대 팁 금액: 4.92달러
'''