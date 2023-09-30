import string
abjad = string.printable

def enkrip(pesan) :
    global abjad
    
    key = int (input('Masukan Key               : '))
    cipher = ''#menampilkan chiper enkripsi sesuai kaidah chiper caesar
    for i in pesan:
        if i in abjad:
            k = abjad.find(i) #menentukan variabel sebelumnya yang sudah dijadikan pemanggil
            k = (k + key)%100
            cipher = cipher+abjad[k]
        else:
            cipher = cipher + i
    return cipher
    

def deskrip(cipher) :
    global abjad
    key = int (input('Masukan Key               : '))
    pesan = '' #menampilkan pesan deskripsi sesuai kaidah cipher caesar
    for i in cipher:
        if i in abjad:
            k = abjad.find(i)
            k = (k - key)%100
            pesan = pesan+abjad[k]
        else:
            pesan = pesan + i
    return pesan

if __name__ == '__main__':
    print ('-----------------------------------')
    print ('    Nama        : Munis Zulhusni   ')
    print ('    Nim         : A11.2021.13693   ')
    print ('    Kelas       : A11.4302         ')
    print ('-----------------------------------')    

    option = int (input ('1. Enkripsi\n2. Deskripsi\nPilih Option              : '))
    if option == 1:
        pesan = input ('Masukan pesan (Plaintext) : ')
        print(enkrip(pesan))
    elif option == 2:
        cipher = input ('Masukan pesan (Chipertext): ')
        print(deskrip(cipher))
    else:
        print ('TIDAK VALID! PILIH OPSI LAIN!')                          