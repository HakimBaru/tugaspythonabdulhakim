def main():
    #Menginput Angka
    angka = float(input("Masukkan Angka: "))

    #Mengecek apakah Small,Large atau Medium
    if angka < 100:
        print("Small")
    elif angka > 200:
        print("Large")
    else:
        print("Medium")

if __name__ == "__main__":
    main()