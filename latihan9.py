#latihan 9 : unit tekanan
    
print("Program Konversi Satuan Tekanan\n")
# kilopascal --> psi, mmHg, atm

kilopascal = float(input('Masukkan Satuan tekanan (dalam kilopascal) :'))
print("tekanannya adalah", kilopascal, "kilopascal")

psi = (1000*kilopascal/(101300*14.689))
mmHg = ((1000* kilopascal/(101300*760)))
atm = ((kilopascal*1000)/(101300))

print("Dalam psi Satuan tekanan adalah :", psi,"psi")
print("Dalam mmHg Satuan tekanan adalah :", mmHg, "mmHg")
print("Dalam atm Satuan tekanan adalah :", atm, "atm")
