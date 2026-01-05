# REFLEKSI PRAKTIKUM 4

## Algoritma Penggambaran Lingkaran (Circle Drawing Algorithms)

---

### 1. Tujuan Praktikum

Praktikum 4 bertujuan untuk memahami dan mengimplementasikan algoritma penggambaran lingkaran, yaitu **Midpoint Circle Algorithm** dan **Bresenham Circle Algorithm** menggunakan Python dan matplotlib.

---

### 2. Konsep yang Dipelajari

#### A. Mengapa Perlu Algoritma Khusus?

Menggambar lingkaran menggunakan persamaan kartesian (x² + y² = r²) atau trigonometri (x = r·cos θ, y = r·sin θ) memerlukan operasi floating-point yang mahal. Algoritma Midpoint dan Bresenham menggunakan aritmatika integer yang lebih efisien.

#### B. Simetri 8 Titik (8-Way Symmetry)

Lingkaran memiliki simetri pada 8 oktannya. Dengan menghitung satu titik (x, y), kita dapat langsung mendapatkan 7 titik lainnya:

```
(x, y)   (-x, y)   (x, -y)   (-x, -y)
(y, x)   (-y, x)   (y, -x)   (-y, -x)
```

#### C. Midpoint Circle Algorithm

**Rumus Decision Parameter:**

```
p₀ = 1 - r    (atau p₀ = 5/4 - r)

Jika p < 0:
    p_next = p + 2x + 1
Jika p ≥ 0:
    p_next = p + 2x - 2y + 1
    y = y - 1
```

#### D. Bresenham Circle Algorithm

**Rumus Decision Parameter:**

```
d₀ = 3 - 2r

Jika d ≤ 0:
    d_next = d + 4x + 6
Jika d > 0:
    d_next = d + 4(x - y) + 10
    y = y - 1
```

---

### 3. Implementasi Program

#### Program 1 (p1.py) - Midpoint Circle (Nilai Tetap)

- Mengimplementasikan algoritma Midpoint Circle
- Pusat lingkaran tetap di (0, 0) dengan radius 10
- Menggunakan decision parameter p = 1 - r
- Menampilkan titik-titik hasil perhitungan dengan warna biru

#### Program 2 (p2.py) - Midpoint Circle (Input Dinamis)

- User memasukkan koordinat pusat (x, y) dan radius
- Menambahkan titik awal (0, r) sebelum iterasi
- Batas sumbu otomatis menyesuaikan dengan pusat dan radius
- Judul menampilkan parameter lingkaran yang diinput

#### Program 3 (p3.py) - Bresenham Circle Algorithm

- Mengimplementasikan algoritma Bresenham untuk lingkaran
- User memasukkan pusat dan radius
- Decision parameter d = 3 - 2r
- Menampilkan titik-titik dengan warna merah

#### Tugas (tugas.py) - Midpoint Circle (Versi Buku)

- Implementasi Midpoint Circle sesuai rumus dari buku
- Decision parameter p = 5/4 - r
- Update parameter: p + 2x + 3 atau p + 2(x-y) + 5
- Pusat di origin dengan radius 10

---

### 4. Perbandingan Algoritma

| Aspek              | Midpoint Circle    | Bresenham Circle   |
| ------------------ | ------------------ | ------------------ |
| Decision Parameter | p = 1 - r          | d = 3 - 2r         |
| Kondisi Update     | p < 0 / p ≥ 0      | d ≤ 0 / d > 0      |
| Operasi            | Integer arithmetic | Integer arithmetic |
| Akurasi            | Sangat baik        | Sangat baik        |
| Kompleksitas       | O(r)               | O(r)               |

---

### 5. Langkah-langkah Algoritma

#### Midpoint Circle:

1. Inisialisasi: x = 0, y = r, p = 1 - r
2. Plot 8 titik simetris dari (x, y)
3. Increment x
4. Jika p < 0: p = p + 2x + 1
5. Jika p ≥ 0: y--, p = p + 2x - 2y + 1
6. Ulangi langkah 2-5 selama x ≤ y

#### Bresenham Circle:

1. Inisialisasi: x = 0, y = r, d = 3 - 2r
2. Plot 8 titik simetris dari (x, y)
3. Jika d ≤ 0: d = d + 4x + 6
4. Jika d > 0: y--, d = d + 4(x-y) + 10
5. Increment x
6. Ulangi langkah 2-5 selama y ≥ x

---

### 6. Fungsi Simetri 8 Titik

```python
def plot_8_points(h, k, x, y):
    points = [
        (h + x, k + y),  # Oktant 1
        (h - x, k + y),  # Oktant 2
        (h + x, k - y),  # Oktant 8
        (h - x, k - y),  # Oktant 7
        (h + y, k + x),  # Oktant 4
        (h - y, k + x),  # Oktant 3
        (h + y, k - x),  # Oktant 5
        (h - y, k - x),  # Oktant 6
    ]
    return points
```

---

### 7. Kesulitan yang Dihadapi

1. Memahami perbedaan rumus decision parameter antar versi algoritma
2. Memahami konsep simetri 8 titik dan penerapannya
3. Menentukan kondisi berhenti iterasi (x ≤ y atau x < y)
4. Memahami kapan harus decrement nilai y

---

### 8. Solusi dan Pembelajaran

1. **Variasi Rumus**: Ada beberapa versi rumus yang valid, perbedaan hanya pada konstanta
2. **Simetri 8 Titik**: Dengan menghitung 1/8 lingkaran, kita mendapat lingkaran penuh
3. **Kondisi Berhenti**: Iterasi berhenti saat x melewati y (oktant pertama selesai)
4. **Decrement y**: y berkurang saat decision parameter menunjukkan titik di luar lingkaran

---

### 9. Keunggulan Algoritma

1. **Efisiensi**: Hanya menggunakan operasi integer (penjumlahan, pengurangan)
2. **Tidak Ada Perkalian/Pembagian**: Operasi mahal dihindari
3. **Akurasi Tinggi**: Menghasilkan titik-titik yang sangat mendekati lingkaran ideal
4. **Memanfaatkan Simetri**: Hanya perlu menghitung 1/8 bagian lingkaran

---

### 10. Kesimpulan

Algoritma Midpoint Circle dan Bresenham Circle adalah metode efisien untuk menggambar lingkaran dalam grafika komputer. Kedua algoritma memanfaatkan simetri 8 titik dan aritmatika integer untuk menghasilkan lingkaran dengan cepat dan akurat. Pemahaman tentang algoritma ini penting sebagai dasar untuk memahami rasterisasi bentuk-bentuk geometri lainnya.

---

### 11. Referensi

- Computer Graphics: Principles and Practice (Foley, van Dam)
- Algoritma Midpoint Circle (Bresenham, 1977)
- Matplotlib documentation untuk visualisasi
