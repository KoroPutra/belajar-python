def main():
    nama1 = input('Masukkan nama 1: ')
    nama2 = input('Masukkan nama 2: ')
    nama3 = input('Masukkan nama 3: ')

    outfile = open('nama.txt', 'w')
    outfile.write(nama1 + '\n')
    outfile.write(nama2 + '\n')
    outfile.write(nama3 + '\n')

    outfile.close()

    print('Data ditulis ke file nama.txt')
    print()

main()