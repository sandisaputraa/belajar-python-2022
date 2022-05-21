#latihan 6: Program Konversi Satuan Jarak

print("Program Konversi Satuan Jarak\n")
# ft --> inci, yard, mile, km

feet = float(input('Masukkan Satuan Jarak (dalam ft) :'))
print("Jaraknya adalah", feet, "ft")

inci = (12 * feet)
yard = (0.333333 * feet)
mile = (0.000189394 * feet)
km = (0.0003048 * feet)

print("Dalam Inci Satuan Jarak adalah :", inci, "inch")
print("Dalam yard Satuan Jarak adalah :", yard, "yard")
print("Dalam mile Satuan Jarak adalah :", mile, "mile")
print("Dalam km Satuan Jarak adalah :", km, "km")
