-- =====================================================================
--  Skrip Persiapan Praktikum Pertemuan 6: Trigger & Window Functions
--  Jalankan di MySQL 8.0+  (mysql -u root -p < toko_db_setup.sql)
-- =====================================================================
DROP DATABASE IF EXISTS toko_db;
CREATE DATABASE toko_db;
USE toko_db;

CREATE TABLE produk (
  id_produk INT AUTO_INCREMENT PRIMARY KEY,
  nama      VARCHAR(50)   NOT NULL,
  kategori  VARCHAR(30),
  harga     DECIMAL(12,2) NOT NULL,
  stok      INT           NOT NULL DEFAULT 0
);

CREATE TABLE penjualan (
  id_jual   INT AUTO_INCREMENT PRIMARY KEY,
  id_produk INT  NOT NULL,
  jumlah    INT  NOT NULL,
  tanggal   DATE NOT NULL,
  FOREIGN KEY (id_produk) REFERENCES produk(id_produk)
);

CREATE TABLE log_harga (
  id_log      INT AUTO_INCREMENT PRIMARY KEY,
  id_produk   INT,
  harga_lama  DECIMAL(12,2),
  harga_baru  DECIMAL(12,2),
  diubah_oleh VARCHAR(100),
  waktu       DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE log_stok (
  id_log    INT AUTO_INCREMENT PRIMARY KEY,
  id_produk INT,
  stok_lama INT,
  stok_baru INT,
  selisih   INT,
  waktu     DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE produk_arsip (
  id_produk   INT,
  nama        VARCHAR(50),
  harga       DECIMAL(12,2),
  waktu_hapus DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE nilai_mhs (
  nim   CHAR(5) PRIMARY KEY,
  nama  VARCHAR(30),
  kelas CHAR(1),
  nilai INT
);

INSERT INTO produk (nama, kategori, harga, stok) VALUES
  ('Laptop A',    'Elektronik', 8500000, 10),
  ('Mouse B',     'Elektronik',  150000, 50),
  ('Keyboard C',  'Elektronik',  350000, 30),
  ('Buku SQL',    'Buku',        120000, 40),
  ('Buku Python', 'Buku',        135000, 25),
  ('Pulpen',      'ATK',          5000, 200),
  ('Map Plastik', 'ATK',          3000, 150);

  INSERT INTO nilai_mhs VALUES
  ('M01','Andi','A',90), ('M02','Budi','A',85),  ('M03','Citra','A',85), ('M04','Dewi','A',78),
  ('M05','Eko','B',92),  ('M06','Fitri','B',88), ('M07','Gilang','B',88),('M08','Hana','B',70);

-- Catatan: data penjualan diisi SETELAH trigger pengurang stok dibuat
-- (lihat slide contoh trigger), agar stok ikut berkurang otomatis:
-- INSERT INTO penjualan (id_produk, jumlah, tanggal) VALUES
--  (1,2,'2026-09-01'),(2,10,'2026-09-01'),(4,5,'2026-09-02'),(6,50,'2026-09-02'),
--  (3,4,'2026-09-03'),(5,7,'2026-09-03'),(2,5,'2026-09-04'),(7,30,'2026-09-04'),(4,8,'2026-09-05');
