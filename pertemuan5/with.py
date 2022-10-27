# #Python menyediakan statement with yang dapat digunakan sebagai alternatif untuk membuka
# dan menutup file. Berikut adalah contoh kode dengan statement with untuk menulis ke sebuah
# file:
def main():
    with open('presiden.txt', 'w') as outfile:
        outfile.write('Sukarno\n')
        outfile.write('Suharto\n')
        outfile.write('B.J. Habibie\n')

main()