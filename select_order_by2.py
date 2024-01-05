# Impor module dan Cek koneksi database
import sqlite3
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Jalankan Query SELECT ORDER BY Jumlah sekarang secara Descending
cursor.execute("SELECT * FROM Fauna ORDER BY jml_skrng DESC")
dataFauna = cursor.fetchall()

if len(dataFauna) > 0:
    print("-"*100)
    print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format("ID", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN DITEMUKAN"))
    print("-"*100)
    for value in dataFauna:
        print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(value[0], value[1], value[2], value[3], value[4],value[5]))
    else:
        print("*"*100)
        print("Jumlah Fauna Sekarang, Telah Diurutkan Berdasarkan dari yang terbanyak ke paling sedikit")

# Tutup Koneksi
conn.close()