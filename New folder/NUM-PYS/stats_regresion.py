import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
study_hours=np.linspace(1,10,50)
exam_scores=8.5*study_hours+ 15+np.random.normal(0,5,50)
m,c=np.polyfit(study_hours, exam_scores,1)
trend_line=m*study_hours+c
plt.figure(figsize=(9,6))
plt.scatter(study_hours,exam_scores, color='royalblue')
plt.plot(study_hours,trend_line, color='crimson', linestyle='--',linewidth=2,label=f'Trend Line:y={m:2f}x+{c:2f}')
plt.title('Data Science:Linear Regression & Correlation',fontsize=14,fontweight='bold')
plt.xlabel('Study Hours',fontsize=12)
plt.ylabel('Exam Score', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True,linestyle='--',alpha=0.6)
plt.show()