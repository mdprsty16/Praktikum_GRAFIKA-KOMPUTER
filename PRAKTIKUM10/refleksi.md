# REFLEKSI PRAKTIKUM 10

## Translasi dan Penskalaan pada Objek 3D

---

### 1. Tujuan Praktikum

Praktikum 10 bertujuan untuk memahami dan mengimplementasikan transformasi geometri 3D, khususnya:

- **Translasi 3D**: Memindahkan objek ke posisi baru tanpa mengubah ukuran atau bentuk
- **Penskalaan 3D**: Mengubah ukuran objek (memperbesar/memperkecil) dari titik pusat

---

### 2. Konsep yang Dipelajari

#### A. Translasi 3D

Translasi adalah operasi pemindahan objek dari satu posisi ke posisi lain. Pada ruang 3D, translasi melibatkan perpindahan pada tiga sumbu (x, y, z).

**Matriks Translasi 3D (4x4):**

```
| 1  0  0  tx |
| 0  1  0  ty |
| 0  0  1  tz |
| 0  0  0  1  |
```

Di mana:

- `tx` = perpindahan pada sumbu X
- `ty` = perpindahan pada sumbu Y
- `tz` = perpindahan pada sumbu Z

#### B. Penskalaan 3D

Penskalaan adalah operasi untuk mengubah ukuran objek dengan faktor skala tertentu pada setiap sumbu.

**Matriks Penskalaan 3D (4x4):**

```
| sx  0   0   0 |
| 0   sy  0   0 |
| 0   0   sz  0 |
| 0   0   0   1 |
```

Di mana:

- `sx` = faktor skala pada sumbu X
- `sy` = faktor skala pada sumbu Y
- `sz` = faktor skala pada sumbu Z

---

### 3. Implementasi Program

#### Program 1 (p1.py) - Translasi Kubus

- Membuat objek kubus 3D
- Mengimplementasikan fungsi translasi menggunakan operasi penjumlahan koordinat
- User dapat memasukkan nilai translasi untuk masing-masing sumbu
- Menampilkan visualisasi kubus asli (cyan) dan kubus hasil translasi (merah)

#### Program 2 (p2.py) - Penskalaan Limas

- Membuat objek limas/pyramid 3D
- Mengimplementasikan fungsi penskalaan menggunakan operasi perkalian koordinat
- User dapat memasukkan faktor skala untuk masing-masing sumbu
- Menampilkan visualisasi limas asli (biru) dan limas hasil penskalaan (merah)

#### Pretest & Posttest

- Menggunakan matriks transformasi 4x4 (homogeneous coordinates)
- Mendemonstrasikan kombinasi transformasi secara berurutan
- Menunjukkan bahwa **urutan transformasi mempengaruhi hasil akhir**

---

### 4. Perbedaan Translasi vs Penskalaan

| Aspek              | Translasi                | Penskalaan                   |
| ------------------ | ------------------------ | ---------------------------- |
| Tujuan             | Memindahkan posisi objek | Mengubah ukuran objek        |
| Bentuk Objek       | Tidak berubah            | Tidak berubah (proporsional) |
| Ukuran Objek       | Tidak berubah            | Berubah sesuai faktor skala  |
| Operasi Matematika | Penjumlahan              | Perkalian                    |
| Titik Referensi    | Tidak ada                | Titik pusat/origin           |

---

### 5. Kesulitan yang Dihadapi

1. Memahami konsep homogeneous coordinates (koordinat homogen) yang menggunakan matriks 4x4
2. Memvisualisasikan transformasi 3D pada layar 2D
3. Memahami pengaruh urutan transformasi ketika dikombinasikan

---

### 6. Solusi dan Pembelajaran

1. **Homogeneous Coordinates**: Menggunakan koordinat homogen memungkinkan semua transformasi (translasi, rotasi, penskalaan) dapat direpresentasikan dalam bentuk perkalian matriks
2. **Visualisasi**: Menggunakan library `matplotlib` dengan `mplot3d` untuk membuat visualisasi 3D yang interaktif
3. **Urutan Transformasi**: Memahami bahwa `M_total = M2 @ M1` berarti M1 diterapkan lebih dulu, kemudian M2

---

### 7. Kesimpulan

Praktikum ini memberikan pemahaman mendalam tentang:

- Cara kerja transformasi geometri 3D (translasi dan penskalaan)
- Penggunaan matriks transformasi untuk memanipulasi objek 3D
- Implementasi visualisasi 3D menggunakan Python dan matplotlib
- Pentingnya memahami urutan transformasi dalam komposisi matriks

Transformasi 3D merupakan dasar penting dalam grafika komputer yang digunakan dalam berbagai aplikasi seperti game development, animasi, CAD/CAM, dan virtual reality.

---

### 8. Library yang Digunakan

- `numpy`: Untuk operasi matriks dan array
- `matplotlib.pyplot`: Untuk visualisasi grafik
- `mpl_toolkits.mplot3d`: Untuk plotting 3D
- `Poly3DCollection`: Untuk membuat koleksi polygon 3D

---

_Praktikum 10 - Grafika Komputer_
_Semester 5_
