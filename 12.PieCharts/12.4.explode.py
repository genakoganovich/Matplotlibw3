import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]
my_explode = [0.2, 0, 0, 0]

plt.pie(y, labels=my_labels, explode=my_explode)
plt.show()
