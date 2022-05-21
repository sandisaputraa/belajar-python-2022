#latihan 8 : Program Untuk Menghitung Body Mass Index (BMI)
# Rumus untuk menghitung BMI adalah : weight /(height * height)

print("\nProgram Untuk Menghitung BMI")
weight = float(input("Masukkan Berat Badan (dalam satuan kg) :"))
height = float(input("Masukkan Tinggi Badan (dalam satuan meter)"))
hasil = float((weight/(height * height)))
print("Jadi nilai BMI adalah :",hasil)
