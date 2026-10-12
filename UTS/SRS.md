# Software Requirements Specification

## 1. Pendahuluan

### 1.1 Tujuan
Jelajah Lokal adalah situs informasi wisata yang memberi pengunjung inspirasi destinasi Indonesia dan cara sederhana untuk menemukan tempat berdasarkan kategori atau kata kunci.

### 1.2 Ruang lingkup
Situs ini merupakan frontend statis untuk tugas UTS Pemrograman Web. Cakupan meliputi halaman jelajah, tentang, kontak, pencarian, filter, favorit pada browser, dan validasi formulir. Situs tidak memiliki akun, basis data, layanan peta, transaksi, atau pengiriman pesan ke server.

### 1.3 Pengguna
Pengunjung umum yang mencari inspirasi wisata Indonesia dan ingin membaca atau membagikan rekomendasi destinasi.

## 2. Kebutuhan fungsional

- **F-01:** Pengunjung dapat berpindah antara halaman Jelajahi, Tentang, dan Kontak melalui navigasi.
- **F-02:** Halaman Jelajahi menampilkan nama, lokasi, kategori, deskripsi, gambar, dan tautan informasi untuk setiap destinasi.
- **F-03:** Pengunjung dapat memfilter destinasi menurut kategori: Alam, Pantai, Budaya, atau Petualangan.
- **F-04:** Pengunjung dapat mencari destinasi menggunakan nama atau lokasi; hasil pencarian mengikuti filter kategori yang aktif.
- **F-05:** Sistem memperbarui jumlah hasil dan menampilkan pesan ketika tidak ada destinasi yang cocok.
- **F-06:** Pengunjung dapat menekan tombol favorit untuk mengubah statusnya selama halaman sedang terbuka.
- **F-07:** Pengunjung dapat mengisi nama, email, topik, dan pesan pada halaman Kontak.
- **F-08:** Formulir menolak isian yang tidak memenuhi validasi HTML dan menampilkan pesan konfirmasi untuk isian yang valid. Pesan tidak dikirim ke server.

## 3. Kebutuhan nonfungsional

- **NF-01:** Halaman harus dapat digunakan pada layar desktop maupun ponsel tanpa gulir horizontal yang tidak diperlukan.
- **NF-02:** Markup memakai elemen HTML semantik, bahasa dokumen Bahasa Indonesia, label formulir, dan teks alternatif gambar.
- **NF-03:** Warna, ukuran teks, dan status tombol harus membantu keterbacaan dan navigasi dengan keyboard.
- **NF-04:** Gerakan dekoratif dikurangi ketika sistem pengguna mengaktifkan preferensi `prefers-reduced-motion`.
- **NF-05:** Situs dapat dipublikasikan sebagai situs statis di GitHub Pages tanpa backend.

## 4. Asumsi dan batasan

- Akses internet dibutuhkan untuk memuat gambar Unsplash dan font Google Fonts.
- Status favorit tidak disimpan setelah halaman dimuat ulang.
- Form kontak hanya simulasi interaksi frontend; integrasi email atau backend berada di luar ruang lingkup.
- Informasi destinasi dan tautan eksternal merupakan materi awal dan perlu diverifikasi sebelum publikasi.

## 5. Kriteria penerimaan

- Ketiga halaman dapat dibuka dan navigasinya bekerja.
- Filter dan pencarian menampilkan kartu yang sesuai serta jumlah hasil yang benar.
- Tombol favorit berubah saat ditekan.
- Formulir menolak isian wajib yang kosong atau email tidak valid, lalu menampilkan konfirmasi untuk isian valid.
- Tata letak tetap terbaca pada desktop dan ponsel.
