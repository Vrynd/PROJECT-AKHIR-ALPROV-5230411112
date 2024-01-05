# Impor Module dan Cek koneksi database
import sqlite3
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Jalankan Query SELECT SUM
cursor.execute("SELECT SUM(jml_skrng) FROM Fauna")
jumlahFauna = cursor.fetchone()[0]

print(f"Jumlah Populasi Hewan Adalah {jumlahFauna}")

# Tutup Koneksi
conn.close()

