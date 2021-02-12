
import numpy as np
import matplotlib.pyplot as plt
# import data.txt
filename = 'data.txt'
dat = np.loadtxt(filename)
list1 = dat.flatten()
# creates histogram
n, bins, patches = plt.hist(list1, bins=range(4),alpha=0.7)

# plot formating options
plt.xlabel('x')
plt.ylabel('Frequency')
plt.title('Plot of the data in data.txt file')
plt.grid(axis='y', alpha=0.75)
plt.xlim(xmin=-0.5, xmax = 3.5)
plt.xticks(range(3))
# show figure (program only ends once closed
plt.show()
