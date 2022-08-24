import numpy as np

a = np.arange(10)**2

print(a)

# mengambil nilai / indexing
print('elemen ke 1 dari a adalah', a [0])
print('elemen ke 8 dari a adalah', a [8])
print('elemen ke terakhir dari a adalah', a [-1]) # mulai dari belakang mengambil nilainya

# slicing / mengambil rentang pada array
print('elemen dari 1-6 adalah', a [0:6]) # (start,end)
print('elemen dari 4-akhir adalah', a [3:]) # mengambil nilai dari 4 hingga dengan akhir
print('elemen dari awal-5 adalah', a [:5]) # mengambil nilai dari awal hingga dengan 5

# iterasi
for i in a:
    print('hasil =',i) # mengiterasi hasil dari a 