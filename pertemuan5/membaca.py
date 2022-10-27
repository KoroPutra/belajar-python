def main():
    file = open('presiden.txt', 'r')
    isi_file = file.read()
    print(isi_file)
    file.close()

main()