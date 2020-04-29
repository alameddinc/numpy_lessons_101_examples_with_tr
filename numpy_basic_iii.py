# -*- coding: UTF-8 -*-
import numpy as np

# numpy array with 2 x 3 x 4 items that between 0 to 1
# 2 x 3 x 4 boyutunda  arasındaki sayılardan oluşan numpy dizi
randomZPArray = np.random.rand(2, 3, 4)

# numpy array with 2 x 3 x 4 items with negative
# 2 x 3 x 4 boyutunda negatif dahil olacak şekilde numpy dizi
randomNPArray = np.random.randn(2, 3, 4)

# numpy array with 2 x 3 x 4 items items that between 0 to 50, items is an integer variable
# 2 x 3 x 4 boyutunda rasgele 0 ile 50 arasında tam sayılardan oluşan numpy dizi
randomIntArray = np.random.randint(0, 50, [2, 3, 4])

print (randomZPArray)
print (randomNPArray)
print (randomIntArray)
