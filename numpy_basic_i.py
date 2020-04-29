# -*- coding: UTF-8 -*-
import numpy as np

# created a numpy array
# numpy dizi oluşturma
npArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# reshaped array
# tekrardan diziyi boyutlandırma
npMultiArray = npArray.reshape(3, 3)

# Printed Array
# Array'i yazdırma
print(npMultiArray)

# Printed Shape of Array
# Array'in Şeklini yazdırma
print(npMultiArray.shape)

# Printed Size x Size of Array
# Arrayın Boyununu yazdırma (Boyut x Boyut gibi)
print(npMultiArray.ndim)
