import math

def main():
    #Menginput gaji
    gaji = float(input("Masukkan gaji anda dalam setahun : "))

    #Gaji setahun dibagi 12 untuk hitungan sebulan 
    gajisebulan = math.ceil(gaji / 12)

    #Output gaji perbulan
    print("Gaji per bulan adalah:", gajisebulan)

if __name__ == "__main__":
    main()