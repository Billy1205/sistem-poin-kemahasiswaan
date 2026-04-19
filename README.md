# Student Activity Point System (SPK) Application

The Student Activity Point System (Sistem Poin Kemahasiswaan/SPK) is a prototype management system designed to streamline the input, management, and summarization of student participation data. This application implements core CRUD (Create, Read, Update, Delete) operations integrated with a relational database.

<i>This project was developed collaboratively by a team of three IT & Big Data Analytics students to demonstrate database management system implementation using Python and MySQL.</i>

## 🚀 Key Features
- **Multi-user Authentication**: Role-based access control (RBAC) distinguishing between Students, Staff, and Administrators.
- **Administrative Management**: Comprehensive tools for adding, viewing, and editing activity statuses, as well as managing student and staff records.
- **User Dashboards**: Personalized interfaces for Students and Staff to view profiles and track available or completed events.
- **Real-time Analytics & Visualization**: Integrated pie charts to visualize attendance percentages and participation rates for administrative review.
- **Robust Input Validation**: Built-in checks for date/time formatting, decimal precision, and unique constraints (ID/Name) to ensure data integrity.

## 🛠️ Tech Stack & Implementation
- **ERD Design**: Architected entity relationships to support accurate point calculation and data consistency.
- **Database Engineering**: Implemented tables, constraints, and relationships using MySQL.
- **GUI Development**: Developed responsive login pages and interactive dashboards.
- **Backend Integration**: Seamlessly mapped UI actions (Save, Search, Delete) to optimized SQL queries.
- **Data Visualization**: Integrated graphical reporting modules for administrative insights.

## 🔗 Database Schema (ERD)
The system architecture relies on five primary tables:
- **Students**: Stores identity data and cumulative activity points.
- **Staff**: Manages staff identity records.
- **Events**: Contains activity details, point weightage, and repetition quotas.
- **Student & Staff Logs**: Transactional junction tables that track user participation in specific activities.

## ⚡ Installation & Setup
Follow these steps to deploy the application locally:

1. **Prerequisites**: Ensure you have **MySQL Server** installed and running.
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/Billy1205/sistem-poin-kemahasiswaan.git
   cd sistem-poin-kemahasiswaan
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configuration**:
   Open the Python file and locate the `connect_mysql` function. Update your credentials:
   ```python
   host="localhost",
   user="your_username",
   password="your_password"
   ```
5. **Run Application**:
   ```bash
   python IBDA02_Billy_Brian_Joey_SPK.py
   ```
   *Note: The system will automatically initialize the `spkDB` database and create all necessary tables on the first run.*
  
***

# Aplikasi Sistem Poin Kemahasiswaan (SPK)
Aplikasi Sistem Poin Kemahasiswaan (SPK) adalah sebuah prototipe sistem manajemen data poin mahasiswa yang dirancang untuk mempermudah proses input, pengelolaan, dan rekapitulasi data partisipasi kegiatan mahasiswa. Aplikasi ini mengimplementasikan konsep CRUD (Create, Read, Update, Delete) yang terintegrasi langsung dengan database relasional.

<i>Proyek ini dikembangkan secara kolaboratif oleh tim yang terdiri dari 3 orang mahasiswa IT & Big Data Analytics untuk mengimplementasikan sistem manajemen database menggunakan Python dan MySQL.</i>

## 🚀 Fitur Utama
- **Sistem Login Multi-user**: Membedakan hak akses antara Mahasiswa, Staff, dan Admin.
- **Manajemen Data (Admin)**: Kemampuan untuk menambah, melihat, mengedit status kegiatan, serta menghapus data mahasiswa atau staff.
- **Dashboard Mahasiswa/Staff**: Menampilkan profil pengguna dan daftar kegiatan (events) yang tersedia atau telah diikuti.
- **Visualisasi Rekapitulasi**: Menampilkan persentase kehadiran mahasiswa dan staff dalam suatu kegiatan menggunakan grafik lingkaran (pie chart) secara real-time.
- **Validasi Input**: Dilengkapi dengan pengecekan format tanggal, jam, nilai desimal, dan verifikasi data unik (ID/Nama) untuk menjaga integritas data.

## 🛠️ Teknologi yang Digunakan
- **ERD Design**: Merancang hubungan antar entitas untuk mendukung sistem poin yang akurat.
- **Database Implementation**: Membangun tabel dan relasi menggunakan SQL.
- **GUI Development**: Membuat halaman login dan dashboard yang responsif.
- **Feature Integration**: Menghubungkan tombol simpan, cari, dan hapus dengan query database.
- **Visualization**: Menambahkan fitur rekapitulasi berbasis grafik untuk admin.

## 🔗 Struktur Database (ERD)
Proyek ini menggunakan 5 tabel utama:
- **Mahasiswa**: Menyimpan data identitas dan total poin.
- **Staff**: Menyimpan data identitas staff.
- **Events**: Menyimpan detail kegiatan, bobot poin, dan kuota repetisi.
- **Log Mahasiswa & Log Staff**: Sebagai tabel perantara untuk mencatat partisipasi pengguna dalam kegiatan.

## ⚡ Instalasi & Persiapan
Ikuti langkah-langkah berikut untuk menjalankan aplikasi secara lokal:

1. **Prasyarat**: Pastikan Anda sudah menginstal dan menjalankan **MySQL Server**.
2. **Klon Repositori**:
   ```bash
   git clone https://github.com/Billy1205/sistem-poin-kemahasiswaan.git
   cd sistem-poin-kemahasiswaan
   ```
3. **Instal Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Konfigurasi**:
   Buka file Python dan cari fungsi `connect_mysql`. Perbarui kredensial MySQL Anda:
   ```python
   host="localhost",
   user="username_anda",
   password="password_anda"
   ```
5. **Jalankan Aplikasi**:
   ```bash
   python IBDA02_Billy_Brian_Joey_SPK.py
   ```
   *Catatan: Sistem akan secara otomatis menginisialisasi database `spkDB` dan membuat semua tabel yang diperlukan saat pertama kali dijalankan.*
