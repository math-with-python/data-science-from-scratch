from matplotlib import pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# 生成条形图x轴位置
xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)
plt.ylabel("所获奥斯卡金像奖数量")
plt.title("我最喜欢的电影")

plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()
