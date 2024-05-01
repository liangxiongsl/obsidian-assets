import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def go(y_data):
    # 定义要拟合的函数
    def polynomial_function(x, *coefficients):
        return np.polyval(coefficients, x)

    # 生成一些随机数据
    x_data = range(100)


    # 初始猜测的多项式系数
    initial_guess = [1, 1, 1]

    # 使用 curve_fit 函数进行拟合
    fitted_coefficients, _ = curve_fit(polynomial_function, x_data, y_data, p0=initial_guess)

    # 绘制原始数据和拟合曲线
    plt.scatter(x_data, y_data, label='Data')
    plt.plot(x_data, polynomial_function(x_data, *fitted_coefficients), color='red', label='Fitted curve')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Polynomial fitting')
    plt.show()

    print("Fitted coefficients:", fitted_coefficients)
