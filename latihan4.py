#latihan 4: Program untuk menjumlahkan bilangan bulat dari 1 sampai N
# Kita tahu bahwa rumus untuk menghitung jumlah bilangan positif adalah : (n)x(n+1)/2

print("Program Penjumlahan Bilangan Bulat\n")
n = int(input('Masukkan Bilangan Terbesar Pada Pada Deret :'))
jumlah = int(((n) * (n + 1))/2)
print("Jumlah ",n,"suku pertama bilangan adalah", jumlah)
