import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]
my_colors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels=my_labels, colors=my_colors)
plt.show()
