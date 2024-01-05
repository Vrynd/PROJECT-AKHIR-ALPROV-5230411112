# Impor module dan Cek Kokensi Database
import sqlite3
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Jalankan Query SELECT UPDATE dan simpan perubahan
cursor.execute("UPDATE Fauna SET asal = 'Kalimantan Timur' WHERE id_fauna = 4")
conn.commit()

# Tampilkan dalam format tabel
cursor.execute("SELECT * FROM Fauna")
dataFauna = cursor.fetchall()  # Ambil semua data dari tabel 'Fauna'

# Tampilkan data dalam format tabel dan berikan pesan
if len(dataFauna) > 0:
    print("-"*100)
    print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format("ID", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN DITEMUKAN"))
    print("-"*100)
    for value in dataFauna:
        print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(value[0], value[1], value[2], value[3], value[4],value[5]))
    else:
        print("*"*100)
        print(f"Data Fauna Yang Memiliki ID 4, Berhasil Diupdate")

# Tutup Koneksi
conn.close()