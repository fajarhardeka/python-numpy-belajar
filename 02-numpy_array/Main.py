import numpy as np

# membuat vektor
a = np.array([10,11,12,13,14]) 
b = np.array([4.5 , 5.5, 6, 7, 8]) 

# vektor dengan range
c = np.arange (1,20,1) # setiap loncatan ditambah batas dan hasil nomor terakhir dikurangi pembatasnya

# vektor linear space
d = np.linspace (1,20,5) # menampilkan angka range 1 - 20 dengan range yang disebutkan (nomor akhirnya)

# array multidimensi / matriks
e = np.array ( [(1,2,3) , (4,5,6) , (7,8,9)] ) # membuat kelompok di setiap ()

# matriks dengan nilai nol
f = np.zeros ((4,5)) # membuat baris dan kolom tetapi menampilkan hanya angka 0

# matriks dengan nilai satu
g = np.ones ((5,5)) # membuat baris dan kolom tetapi menampilkan hanya angka 1

# matriks identitas
h = np.identity (5) # membuat matrik angka secara diagonal
i = np.eye (5) # membuat matrik angka secara diagonal
j = np.diag ([11,12,13,14,15,16]) # membuat matrik angka secara diagonal menggunakan angka yang sudah ditentukan


# display / menampilkan output kode
print(f)
    
 