# ValueError: x and y must have same first dimension, but have shapes

import matplotlib.pyplot as plt


# 👇️ both have a length of 4
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

plt.plot(x, y, '-', color='green')

plt.show()
plt.close()