def main():
    #Menginput angka
    angka = int(input("Masukkan angka: "))

    #Variabel untuk menyimpan jumlah
    jumlah = 0
    #List untuk menyimpan deret angka
    urutan = []

    #Loop untuk menjumlahkan angka dari 1 hingga bilangan yang diinput
    for i in range(1, angka + 1):
        jumlah += i
        # enambahkan angka ke dalam list deret angka
        urutan.append(str(i))

    #Output hasil beserta deret angkanya
    print(f"{jumlah} is ({'+'.join(urutan)})")

if __name__ == "__main__":
    main()