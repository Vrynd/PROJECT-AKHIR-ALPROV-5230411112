# Impor module dan Cek koneksi database
import sqlite3
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Jalankan Query SELECT ORDER BY Tahun Ditemukan secara descending
cursor.execute("SELECT * FROM Fauna ORDER BY thn_ditemukan ASC")
dataFauna = cursor.fetchall()

if len(dataFauna) > 0:
    print("-"*100)
    print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format("ID", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN DITEMUKAN"))
    print("-"*100)
    for value in dataFauna:
        print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(value[0], value[1], value[2], value[3], value[4],value[5]))
    else:
        print("*"*100)
        print("Tahun Ditemukan Telah Diurutkan, Berdasarkan dari tahun yang terlama ke terbaru")

# Tutup Koneksi
conn.close()