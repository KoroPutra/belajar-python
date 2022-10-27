import lingkaran
import persegipanjang

PILIHAN_LUAS_LINGKARAN = 1
PILIHAN_KELILING_LINGKARAN = 2
PILIHAN_LUAS_PERSEGIPANJANG = 3
PILIHAN_KELILING_PERSEGIPANJANG = 4
PILIHAN_KELUAR = 5

def tampilkan_menu():
    print('Menu')
    print('1) Luas Lingkaran')
    print('2) Keliling Lingkaran')
    print('3) Luas Persegi Panjang')
    print('4) Keliling persegi panjang')
    print('5) Keluar')

def main():
    pilihan = 0

    while pilihan != PILIHAN_KELUAR:
        tampilkan_menu()
        pilihan = int(input('Masukkan pilihan Anda: '))
        if pilihan == PILIHAN_LUAS_LINGKARAN:
            radius = float(input('Masukkan radius lingkaran: '))
            print('Luas lingkaran adalah', lingkaran.luas(radius))
        elif pilihan == PILIHAN_KELILING_LINGKARAN:
            radius = float(input('Masukkan radius lingkaran: '))
            print('Keliling Lingkaran adalah', lingkaran.keliling(radius))
        elif pilihan == PILIHAN_LUAS_PERSEGIPANJANG:
            lebar = float(input('Masukkan lebar persegi panjang: '))
            panjang = float(input('Masukkan panjang persegi panjang: '))
            print('Luas persegi panjang adalah', persegipanjang.luas(lebar, panjang))
        elif pilihan == PILIHAN_KELILING_PERSEGIPANJANG:
            lebar = float(input('Masukkan lebar persegi panjang: '))
            panjang = float(input('Masukkan panjang persegi panjang: '))
            print('Keliling persegi panjang adalah', persegipanjang.keliling(lebar, panjang))
        elif pilihan == PILIHAN_KELUAR:
            print('Keluar dari program')
        else:
            print('Error: pilihan tidak valid.')

main()