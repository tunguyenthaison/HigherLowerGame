# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dataset:

# I = [[1, 0], [0,1]]
A = [[1, 0.25], [0.25, 1]]
B = [[1, -0.25], [-0.25, 1]]
xA, yA = 0.3*np.random.multivariate_normal(mean=(5, 0), cov=A, size = 100).T
xB, yB = 0.7*np.random.multivariate_normal(mean=(-5, 0), cov=B, size = 100).T
x = xA+xB
y = yA+yB

# plot
# fig, ax = plt.subplots(figsize=(12, 6))

plt.plot(x, y , linestyle='none', marker='.')
plt.xlim([-4, 4])
plt.ylim([-4, 4])
# plt.plot( 'x_values', 'y_values', data=df, linestyle='none', marker='.')
# plt.axis('equal')
plt.savefig('foo.png')
plt.show()

