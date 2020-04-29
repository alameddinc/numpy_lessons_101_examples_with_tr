# -*- coding: UTF-8 -*-
import numpy as np

# created numpy array with 2 x 3 x 4 items that between 0 (0 x 3) to 3 (1 x 3)
# 2 x 3 x 4 boyutunda 0 (0 x 3) ile 3 (1 x 3) arasında sayılardan oluşan Numpy dizisi oluşturma
randomArray = 3 * np.random.random([3, 4])

print("Array")
print(randomArray)

# Sum Rows
# Satırların Toplamı
print('# Sum Rows')
print(randomArray.sum(axis=1))

# Sum Columns
# Sütunların Toplamı
print('# Sum Columns')
print(randomArray.sum(axis=0))

# Max and Min for Rows
# Satırlarda Maksimum ve Minimum
print('Max and Min for Rows')
print(randomArray.max(axis=1))
print(randomArray.min(axis=1))

# Index of Max and Min for Rows
# Satırlar için Maksimum ve Minimum Değerlerin indexleri
print('Index of Max and Min for Rows')
print(randomArray.argmax(axis=1))
print(randomArray.argmin(axis=1))

# Max and Min for column
# Sütunlarda Maksimum ve Minimum
print('Max and Min for Column')
print(randomArray.max(axis=0))
print(randomArray.min(axis=0))

# Index of Max and Min for Rows
# Sütunlar için Maksimum ve Minimum Değerlerin indexleri
print('Index of Max and Min for Rows')
print(randomArray.argmax(axis=0))
print(randomArray.argmin(axis=0))

# Mean for Rows
# Satırların Ortalamaları
print('Mean for Rows')
print(randomArray.mean(axis=0))

# Mean for Columns
# Sütunların Ortalamaları
print('Mean for Column')
print(randomArray.mean(axis=1))

# Mean for Array
# Dizinin Ortalaması
print('Mean for Array')
print(randomArray.mean())
