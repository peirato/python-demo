# https://zhuanlan.zhihu.com/p/33879170 实践部分
# 实例：有20名学生，研究这些学生在考前复习时间与得到的成绩直接的相关关系

from collections import OrderedDict
from sklearn.model_selection import train_test_split
# from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

examDict = {
    '学习时间': [0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25,
             2.50, 2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50],
    '分数': [10, 22, 13, 43, 20, 22, 33, 50, 62,
           48, 55, 75, 62, 73, 81, 76, 64, 82, 90, 93]
}

examOrderDict = OrderedDict(examDict)

exam = pd.DataFrame(examOrderDict)

exam_X = exam['学习时间']
exam_Y = exam['分数']

# 2.绘制散点图
# plt.scatter(exam_X, exam_Y, color='green')
# plt.ylabel('scores')
# plt.xlabel('Times(h)')
# plt.title('Exam Data')

# 3.划分训练集与测试集
X_train, X_test, Y_train, Y_test = train_test_split(exam_X,exam_Y, train_size = 0.8)

# 导入线性回归

# 改变一下数组的形状 sklearn 要求输入的特征为二维数组类型
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

# 创建一个模型
model = LinearRegression()
# 训练一下
model.fit(X_train, Y_train)

# 线性回归方程一般为 y=a+bx
# b为斜率model.coef_，a为截距intercept_

a = model.intercept_
b = model.coef_
a = float(a)
b = float(b)

# 3.1 绘制散点图
plt.scatter(exam_X,exam_Y,color='green',label='train data')
plt.ylabel('scores')
plt.xlabel('times(h)')

# 绘制最佳拟合曲线
Y_train_pred = model.predict(X_train)
plt.plot(X_train,Y_train_pred,color='black',label='best line')

plt.legend(loc=2)


if __name__ == '__main__':
    # print(exam.head())
    # 2. 通过画图判断适不适合用线性回归模型。
    # plt.show()

    # 3.
    print('该模型的简单线性回归方程为y = {} + {} * x'.format(a, b))

    plt.show()
