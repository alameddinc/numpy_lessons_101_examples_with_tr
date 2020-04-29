# -*- coding: UTF-8 -*-
import numpy as np

# Created a numpy array of 9 integers randomly between 0 and 50
# 9 adet 0 ile 50 arasındaki sayıdan oluşan oluşan numpy dizi
# np.random.randint(50) -> 0 to 50
npRandArray = np.random.randint(0, 50, 9)
npRandMultiArray = npRandArray.reshape(3, 3)

# A numpy array has been created, Items are between 10 and 100 each item is 5 more than the previous one
# 10'dan 100'e kadar 5er 5er artarak oluşan numpy dizi
npRangeArray = np.arange(10, 100, 5)
npRangeMultiArray = npRangeArray.reshape(3, 6)

print (npRandMultiArray)
print (npRangeMultiArray)

# A Numpy Array with 9 numbers that increase regularly between 0 and 100
# 0 ile 100 arasinda nizami artan 9 sayıdan olusan bir dizi
npLinSpaceArray = np.linspace(0, 100, 9)
npLinSpaceMultiArray = npLinSpaceArray.reshape(3, 3)

print(npLinSpaceMultiArray)

# A Numpy Array created with 9 Zeros
# 9 sıfırdan oluşan Numpy dizi
npZeroArray = np.zeros(9)
npZeroMultiArray = npZeroArray.reshape(3, 3)

print (npZeroMultiArray)

# A Numpy Array created with 9 Ones
# 9 Birden oluşan Numpy dizi
npOneArray = np.ones(9)
npOneMultiArray = npOneArray.reshape(3, 3)

print (npOneMultiArray)
