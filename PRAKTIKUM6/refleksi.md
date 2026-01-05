# REFLEKSI PRAKTIKUM 6

## Transformasi Scaling (Penskalaan) pada Objek 2D dan 3D

---

### 1. Tujuan Praktikum

Praktikum 6 bertujuan untuk memahami dan mengimplementasikan transformasi **Scaling (Penskalaan)** pada berbagai objek 2D dan 3D menggunakan Python, NumPy, dan matplotlib.

---

### 2. Konsep yang Dipelajari

#### A. Apa itu Scaling?

Scaling adalah transformasi geometri yang mengubah ukuran objek dengan mengalikan setiap koordinat dengan faktor skala tertentu. Objek dapat diperbesar (scale > 1) atau diperkecil (scale < 1).

#### B. Matriks Scaling 2D

```
| Sx  0  |
| 0   Sy |
```

Di mana:

- `Sx` = faktor skala pada sumbu X
- `Sy` = faktor skala pada sumbu Y
- Jika Sx = Sy, scaling bersifat **uniform** (proporsional)
- Jika Sx ≠ Sy, scaling bersifat **non-uniform** (tidak proporsional)

#### C. Rumus Transformasi

Untuk titik (x, y) yang di-scale menjadi (x', y'):

```
x' = x * Sx
y' = y * Sy
```

Untuk scaling uniform dengan faktor s:

```
x' = x * s
y' = y * s
```

---

### 3. Implementasi Program

#### Program 1 (p1.py) - Scaling Segitiga

- Membuat objek segitiga dengan 3 titik sudut yang diinput user
- User memasukkan faktor skala untuk penskalaan
- Mengalikan setiap koordinat titik dengan faktor skala
- Menampilkan segitiga asli dan hasil penskalaan

#### Program 2 (p2.py) - Scaling Persegi

- Membuat objek persegi dengan 4 titik sudut
- User memasukkan koordinat 4 titik dan faktor skala
- Menerapkan transformasi scaling pada setiap titik
- Visualisasi persegi sebelum dan sesudah penskalaan
- Kode dilengkapi dengan komentar penjelasan yang detail

#### Program 3 (p3.py) - Scaling Lingkaran

- Membuat objek lingkaran menggunakan persamaan parametrik
- User memasukkan pusat, radius, dan faktor skala
- Scaling pada lingkaran dilakukan dengan mengalikan radius
- Pusat lingkaran tetap, hanya radius yang berubah

#### Program 4 (p4.py) - Scaling Lingkaran dan Persegi Panjang

- Menggabungkan scaling dua objek berbeda dalam satu program
- Lingkaran dan persegi panjang ditampilkan dalam subplot
- Masing-masing objek memiliki faktor skala tersendiri
- Visualisasi side-by-side untuk perbandingan

#### Tugas (tugas.py) - Scaling Tabung 3D

- Membuat objek tabung 3D menggunakan koordinat silinder
- Menggunakan `mpl_toolkits.mplot3d` untuk visualisasi 3D
- Scaling 3D: mengalikan koordinat x, y, z dengan faktor skala
- Menampilkan tabung asli dan hasil penskalaan dalam subplot vertikal

---

### 4. Perbandingan Hasil Scaling pada Berbagai Objek

| Objek           | Scale > 1           | Scale < 1            | Scale = 1 |
| --------------- | ------------------- | -------------------- | --------- |
| Segitiga        | Membesar            | Mengecil             | Tetap     |
| Persegi         | Membesar            | Mengecil             | Tetap     |
| Lingkaran       | Radius bertambah    | Radius berkurang     | Tetap     |
| Persegi Panjang | Lebar & tinggi naik | Lebar & tinggi turun | Tetap     |
| Tabung 3D       | Membesar semua arah | Mengecil semua arah  | Tetap     |

---

### 5. Karakteristik Transformasi Scaling

1. **Mengubah Ukuran**: Scaling mengubah dimensi objek sesuai faktor skala
2. **Titik Pusat**: Scaling dilakukan relatif terhadap origin (0, 0)
3. **Proporsionalitas**: Uniform scaling menjaga proporsi objek
4. **Mengubah Luas/Volume**: Luas berubah sebesar faktor² (2D), volume berubah sebesar faktor³ (3D)
5. **Reversible**: Scaling dapat dibalik dengan faktor 1/s

---

### 6. Perbedaan Scaling 2D dan 3D

#### Scaling 2D:

```python
x' = x * scale_factor
y' = y * scale_factor
```

#### Scaling 3D:

```python
x' = x * scale_factor
y' = y * scale_factor
z' = z * scale_factor
```

---

### 7. Kesulitan yang Dihadapi

1. Memahami perbedaan scaling uniform dan non-uniform
2. Menentukan titik referensi scaling (origin vs titik lain)
3. Implementasi scaling 3D pada objek tabung
4. Mengatur visualisasi agar objek asli dan hasil scaling terlihat jelas

---

### 8. Solusi dan Pembelajaran

1. **Uniform vs Non-uniform**: Uniform scaling menggunakan faktor sama untuk semua sumbu
2. **Titik Referensi**: Untuk scaling terhadap titik selain origin, perlu translasi dulu
3. **Scaling 3D**: Menggunakan meshgrid dan persamaan parametrik untuk tabung
4. **Visualisasi**: Mengatur xlim/ylim yang cukup besar untuk menampilkan kedua objek

---

### 9. Aplikasi Scaling dalam Grafika Komputer

1. **Zoom In/Out**: Memperbesar atau memperkecil tampilan objek
2. **Resize Objek**: Mengubah ukuran sprite atau model dalam game
3. **Normalisasi**: Menyesuaikan ukuran objek ke rentang tertentu
4. **Animasi**: Efek pertumbuhan atau penyusutan objek

---

### 10. Kesimpulan

Transformasi scaling adalah operasi fundamental dalam grafika komputer yang memungkinkan perubahan ukuran objek. Praktikum ini memberikan pemahaman tentang cara kerja scaling pada berbagai bentuk geometri 2D (segitiga, persegi, lingkaran) dan 3D (tabung). Pemahaman tentang scaling sangat penting untuk manipulasi objek dalam aplikasi grafis dan game development.

---

### 11. Referensi

- NumPy documentation untuk operasi array dan meshgrid
- Matplotlib documentation untuk visualisasi 2D dan 3D
- Konsep transformasi geometri dalam grafika komputer
