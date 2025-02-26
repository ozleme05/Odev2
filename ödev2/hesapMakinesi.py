def hesapMakinesi(sayi1, sayi2, işlem):
    sonuc = None  

    if işlem == '+':
        sonuc = sayi1 + sayi2
    elif işlem == '-':
        sonuc = sayi1 - sayi2
    elif işlem == '*':
        sonuc = sayi1 * sayi2
    elif işlem == '/':
        if sayi2 == 0:
            print('Bölme işlemi için ikinci sayı 0 olamaz!')
        else:
            sonuc = sayi1 / sayi2
    else:
        print("Geçersiz İşlem")

    if sonuc is not None:  
        print(f"Sonuç: {sonuc}")

sayi1 = int(input('sayi1: '))
sayi2 = int(input('sayi2: '))
işlem = input("İşlemi girin (+,-,*,/): ")  



hesapMakinesi(sayi1, sayi2, işlem)
