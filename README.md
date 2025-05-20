# TASKMATE-APLIKASI-PENGINGAT-TUGAS-KULIAH

## Disusun Oleh

 | Nama | NIM |
 |--------|------|
 | Salsabila Fitri Ramadhani | 2310511002 |
 | Najwa Khaylawati | 2310511008 |
 | Nurhaliza	| 2310511028 |

1. Pendahuluan
1.1 Tujuan
Dokumen ini disusun untuk menjabarkan kebutuhan perangkat lunak, baik dari sisi fungsional maupun non-fungsional, dari aplikasi TaskMate. Aplikasi ini dirancang sebagai pengingat tugas kuliah berbasis terminal (CLI) yang dibangun menggunakan bahasa pemrograman Python. Tujuan utamanya adalah membantu mahasiswa dalam mencatat, mengelola, serta menghapus daftar tugas perkuliahan dengan cara yang efisien dan mudah digunakan.
1.2 Lingkup
TaskMate menyediakan fitur utama untuk:
 Menambahkan tugas baru dengan detail seperti judul, nama mata kuliah, dan tenggat waktu (deadline)
 Menampilkan daftar tugas yang telah disimpan
Menghapus tugas yang sudah diselesaikan atau tidak lagi diperlukan
 Menyimpan serta memuat data secara otomatis dalam format file JSON
1.3 Definisi, Akronim, dan Singkatan
Istilah
Makna
CLI
Command Line Interface: antarmuka yang menggunakan baris perintah
SRS
Software Requirements Specification: dokumen kebutuhan perangkat lunak
User
Pengguna akhir dari aplikasi, yaitu mahasiswa
JSON
JavaScript Object Notation: format penyimpanan data berbasis teks


2. Deskripsi Umum
2.1 Perspektif Produk
TaskMate merupakan aplikasi mandiri (standalone) yang dapat dijalankan di terminal komputer yang sudah terinstal Python versi 3.x. Sistem ini tidak membutuhkan database eksternal karena seluruh data disimpan dalam file JSON secara lokal.
2.2 Fungsi Sistem
Fungsi utama TaskMate meliputi:
Menampilkan daftar tugas kuliah.
Menambahkan tugas baru dengan validasi terhadap input pengguna.
Menghapus tugas berdasarkan ID atau urutan nomor.
Menyimpan dan memuat data secara otomatis ke dan dari file JSON.
2.3 Karakteristik Pengguna
Pengguna aplikasi ini adalah mahasiswa yang membutuhkan alat bantu sederhana untuk mencatat dan mengelola tugas kuliah. Sistem dirancang agar mudah digunakan tanpa membutuhkan kemampuan teknis yang tinggi. Input dilakukan melalui menu numerik dan teks sederhana di terminal.
3. Kebutuhan Fungsional
Kode
Nma Fitur
Deskripsi
RF001
Tambah Tugas
Pengguna dapat menambahkan tugas baru dengan mengisi judul, mata kuliah, dan deadline.
RF002
Tampilkan Tugas
Sistem menampilkan seluruh tugas beserta informasinya.
RF003
Hapus Tugas
Pengguna dapat menghapus tugas berdasarkan ID atau nomor tugas.
RF004
Simpan Data
Data disimpan otomatis ke file JSON saat ada perubahan.
RF005
Muat Data
Data dimuat dari file JSON saat aplikasi dijalankan.
RF006
Validasi Input
Input divalidasi agar judul tidak kosong dan deadline sesuai format.


4. Kebutuhan Non-Fungsional
Kode
Deskripsi
RNF001
Sistem merespons input pengguna dalam waktu kurang dari 1 detik.
RNF002
Sistem dapat dijalankan dengan Python 3.x di Windows, Linux, dan macOS.
RNF003
Antarmuka CLI sederhana dan mudah dipahami.
RNF004
Data disimpan dalam file JSON yang dapat dibaca dan dimodifikasi dengan mudah.





5. Antarmuka Sistem
5.1 Antarmuka Pengguna
TaskMate memiliki antarmuka berbasis teks yang dijalankan di terminal. Menu navigasi menggunakan angka dan input dilakukan dalam bentuk teks sederhana.
5.2 Antarmuka Perangkat Keras
Aplikasi ini memerlukan komputer dengan Python 3.x terinstal. Tidak membutuhkan perangkat keras tambahan.
5.3 Antarmuka Perangkat Lunak
Dijalankan menggunakan Python 3.x dengan memanfaatkan modul standar seperti json dan datetime. Tidak menggunakan pustaka eksternal pihak ketiga.
6. Batasan Sistem
Sistem hanya dapat dijalankan melalui terminal (CLI), tanpa antarmuka grafis atau berbasis web.
Data disimpan secara lokal menggunakan file JSON, tanpa koneksi ke server database.
Tidak mendukung fitur login atau multi-user.
Tidak menyediakan notifikasi atau pengingat otomatis.



7. Lampiran
Struktur kode program:
main.py: berisi logika utama dan tampilan menu.


task_manager.py: menangani fungsi penambahan, penghapusan, dan penampilan tugas.
storage.py: bertanggung jawab atas penyimpanan dan pemuatan data dalam file JSON.


Lampiran tambahan:
Screenshot tampilan terminal (menu & daftar tugas).
Diagram alur proses kerja aplikasi.
