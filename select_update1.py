# Impor module dan Cek Koneksi Database
import sqlite3
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Data Yang ingin dirubah
jumlah = 650
id_fauna = 10

# Jalankan Query SELECT UPDATE dan simpan perubahan
cursor.execute(f"UPDATE Fauna SET jml_skrng = {jumlah} WHERE id_fauna= {id_fauna}")
conn.commit()

# Jalankan Query SELECT
cursor.execute("SELECT * FROM Fauna")
dataFauna = cursor.fetchall()  # Ambil semua data dari tabel 'Fauna'

# Tampilkan dalam format tabel dan berikan pesan
if len(dataFauna) > 0:
    print("-"*100)
    print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format("ID", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN DITEMUKAN"))
    print("-"*100)
    for value in dataFauna:
        print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(value[0], value[1], value[2], value[3], value[4],value[5]))
    else:
        print("*"*100)
        print(f"Data Fauna Dengan ID {id_fauna} Berhasil Diupdate")
# Tutup Koneksi
conn.close()