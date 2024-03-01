def main():
    #Variabel untuk menyimpan jumlah
    jumlah = 0
    
    #List untuk menyimpan angka yang dimasukkan
    angka = []
    
    #Loop tak terbatas untuk memasukkan terus angka
    while True:
        #Menginput angka dan -1 untuk menghentikannya untuk dihitung
        num = int(input("Masukkan angka (Ketik -1 untuk berhenti): "))
        
        #Mengecek apakah angka -1
        if num == -1:
            #Break jika -1 untuk keluar dari loop
            break
        
        #Jika tidak, tambahkan angka ke jumlah
        jumlah += num
        angka.append(str(num))  #Menambahkan angka ke dalam list sebagai string
    
    #Output jumlah dan urutan angka
    print(f"{jumlah} is {'+'.join(angka)}")

if __name__ == "__main__":
    main()