def main():
    #Menginput angka
    angka = float(input("Masukkan angka: "))

    #Membagikan angka dengan 3
    hasil_pembagian = angka / 3

    #Output hasil dengan tiga tempat desimal
    print("Hasil Pembagian:", "{:.3f}".format(hasil_pembagian))

if __name__ == "__main__":
    main()