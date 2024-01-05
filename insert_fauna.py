# Impor module dan Cek koneksi database
import sqlite3
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Jalankan Query INSERT INTO
sql = "INSERT INTO Fauna (nama_fauna, jenis, asal, jml_skrng, thn_ditemukan) VALUES (?, ?, ?, ?, ?)"
insert_data = [
    ("Harimau Jawa", "Mamalia", "Jawa", 40, 2019),
    ("Kuskus Beruang", "Mamalia", "Sulawesi", 30, 2021),
    ("Beruang Madu", "Mamalia", "Sumatera", 1000, 2020),
    ("Pesut Mahakam", "Mamalia", "Kalimantan", 100, 2021),
    ("Burung Maleo", "Burung", "Sulawesi", 7000, 2023),
    ("Macan Dahan", "Mamlia", "Sumatera", 400, 2020),
    ("Kancil", "Mamalia", "Jawa", 60, 2022),
    ("Gajah Kalimantan", "Mamalia", "Kalimantan", 1500, 2021),
    ("Elang Jawa", "Burung", "Jawa", 200, 2021),
    ("Katak Borneo", "Amfibi", "Kalimantan", 2000, 2023)
]
cursor.executemany(sql, insert_data)
conn.commit()

# Tutup koneksi
cursor.close()