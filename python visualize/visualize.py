import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("Enter the amount of points")
n = int(input())

Xs = []
Ys = []

print("Enter coordinates")
coords = []
for i in range(n):
    x, y = map(int, input().split())
    coords += [(x, y)]
    Xs += [x]
    Ys += [y]

print("Enter linear coefficients")
b, a = map(float, input().split())
line_x = np.linspace(0,10,100)
line_y = b + a*line_x

scatterdata = pd.DataFrame({'x': Xs, 'y': Ys})
linedata = pd.DataFrame({'x': line_x, 'y': line_y})

sns.set_theme(style="darkgrid")
sns.color_palette('pastel')
_, plots = plt.subplots(1, 1, figsize=(8, 8))
first_graph = sns.scatterplot(x='x', y='y', data=scatterdata, ax=plots, color='r')
first_graph.set_xticks(np.arange(0, 11))
first_graph.set_yticks(np.arange(0, 11))
second_graph = sns.lineplot(x='x', y='y', data=linedata, ax=plots, color='b')
plt.show()