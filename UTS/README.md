# Jelajah Lokal

Direktori wisata Indonesia yang membantu pengunjung menemukan inspirasi destinasi berdasarkan nama, lokasi, dan kategori. Dibuat sebagai proyek UTS Pemrograman Web menggunakan HTML, CSS, dan JavaScript.

## Halaman dan fitur

- `index.html`: halaman jelajah dengan enam rekomendasi destinasi, pencarian, filter kategori, dan tombol favorit.
- `about.html`: tujuan dan prinsip Jelajah Lokal.
- `contact.html`: formulir rekomendasi dengan validasi bawaan HTML dan pesan konfirmasi JavaScript.
- `style.css`: sistem warna, tipografi, tata letak responsif, dan animasi.
- `script.js`: logika filter dan pencarian kartu, tombol favorit sederhana, serta pesan konfirmasi formulir.

Pencarian dan filter dapat digunakan bersamaan. Status tombol favorit hanya berlaku selama halaman terbuka. Formulir kontak memakai validasi bawaan browser dan hanya menampilkan konfirmasi di halaman; data belum dikirim atau disimpan ke server.

## Menjalankan

Buka `index.html` di browser. Koneksi internet diperlukan untuk memuat font dan foto dari Google Fonts dan Unsplash.

## Publikasi di GitHub Pages

1. Unggah isi folder `UTS` ke repositori GitHub.
2. Buka **Settings > Pages** pada repositori.
3. Pada **Build and deployment**, pilih **Deploy from a branch**, pilih branch `main` dan folder `/ (root)`, lalu simpan.
4. Setelah publikasi selesai, buka alamat yang ditampilkan di bagian GitHub Pages. Pastikan halaman utama bernama `index.html`.

## Struktur HTML

Setiap halaman menggunakan `header`, `nav`, `main`, `section`, dan `footer` untuk membagi struktur konten secara semantik. Elemen `article` mewakili satu destinasi; judul bertingkat membantu pembaca dan teknologi bantu memahami susunan halaman. Gambar memiliki teks alternatif, kontrol formulir memiliki label, dan bahasa halaman ditetapkan ke Bahasa Indonesia melalui `lang="id"`.

## Desain CSS

CSS menggunakan custom properties untuk warna dan tipografi agar tampilan konsisten. Grid menata kartu destinasi, sedangkan media queries mengubah navigasi, kolom kartu, dan halaman kontak untuk layar yang lebih kecil. Animasi singkat memberi penekanan pada hero dan kartu; preferensi `prefers-reduced-motion` mengurangi animasi bagi pengguna yang memintanya.

## JavaScript

Event `input` pada kolom pencarian dan event `click` pada tombol kategori memperbarui kartu yang terlihat serta jumlah hasil. Tombol hati mengubah ikon saat diklik. Formulir memanfaatkan atribut HTML seperti `required`, `type="email"`, dan `minlength`, kemudian JavaScript menampilkan pesan setelah isian valid.

## Sumber visual dan informasi

Foto dimuat dari Unsplash. Tautan pada kartu mengarah ke halaman informasi destinasi dari Indonesia Travel atau pengelola Borobudur. Pastikan untuk memeriksa kembali kredit dan ketentuan penggunaan aset sebelum publikasi akhir.
