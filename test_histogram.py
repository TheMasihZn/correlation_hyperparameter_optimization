import matplotlib.pyplot as plt

a= [1,2,3,4,5,6,7,8,9]
b= [5,3,4,5,3,2,1,2,3]
plt.hist2d(a, a,9, weights=b)
cb= plt.colorbar()
cb.set_label("counts in bins")
plt.show()