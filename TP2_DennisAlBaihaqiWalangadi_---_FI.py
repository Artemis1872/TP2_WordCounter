"""
Title: Word Counter
Author: Dennis Al Baihaqi Walangadi
NPM: *redacted*
Contact: github.com/Artemis1871
"""
import matplotlib.pyplot as plt
import string
import os
import platform


def kosong():
    '''
    Mengosongkan terminal agar enak dilihat
    '''

    if platform.system() == "Windows":          # Cek apakah program berjalan di Windows
        os.system('cls')                        # Jika ya, eksekusi perintah 'cls'
    else:                                       # Jika bukan, asumsi Linux
        os.system('clear')                      # Eksekusi perintah 'clear'


def pause():
    '''
    Menjeda terminal
    '''

    if platform.system() == "Windows":                          # Cek apakah program berjalan di Windows
        os.system('pause')                                      # Jika ya, eksekusi perintah 'pause'
    else:                                                       # Jika bukan, asumsi Linux
        os.system('read -p "Press [Enter] to continue..."')     # Eksekusi perintah 'read -p'


def masukan(var):
    '''
    Memasukkan kata ke dalam list yang akan di proses.
    '''

    menu = f"{'':=<56s}" + "\nMasukkan pesan: (untuk berhenti masukkan string kosong)\n" + f"{'':=<56s}"

    kosong()                                                # Kosongkan terminal agar mudah dilihat mata

    print(menu)
    # Print menu agar sesuai
    while True:
        pesan = input("Pesan: ")                            # Loop input pesan
        if pesan == '':                                     # Loop akan berhenti jika user tidak input apa-apa
            break
        else:
            for kata in pesan.split():                      # Setiap kalimat dipisahkan melalui spasi menjadi kata
                kata = kata.strip(string.punctuation)       # Jika di kanan atau kiri kata ada tanda baca, maka dihilangkan
                if kata == '':                              # Jika hasil dari penghilangan tanda baca menghasilkan string kosong
                    continue                                # Lewati saja
                else:                                       # Jika terdapat kata
                    var.append(kata.lower())                # Ubah kata tersebut menjadi lower case dan append ke list


def bukaCekal(listCekal):
    '''
    Buka file referensi kata yang akan dicekal. Masukkan kedalam list.
    '''

    global kataCekal                                                                                # Entah kenapa tapi pycharm saranin pake ini
                                                                                                    # tapi kalau nggak pake jalan-jalan aja
    try:
        kataCekal = open("TP2-stopword.txt")                                                        # Mencoba buka file stopword
    except FileNotFoundError:                                                                       # Kalo nggak nemu
        print("File TP2-stopword.txt tidak ditemukan. Mohon periksa ulang!")                        # Print error message
        exit(1)                                                                                     # Exit dengan kode 1

    for baris in kataCekal.read().split('\n'):                                                      # Setiap kata di file tersebut,
        listCekal.append(baris)                                                                     # Dimasukan kedalam list
    kataCekal.close()                                                                               # Kalau selesai, close file tersebut


def bersihkan(listLama,listCekal):
    '''
    Membersihkan list yang ingin dibersiskan dari kumpulan kata yang ada di listCekal dan Punctuation.
    '''

    for kataCekal in listCekal:                             # Setiap kata di list kata yang akan dicekal
        for kata in listLama:                               # Setiap kata di list kata yang akan dibersikan
            if kataCekal == kata:                           # Di bandingkan, jika ternyata sama
                listLama.pop(listLama.index(kata))          # Hapus kata yang sama dari list kata yang sedang dibersihkan
    return listLama                                         # Jika sudah bersihk return list yang sudah bersih


def tokenisasi(perolehanKata, kataCekal):
    '''
    Memecah pesan yang sudah diinput dan sudah sibersihkan menjadi list.
    '''

    masukan(perolehanKata)                  # Masukan kata yang di input ke dalam list
    bukaCekal(kataCekal)                    # Masukan kata yang ingin di cekal ke dalam list
    bersihkan(perolehanKata, kataCekal)     # Bandingkan kedua list tersebut, lalu bershikan jika ada kata yang dicekal
                                            # Hasilnya akan berupa list yang tidak mengandung kata yang sudah dicekal


