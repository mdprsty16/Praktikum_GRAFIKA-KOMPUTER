# REFLEKSI PRAKTIKUM 9

## Transformasi Shearing (Geser) pada Objek 2D

---

### 1. Tujuan Praktikum

Praktikum 9 bertujuan untuk memahami dan mengimplementasikan transformasi **Shearing (Geser)** pada berbagai objek 2D menggunakan Python dan matplotlib.

---

### 2. Konsep yang Dipelajari

#### A. Apa itu Shearing?

Shearing adalah transformasi geometri yang menggeser/memiringkan objek ke satu arah tertentu. Transformasi ini membuat objek tampak "miring" atau "condong" tanpa mengubah luasnya.

#### B. Matriks Shearing 2D

```
| 1     shear_x |
| shear_y    1  |
```

Di mana:

- `shear_x` = faktor geser horizontal (menggeser titik sepanjang sumbu X berdasarkan nilai Y)
- `shear_y` = faktor geser vertikal (menggeser titik sepanjang sumbu Y berdasarkan nilai X)

#### C. Rumus Transformasi

Untuk titik (x, y) yang ditransformasi menjadi (x', y'):

```
x' = x + shear_x * y
y' = shear_y * x + y
```

---

### 3. Implementasi Program

#### Program 1 (p1.py) - Shearing Belah Ketupat

- Membuat objek belah ketupat dengan 4 titik sudut
- Mengimplementasikan transformasi shear menggunakan matriks
- User memasukkan nilai shear_x dan shear_y
- Menampilkan perbandingan belah ketupat asli dan setelah shear

#### Program 2 (p2.py) - Shearing Segitiga

- Membuat objek segitiga dengan 3 titik sudut
- Menerapkan transformasi shear pada segitiga
- Visualisasi side-by-side antara segitiga asli dan hasil shear

#### Program 3 (p3.py) - Shearing Lingkaran

- Membuat objek lingkaran menggunakan persamaan parametrik
- Menerapkan transformasi shear pada lingkaran
- Lingkaran berubah menjadi bentuk elips setelah di-shear
- Menggunakan 100 titik untuk membuat lingkaran smooth

#### Tugas (tugas.py) - Shearing Persegi Panjang

- Membuat objek persegi panjang dengan ukuran 8x4
- Menerapkan shear dengan nilai tetap (shear_x=0.8, shear_y=0.3)
- Visualisasi transformasi dari persegi panjang menjadi jajar genjang

---

### 4. Perbandingan Hasil Shearing pada Berbagai Objek

| Objek           | Hasil Shearing                       |
| --------------- | ------------------------------------ |
| Belah Ketupat   | Menjadi jajar genjang miring         |
| Segitiga        | Segitiga miring dengan sudut berubah |
| Lingkaran       | Menjadi bentuk elips                 |
| Persegi Panjang | Menjadi jajar genjang                |

---

### 5. Karakteristik Transformasi Shearing

1. **Tidak Mengubah Luas**: Area objek tetap sama setelah transformasi
2. **Mengubah Sudut**: Sudut-sudut objek berubah
3. **Garis Tetap Lurus**: Garis lurus tetap menjadi garis lurus
4. **Tidak Isotropik**: Berbeda dengan rotasi/skala, shearing hanya bekerja pada satu arah

---

### 6. Kesulitan yang Dihadapi

1. Memahami perbedaan antara shear horizontal dan shear vertikal
2. Menentukan nilai shear yang tepat agar hasil visualisasi terlihat jelas
3. Memahami bagaimana matriks shearing bekerja pada koordinat titik

---

### 7. Solusi dan Pembelajaran

1. **Shear Horizontal vs Vertikal**:
   - Shear_x: menggeser titik ke kanan/kiri berdasarkan posisi Y
   - Shear_y: menggeser titik ke atas/bawah berdasarkan posisi X
2. **Nilai Shear**: Nilai antara 0.3-1.0 biasanya memberikan visualisasi yang baik
3. **Implementasi Matriks**: Menggunakan `np.dot()` untuk perkalian matriks dengan koordinat titik

---

### 8. Kesimpulan

Praktikum ini memberikan pemahaman tentang:

- Konsep transformasi shearing dalam grafika komputer 2D
- Penggunaan matriks transformasi 2x2 untuk operasi shearing
- Efek shearing pada berbagai bentuk geometri (belah ketupat, segitiga, lingkaran, persegi panjang)
- Implementasi visualisasi transformasi menggunakan matplotlib

Transformasi shearing banyak digunakan dalam:

- Membuat efek bayangan (shadow)
- Animasi karakter
- Desain grafis dan tipografi
- Simulasi perspektif sederhana

---

### 9. Library yang Digunakan

- `numpy`: Untuk operasi matriks dan array
- `matplotlib.pyplot`: Untuk visualisasi grafik 2D

---

### 10. Contoh Kode Matriks Shearing

```python
def shear(points, shear_x, shear_y):
    shear_matrix = np.array([
        [1, shear_x],
        [shear_y, 1]
    ])
    return np.dot(points, shear_matrix.T)
```

---

_Praktikum 9 - Grafika Komputer_
_Semester 5_
