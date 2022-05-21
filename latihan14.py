#latihan 14
tahun=int(input('masukan tahun = '))
if(tahun%400==0):
    print("tahun",tahun,"adalah tahun kabisat.")
elif(tahun%400!=0 and tahun%100==0):
    print('tahun',tahun,'bukan tahun kabisat.')
elif(tahun%400 !=0 and tahun%100 !=0 and tahun%4==0):
    print('tahun',tahun,'adalah tahun kabisat')
elif(tahun%400 !=0 and tahun%100 !=0 and tahun%4 !=0):
    print('tahun',tahun,'bukan tahun kabisat')
