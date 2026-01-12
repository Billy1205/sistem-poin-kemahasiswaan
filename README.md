## Student Point System (SPK) Application
Aplikasi Sistem Poin Kemahasiswaan (SPK) adalah sebuah prototipe sistem manajemen data poin mahasiswa yang dirancang untuk mempermudah proses input, pengelolaan, dan rekapitulasi data partisipasi kegiatan mahasiswa. Aplikasi ini mengimplementasikan konsep CRUD (Create, Read, Update, Delete) yang terintegrasi langsung dengan database relasional.

## Fitur Utama
- Sistem Login Multi-user: Membedakan hak akses antara Mahasiswa, Staff, dan Admin.
- Manajemen Data (Admin): Kemampuan untuk menambah, melihat, mengedit status kegiatan, serta menghapus data mahasiswa atau staff.
- Dashboard Mahasiswa/Staff: Menampilkan profil pengguna dan daftar kegiatan (events) yang tersedia atau telah diikuti.
- Visualisasi Rekapitulasi: Menampilkan persentase kehadiran mahasiswa dan staff dalam suatu kegiatan menggunakan grafik lingkaran (pie chart) secara real-time.
- Validasi Input: Dilengkapi dengan pengecekan format tanggal, jam, nilai desimal, dan verifikasi data unik (ID/Nama) untuk menjaga integritas data.

## Teknologi yang Digunakan
- Bahasa Pemrograman: Python.
- Antarmuka Pengguna (GUI): Tkinter.
- Database: MySQL (melalui library pymysql).
- Visualisasi Data: Matplotlib (untuk grafik rekapitulasi).
- Struktur Data: Penggunaan tabel relasional dengan hubungan Many-to-Many melalui tabel perantara (Log Table).

## Struktur Database (ERD)
Proyek ini menggunakan 5 tabel utama:
- Mahasiswa: Menyimpan data identitas dan total poin.
- Staff: Menyimpan data identitas staff.
- Events: Menyimpan detail kegiatan, bobot poin, dan kuota repetisi.
- Log Mahasiswa & Log Staff: Sebagai tabel perantara untuk mencatat partisipasi pengguna dalam kegiatan.

## Cara Menjalankan
- Pastikan MySQL Server sudah aktif di perangkat Anda.
- Install library yang dibutuhkan:
`pip install pymysql matplotlib tabulate`
- Sesuaikan konfigurasi koneksi database pada fungsi
`connect_mysql di dalam file .py`
- Jalankan aplikasi:
`python IBDA02_Billy_Brian_Joey_SPK.py`
