def asalMi(sayi):
    if sayi <=1:
        return 'Girdiğiniz sayi Asal Değildir.'
    for i in range(2,sayi):
        if sayi % i ==0:
            return 'Girdiğiniz sayi Asal Değildir.'
    return 'Girdiğiniz sayi Asaldir.'

sayi = int(input('Sayi : '))
print(asalMi(sayi))
