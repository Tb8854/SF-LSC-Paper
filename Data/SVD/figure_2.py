
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string
from matplotlib import cm

# Set up the axes with gridspec
fig = plt.figure(figsize=(10,5))
grid = plt.GridSpec(ncols=2, nrows=4, figure = fig,wspace=0.1,hspace=0.3)
plt.rcParams["font.family"] = "arial"

svd = fig.add_subplot(grid[0:4,0])

svd1 = fig.add_subplot(grid[0:1,1])
svd2 = fig.add_subplot(grid[1:2,1])
svd3 = fig.add_subplot(grid[2:3,1])
svd4 = fig.add_subplot(grid[3:4,1])

svd.text(-0.1, 1.02, string.ascii_uppercase[0], transform=svd.transAxes,
            size=25, weight='bold')

svd1.text(-0.1, 1.02, string.ascii_uppercase[1], transform=svd1.transAxes,
            size=25, weight='bold')

svd2.text(-0.1, 1.02, string.ascii_uppercase[2], transform=svd2.transAxes,
            size=25, weight='bold')

svd3.text(-0.1, 1.02, string.ascii_uppercase[3], transform=svd3.transAxes,
            size=25, weight='bold')

svd4.text(-0.1, 1.02, string.ascii_uppercase[4], transform=svd4.transAxes,
            size=25, weight='bold')


svddata = np.genfromtxt('./Smatrix.csv', delimiter=',', skip_header=0)


svd.plot([1,2, 3, 4, 5, 6, 7, 8, 9, 10], svddata, linestyle='-',color='#2A6478')
svd.set_xlabel(r'Basis Vector')
svd.set_ylabel(r'Eigenvalue')


svddata1 = np.genfromtxt('./svd1.csv', delimiter=',', skip_header=0)
svddata2 = np.genfromtxt('./svd2.csv', delimiter=',', skip_header=0)
svddata3 = np.genfromtxt('./svd3.csv', delimiter=',', skip_header=0)
svddata4 = np.genfromtxt('./svd4.csv', delimiter=',', skip_header=0)

svddata1x = svddata1[:,0]
svddata1y = svddata1[:,1]

svddata2x = svddata2[:,0]
svddata2y = svddata2[:,1]

svddata3x = svddata3[:,0]
svddata3y = svddata3[:,1]

svddata4x = svddata4[:,0]
svddata4y = svddata4[:,1]


svd1.plot(svddata1x, svddata1y,color='#2A6478',marker='o', linestyle='None', markersize=0.2)

svd2.plot(svddata1x, svddata2y,color='#2A6478',marker='o', linestyle='None', markersize=0.2)
svd3.plot(svddata1x, svddata3y,color='#2A6478',marker='o', linestyle='None', markersize=0.2)
svd4.plot(svddata1x, svddata4y,color='#2A6478',marker='o', linestyle='None', markersize=0.2)


svd1.axes.get_yaxis().set_visible(False)
svd2.axes.get_yaxis().set_visible(False)
svd3.axes.get_yaxis().set_visible(False)
svd4.axes.get_yaxis().set_visible(False)


svd1.axes.get_xaxis().set_visible(False)
svd2.axes.get_xaxis().set_visible(False)
svd3.axes.get_xaxis().set_visible(False)
svd4.set_xlabel(r'Wavelength [nm]')

fig.savefig('svd.pdf', bbox_inches="tight")