def hitungkata(perolehanKata,listHasil):
    '''
    Hitung kata yang ada di dalam list. Lalu sisipkan hasilnya disamping kata tersebut
    Fungsi ini memerlukan list dalam list.
    '''

    for kata in perolehanKata:                      # Setiap kata di perolehan kata
        kuantitas = perolehanKata.count(kata)       # Hitung ada berapa kata di perolehanKata
        if listHasil[0].count(kata) == 0:           # Jika belum ada kata tersebut di dalam listHasil
            listHasil[0].append(kata)               # Masukan kata tersebut kedalam listHasil
            listHasil[1].append(kuantitas)          # Bersama dengan banyaknya kata tersebut
        else:                                       # Jika sudah ada, maka lanjut ke kata yang lain
            continue
    return listHasil                                # Return list yang sudah mengandung kata dan kuantitasnya


def sediaData(data,mode=2):
    '''
    Mengubah data ke tuple agar mudah diproses tanpa mengubah isinya.
    sediaData(data,mode=2)

    data =  data yang akan dibersihkan
    mode = sorting data

    0 = Berdasarkan kuantitas kecil ke besar
    1 = Berdasarkan alfabet dari a-z
    2 = Berdasarkan urutan kata saat di input
    '''

    data = tuple(zip(data[0], data[1]))             # Ubah data ke tuple, dan beri pasangan kuantitas yang paralel dengan list sebelumnya
    if mode == 0:
        data = sorted(data, key = lambda x: x[1])   # Sort berdasarkan banyak frekuensi kata
        return data
    if mode == 1:
        data = sorted(data, key = lambda x: x[0])   # Sort berdasarkan alfabet kata-kata
        return data
    if mode == 2:                                   # Tanpa sort, data berdasarkan urutan kata saat diinput
        return data


def grafik(data):
    '''
    Menggambar grafik menggunakan matplotlib.pyplot
    '''

    plt.figure(figsize=(8, 8), dpi=80)          # Atur besar canvas default Matplotlib (640x640)px
    plt.title('Frekuensi Kemunculan Kata')      # Atur judul canvas
    plt.xlabel('Frekuensi')                     # Label sumbu x sebagai 'Frekuensi'
    plt.grid(axis='x')                          # Beri garis pada setiap titik di sumbu x, agar mudah dilihat
    plt.barh(*zip(*data), align='center')       # Tampilkan grafik bar horizontal
    plt.yticks(range(len(data)))                # Memberi titik sebanyak kuantitas data
    plt.gca().invert_yaxis()                    # Default invert y axis matplotlib
    plt.show()                                  # Tampilkan hasil grafik


def tabel(data):
    '''
    Membuat tabel ASCII mengenai distribusi frekuensi data
    '''

    pemisah = f"{'':=<40s}"                                                 # Pemisah berupa tanpa sama dengan

    kosong()                                                                # Membersihkan terminal

    # MENAMPILKAN TABEL
    print("\nDistribusi frekuensi data:")                                   # Judul tabel
    print(pemisah)
    print('{:<3s}  {:<15s}{:^30s}'.format('No', 'Kata', 'Frekuensi'))       # Header dari tabel
    print(pemisah)
    for i in range(len(data)):                                              # Memasukkan data tabel
        print('{:>3d}  {:<15s}{:^30d}'.format(i+1, data[i][0], data[i][1]))
    print(pemisah)


def main():
    '''
    Urutan proses yag akan dijalankan
    '''

    # VARIABEL YANG DIBUTUHKAN
    perolehanKata = []
    kataCekal = []
    listHasil = [[], []]

    # MULAI TOKENISASI
    tokenisasi(perolehanKata, kataCekal)

    if len(perolehanKata) == 0:                                             # Jika hasil tokenisasi tidak mempunyai data
        print("Tidak dapat menampilkan grafik karena datanya kosong.")      # Return message tidak dapat membuat grafik
    else:
        data = sediaData(hitungkata(perolehanKata, listHasil))              # Jika ada, olah data agar dapat ditampilkan
        tabel(data)                                                         # Buat tabel berdasarkan data
        grafik(data)                                                        # Buat grafik berdasarkan data

    pause()                                                                 # Ketika grafik ditutup, terminal akan berjalan.
                                                                            # Pause untuk tetap dapat melihat tabel saat grafik ditutup
    kosong()                                                                # Kosongkan terminal ketika selesai


if __name__ == "__main__":
    main()
