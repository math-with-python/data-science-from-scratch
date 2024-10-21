from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]


# 折线图 x轴年份，y轴GDP
plt.plot(years, gdp, color='green', marker='o', ls=':')


# 添加标题
plt.title("名义GDP")
# 给y轴添加标签
plt.ylabel("十亿美元")


plt.show()