import matplotlib.pyplot as plt
import numpy as np
 
# Generate random 2D data for hexbin plot
x = np.random.randn(1000)
y = 2 * x + np.random.normal(size=1000)
 
# Creating a 2D histogram (hexbin plot)
plt.hexbin(x, y, gridsize=30, cmap='Blues')
 
# Adding labels and title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('2D Histogram (Hexbin Plot)')
 
# Adding colorbar
plt.colorbar()
 
# Display the plot
plt.show()