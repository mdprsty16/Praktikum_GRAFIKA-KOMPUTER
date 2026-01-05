# REFLEKSI PRAKTIKUM 8

## Transformasi Pencerminan (Reflection) pada Objek 2D

---

### 1. Tujuan Praktikum

Praktikum 8 bertujuan untuk memahami dan mengimplementasikan transformasi **Pencerminan (Reflection)** pada berbagai objek 2D menggunakan Python dan matplotlib.

---

### 2. Konsep yang Dipelajari

#### A. Apa itu Pencerminan (Reflection)?

Pencerminan adalah transformasi geometri yang menghasilkan bayangan cermin dari suatu objek terhadap suatu garis atau titik. Objek hasil pencerminan memiliki bentuk dan ukuran yang sama dengan objek asli, tetapi posisinya terbalik.

#### B. Jenis-jenis Pencerminan 2D

**1. Pencerminan terhadap Sumbu X**

```
x' = x
y' = -y
```

Matriks transformasi:

```
| 1   0 |
| 0  -1 |
```

**2. Pencerminan terhadap Sumbu Y**

```
x' = -x
y' = y
```

Matriks transformasi:

```
| -1  0 |
|  0  1 |
```

**3. Pencerminan terhadap Titik Origin (0,0)**

```
x' = -x
y' = -y
```

Matriks transformasi:

```
| -1   0 |
|  0  -1 |
```

---

### 3. Implementasi Program

#### Program 1 (p1.py) - Pencerminan Segitiga

- User memasukkan 3 koordinat titik segitiga
- Memilih sumbu pencerminan (x, y, atau origin)
- Menampilkan segitiga asli dan hasil pencerminan dengan fill warna

#### Program 2 (p2.py) - Pencerminan Persegi Panjang

- User memasukkan koordinat sudut kiri bawah, lebar, dan tinggi
- Memilih sumbu pencerminan
- Menggunakan `plt.Rectangle` untuk menggambar objek
- Visualisasi persegi panjang asli (biru) dan hasil pencerminan (merah)

#### Program 3 (p3.py) - Pencerminan Lingkaran

- User memasukkan koordinat pusat dan radius lingkaran
- Memilih sumbu pencerminan
- Menggunakan `plt.Circle` untuk menggambar objek
- Visualisasi lingkaran asli dan hasil pencerminan

#### Tugas (tugas.py) - Pencerminan Belah Ketupat

- User memasukkan pusat dan panjang diagonal belah ketupat
- Pencerminan dilakukan terhadap sumbu X
- Menampilkan belah ketupat asli dan hasil pencerminan

---

### 4. Perbandingan Hasil Pencerminan

| Sumbu   | Efek pada Koordinat   | Visualisasi                    |
| ------- | --------------------- | ------------------------------ |
| Sumbu X | Y berubah tanda       | Objek terbalik atas-bawah      |
| Sumbu Y | X berubah tanda       | Objek terbalik kiri-kanan      |
| Origin  | X dan Y berubah tanda | Objek terbalik diagonal (180°) |

---

### 5. Karakteristik Transformasi Pencerminan

1. **Isometri**: Jarak antar titik tetap sama (tidak berubah)
2. **Bentuk Tetap**: Bentuk objek tidak berubah
3. **Ukuran Tetap**: Luas dan keliling objek sama
4. **Orientasi Berubah**: Arah/orientasi objek terbalik
5. **Involusi**: Pencerminan 2x kembali ke posisi awal

---

### 6. Kesulitan yang Dihadapi

1. Memahami perbedaan pencerminan terhadap sumbu X, Y, dan origin
2. Menghitung koordinat baru untuk objek kompleks seperti persegi panjang
3. Memastikan visualisasi objek asli dan hasil pencerminan terlihat jelas

---

### 7. Solusi dan Pembelajaran

1. **Rumus Sederhana**:
   - Sumbu X: negasikan nilai Y
   - Sumbu Y: negasikan nilai X
   - Origin: negasikan keduanya
2. **Persegi Panjang**: Perlu memperhatikan titik referensi (sudut kiri bawah) dan menyesuaikan dengan lebar/tinggi
3. **Visualisasi**: Menggunakan warna berbeda (biru untuk asli, merah untuk hasil) dan grid untuk memperjelas posisi

---

### 8. Kesimpulan

Praktikum ini memberikan pemahaman tentang:

- Konsep pencerminan dalam grafika komputer 2D
- Tiga jenis pencerminan: terhadap sumbu X, sumbu Y, dan origin
- Implementasi pencerminan pada berbagai bentuk geometri
- Penggunaan matplotlib untuk visualisasi transformasi

Transformasi pencerminan banyak digunakan dalam:

- Desain simetris (logo, ornamen)
- Efek cermin dalam game dan animasi
- Pemrosesan citra (image processing)
- Computer-aided design (CAD)

---

### 9. Library yang Digunakan

- `matplotlib.pyplot`: Untuk visualisasi grafik 2D
- `plt.Rectangle`: Untuk membuat objek persegi panjang
- `plt.Circle`: Untuk membuat objek lingkaran

---

### 10. Contoh Kode Pencerminan

```python
def pencerminan(titik, sumbu):
    if sumbu == 'x':
        return [(x, -y) for (x, y) in titik]
    elif sumbu == 'y':
        return [(-x, y) for (x, y) in titik]
    elif sumbu == 'origin':
        return [(-x, -y) for (x, y) in titik]
```

---

_Praktikum 8 - Grafika Komputer_
_Semester 5_
