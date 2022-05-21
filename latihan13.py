#latihan 13
nm=float(input('panjang gelombang cahaya (nm) = '))
if(nm<=720 and nm>=620):
    print("spektrum yang terlihat adalah Red")
elif(nm<620 and nm>=590):
    print("spektrum yang terlihat adalah Orange")
elif(nm<590 and nm>=570):
    print("spektrum yang terlihat adalah Yellow")
elif(nm<570 and nm>=495):
    print("spektrum yang terlihat adalah Green")
elif(nm<495 and nm>=450):
    print("spektrum yang terlihat adalah Blue")
elif(nm<450 and nm>=380):
    print("spektrum yang terlihat adalah Violet")
else:
    print("input kamu diluar spektrum yang diketahui...!!")
