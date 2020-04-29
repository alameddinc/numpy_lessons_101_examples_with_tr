# -*- coding: UTF-8 -*-
import numpy as np

# created two numpy arrays with 2 x 3 x 4 items that between 0 (0 x 3) to 3 (1 x 3)
# 2 x 3 x 4 boyutunda 0 (0 x 3) ile 3 (1 x 3) arasında sayılardan oluşan 2 adet Numpy dizisi oluşturma
randomFirstArray = 3 * np.random.random([3, 4])
randomSecondArray = 3 * np.random.random([3, 4])

# two arrays Basic operations
# İki dizi için basit işlemler
resultArray = randomFirstArray + randomSecondArray
resultArray = randomFirstArray - randomSecondArray
resultArray = randomFirstArray * randomSecondArray
resultArray = randomFirstArray / randomSecondArray
resultArray = randomFirstArray + 10
resultArray = randomFirstArray - 10
resultArray = randomFirstArray * 10
resultArray = randomFirstArray / 10

# Math operations
# Matematiksel işlemler
resultArray = np.sin(resultArray)
resultArray = np.sinh(resultArray)
resultArray = np.cos(resultArray)
resultArray = np.cosh(resultArray)
resultArray = np.tan(resultArray)
resultArray = np.tanh(resultArray)
resultArray = np.log(resultArray)
resultArray = np.sqrt(resultArray)
# resultArray = np.arcsin(resultArray)
# resultArray = np.arcsinh(resultArray)
# resultArray = np.arccos(resultArray)
# resultArray = np.arccosh(resultArray)


# Vertical & Horizantal Merge
# Dikey & Yatay Birleştirme
# Don't forget to parenthize
# Dizileri Paranteze almayı unutmayın
resultArray = np.vstack((randomFirstArray, randomSecondArray))
resultArray = np.hstack((randomFirstArray, randomSecondArray))

# Logic Oprators
# Mantıksal İşlemler

# All items bigger than 5 [[True, False, ...],...]
# Tüm Değişkenler 5'den büyük mü? [[True, False, ...],...]
resultArray = randomFirstArray > 5

# Is Zero when divided by Two for All Items
# Tüm Değişkenler için İkiye bölümden kalan sıfır mıdır? (Mod2)
resultArray = randomFirstArray % 2 == 0

# Printed True Items
# Sonuca göre sayıları yazdırma
print(randomFirstArray[resultArray])
