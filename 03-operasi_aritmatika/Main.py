import numpy as np

#belajar aritmatika pada numpy

# list python
a = [10,11,12,13,14,15]
b = [16,17,18,19,20,21]

# numpy array
anp = np.array([11,12,13,14,15])
bnp = np.array([5,6,7,8,9])

# ELEMENT WISE OPERATION
# PENJUMLAHAN
hasil = a + b # menambahkan list bukan setiap komponen karena bukan array
hasil = anp + bnp # menambahkan komponen di dalam array

# PENGURANGAN
hasil = anp - bnp #mengurangi komponen di dalam array

# PEMBAGIAN
hasil = anp / bnp #membagi komponen di dalam array

# PERKALIAN
hasil = anp * bnp #mengkalikan komponen di dalam array

# EKSPONEN
hasil = anp ** bnp #perpangkatan komponen di dalam array

# MODULUS
hasil = anp % bnp # komponen di dalam array

# display hasil
print (hasil)