# Travel Agent

Website statis sederhana untuk memperkenalkan ide destinasi wisata dan membantu pengunjung menyampaikan rencana perjalanan.

## Halaman

- **Home (`index.html`)** menampilkan pengantar layanan, daftar destinasi, dan gambar dengan judul serta deskripsi.
- **About (`about.html`)** menjelaskan pendekatan Travel Agent dalam membantu pengunjung menemukan dan merencanakan perjalanan.
- **Contact (`contact.html`)** berisi formulir pertanyaan perjalanan.

Semua halaman menggunakan navigasi yang sama dan menyesuaikan tata letak untuk layar ponsel maupun desktop.

## Teknologi

- HTML5 untuk struktur dan konten halaman.
- CSS3 untuk tampilan, grid, warna, tipografi, dan layout responsif.
- JavaScript untuk event form, validasi tanggal perjalanan, dan pesan status.

Tidak diperlukan framework, package manager, atau proses build.

## Struktur Berkas

```text
uts1/
├── index.html    # Beranda dan daftar destinasi
├── about.html    # Informasi tentang Travel Agent
├── contact.html  # Formulir pertanyaan perjalanan
├── style.css     # Gaya dan layout responsif untuk semua halaman
├── script.js     # Validasi dan interaksi formulir
└── README.md     # Dokumentasi proyek
```

## Menjalankan Secara Lokal

1. Buka folder `uts1` di VS Code.
2. Buka `index.html` langsung di browser, atau gunakan ekstensi Live Server.
3. Gunakan navigasi di bagian atas halaman untuk membuka About dan Contact.

Font Google Fonts dan gambar Unsplash dimuat dari internet. Jika tidak tersedia, font fallback CSS akan digunakan dan gambar eksternal mungkin tidak tampil.

## Validasi dan Interaksi Form

Form Contact menggunakan validasi bawaan HTML untuk nama, format email, dan pesan. JavaScript mengatur tanggal kembali agar tidak lebih awal daripada tanggal keberangkatan. Setelah data valid, halaman menampilkan konfirmasi bahwa formulir demo telah diperiksa.

**Formulir belum mengirim atau menyimpan pesan.** Untuk menerima pertanyaan sungguhan, hubungkan form ke backend atau layanan pengiriman formulir.

## Publikasi dengan GitHub Pages

Jika repositori GitHub berisi folder `uts1` di root repositori:

1. Push berkas proyek ke branch `master`.
2. Buka **Settings → Pages** di repositori.
3. Pada **Build and deployment**, pilih **Deploy from a branch**, branch `master`, dan folder `/(root)`.
4. Setelah deployment selesai, halaman proyek tersedia di:

   `https://github.com/charisphilipwibowo-ui/Travel-Agent/tree/master`
