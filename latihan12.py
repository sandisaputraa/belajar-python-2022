#latihan 12
Magnitude=float(input('kekuatan gempa (Magnitude) = '))
if(Magnitude>=10.0):
    print("Gempa tersebut adalah jenis gempa Meteoric")
elif(Magnitude>=8.0):
    print("Gempa tersebut adalah jenis gempa Great")
elif(Magnitude>=7.0):
    print("Gempa tersebut adalah jenis gempa Major")
elif(Magnitude>=6.0):
    print("Gempa tersebut adalah jenis gempa Strong")
elif(Magnitude>=5.0):
    print("Gempa tersebut adalah jenis gempa Moderate")
elif(Magnitude>=4.0):
    print("Gempa tersebut adalah jenis gempa Light")
elif(Magnitude>=3.0):
    print("Gempa tersebut adalah jenis gempa Minor")
elif(Magnitude>=2.0):
    print("Gempa tersebut adalah jenis gempa Very minor")
else:
    print("Gempa tersebut adalah jenis gempa Micro")
