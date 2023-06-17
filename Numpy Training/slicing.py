import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("P1070566.JPG")
#rgbweight = [0.2989,0.58,0.11]
#img = np.dot(image[...,3], rgbweight)

top = img[:-2,1:-1]
left = img[1:-1,:-2]
right = img[1:-1,2:]
bottom = img[2:,1:-1]
center = img[1:-1,1:-1]

print(top.shape)
print(left.shape)
print(right.shape)
print(bottom.shape)
print(center.shape)



blurred = (top + left + bottom + right + center)/5.0
plt.imshow(img)
plt.figure()
plt.imshow(blurred)


plt.show()
