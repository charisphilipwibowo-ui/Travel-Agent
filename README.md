# Travel Agent

Website statis untuk memperkenalkan destinasi wisata dan membantu pengunjung menyampaikan rencana perjalanan.

## Halaman

- [Home](index.html): pengantar layanan, daftar destinasi, serta gambar dengan judul dan deskripsi.
- [About](uts1/about.html): pendekatan Travel Agent dalam membantu pengunjung menemukan dan merencanakan perjalanan.
- [Contact](uts1/contact.html): formulir pertanyaan tentang perjalanan.

Semua halaman berbagi navigasi dan tata letak responsif untuk desktop maupun ponsel.

## Teknologi

- **HTML5** untuk struktur dan konten semantik.
- **CSS3** untuk tata letak grid, warna, tipografi, dan responsivitas.
- **JavaScript** untuk event form, validasi tanggal, dan pesan status.

Tidak diperlukan framework, package manager, atau proses build. Google Fonts dan gambar Unsplash dimuat dari internet.

## Struktur Repositori

```text
.
├── index.html      # Beranda Home yang ditampilkan pada alamat utama
├── README.md       # Dokumentasi repositori
└── uts1/
    ├── about.html   # Halaman About
    ├── contact.html # Halaman Contact dan formulir
    ├── style.css    # Gaya bersama dan layout responsif
    └── script.js    # Validasi dan interaksi formulir
```

## Menjalankan Secara Lokal

Buka `index.html` di browser. Halaman About dan Contact dapat dibuka melalui menu navigasi.

## Formulir Contact

Form menggunakan validasi bawaan HTML untuk nama, email, dan pesan. JavaScript memastikan tanggal kembali tidak lebih awal daripada tanggal keberangkatan, lalu menampilkan status setelah formulir valid.

**Formulir ini hanya demo dan tidak mengirim atau menyimpan pesan.** Untuk menerima pertanyaan sungguhan, hubungkan form ke backend atau layanan formulir.

## GitHub Pages

GitHub Pages dipublikasikan dari branch `main` dan folder `/(root)`. Beranda Home berada langsung di root repo; CSS dan JavaScript serta halaman About dan Contact tetap berada di folder `uts1`.

- [Buka website Travel Agent](https://charisphilipwibowo-ui.github.io/Travel-Agent/)
