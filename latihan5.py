#latihan 5: # Konversi Satuan Kaki, Satuan inci terhadap sentimeter
print("Program Konversi Satuan Tinggi Badan\n")
Centimeter = float(input("Masukkan Ukuran Tinggi Badan (dalam cm):"))
print("Tinggi Badan Kamu adalah :", Centimeter, "cm")

# Satuan Kaki (ft)

feet = (0.0328084*Centimeter)
print("Dalam satuan kaki tinggi badan kamu adalah:", feet, "ft")

# Satuan Inci (inch)

inch = (0.393701*Centimeter)
print("Dalam satuan inci tinggi badan kamu adalah:", inch, "inch")
