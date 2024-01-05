# Impor module Cek koneksi database
import sqlite3
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Jalankan Query SELECT WHERE Jumlah yang kurang dari 1000
cursor.execute("SELECT * FROM Fauna WHERE jml_skrng <= 1000")
dataFauna = cursor.fetchall()

# Tampilkan dalam format tabel
if len(dataFauna) > 0:
    print("-"*100)
    print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format("ID", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN DITEMUKAN"))
    print("-"*100)
    for value in dataFauna:
        print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(value[0], value[1], value[2], value[3], value[4],value[5]))
    else:
        print("*"*100)
        print("Data diatas, Berdasarkan Jumlah Hewan yang Kurang dari 1000")

# Tutup Koneksi
conn.close()