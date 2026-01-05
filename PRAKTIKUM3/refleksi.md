# REFLEKSI PRAKTIKUM 3

## Algoritma Penggambaran Garis (Line Drawing Algorithms)

---

### 1. Tujuan Praktikum

Praktikum 3 bertujuan untuk memahami dan mengimplementasikan algoritma penggambaran garis, yaitu **DDA (Digital Differential Analyzer)** dan **Bresenham Line Algorithm** menggunakan Python dan matplotlib.

---

### 2. Konsep yang Dipelajari

#### A. Mengapa Perlu Algoritma Khusus?

Dalam grafika komputer, layar terdiri dari piksel-piksel diskrit. Untuk menggambar garis dari titik A ke titik B, kita perlu menentukan piksel mana saja yang harus dinyalakan. Algoritma DDA dan Bresenham membantu menentukan piksel-piksel tersebut secara efisien.

#### B. Algoritma DDA (Digital Differential Analyzer)

DDA adalah algoritma incremental yang menggunakan operasi floating-point untuk menghitung titik-titik garis.

**Langkah-langkah DDA:**

1. Hitung dx = x1 - x0 dan dy = y1 - y0
2. Tentukan steps = max(|dx|, |dy|)
3. Hitung increment: Xinc = dx/steps, Yinc = dy/steps
4. Mulai dari (x0, y0), tambahkan Xinc dan Yinc pada setiap iterasi
5. Bulatkan koordinat ke integer terdekat

#### C. Algoritma Bresenham

Bresenham adalah algoritma yang lebih efisien karena hanya menggunakan operasi integer (tanpa floating-point).

**Rumus Decision Parameter:**

```
p₀ = 2dy - dx

Jika p < 0:
    p_next = p + 2dy
    x = x + 1
Jika p ≥ 0:
    p_next = p + 2dy - 2dx
    x = x + 1, y = y + 1
```

---

### 3. Implementasi Program

#### Program 1 (p1.py) - DDA dengan Nilai Tetap

- Mengimplementasikan algoritma DDA untuk garis
- Titik awal (2, 3) dan titik akhir (10, 8) sudah ditentukan
- Menyimpan koordinat hasil dalam list
- Menampilkan garis dengan marker titik berwarna biru

#### Program 2 (p2.py) - DDA dengan Input Dinamis

- User memasukkan koordinat titik awal (x0, y0) dan titik akhir (x1, y1)
- Dilengkapi error handling untuk validasi input integer
- Judul grafik menampilkan koordinat yang diinput user
- Penjelasan kode dengan komentar yang detail

#### Program 3 (p3.py) - DDA dengan Input (Versi Lengkap)

- Sama seperti p2.py dengan implementasi DDA
- Kode yang lebih terstruktur dan terdokumentasi
- Input dinamis dengan validasi

#### PostTest1.py - Algoritma Bresenham

- Mengimplementasikan algoritma Bresenham untuk garis
- Menggunakan decision parameter (p) untuk menentukan piksel
- Output berupa list koordinat piksel yang dilalui garis
- Menggambar garis dari (3, 2) ke (10, 5)

#### Tugas (tugas.py) - Menggambar Rumah dengan DDA

- Menggunakan algoritma DDA untuk menggambar bentuk rumah
- Menggabungkan multiple garis untuk membentuk:
  - Badan rumah (persegi)
  - Atap rumah (segitiga)
  - Pintu rumah
  - Jendela rumah
- Demonstrasi praktis penggunaan algoritma DDA

---

### 4. Perbandingan Algoritma DDA dan Bresenham

| Aspek              | DDA            | Bresenham              |
| ------------------ | -------------- | ---------------------- |
| Operasi Aritmatika | Floating-point | Integer only           |
| Kecepatan          | Lebih lambat   | Lebih cepat            |
| Akurasi            | Baik           | Sangat baik            |
| Kompleksitas       | Sederhana      | Sedikit lebih kompleks |
| Pembulatan         | Perlu round()  | Tidak perlu            |
| Memory             | Lebih banyak   | Lebih sedikit          |

---

### 5. Langkah-langkah Algoritma

#### Algoritma DDA:

```python
def dda_algorithm(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    Xinc = dx / steps
    Yinc = dy / steps

    x, y = x0, y0
    for i in range(steps + 1):
        plot(round(x), round(y))
        x += Xinc
        y += Yinc
```

#### Algoritma Bresenham:

```python
def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    p = 2*dy - dx

    x, y = x0, y0
    for i in range(dx + 1):
        plot(x, y)
        if p < 0:
            p += 2*dy
        else:
            y += 1
            p += 2*dy - 2*dx
        x += 1
```

---

### 6. Aplikasi Praktis: Menggambar Rumah

Program tugas.py mendemonstrasikan penggunaan algoritma DDA untuk menggambar objek kompleks:

```
    /\
   /  \      <- Atap (2 garis miring)
  /----\
  |    |     <- Badan rumah (4 garis)
  | [] |     <- Jendela (4 garis)
  |____|     <- Pintu (3 garis)
```

---

### 7. Kesulitan yang Dihadapi

1. Memahami konsep incremental dalam algoritma DDA
2. Memahami decision parameter dalam algoritma Bresenham
3. Menangani kasus garis dengan kemiringan berbeda (steep vs gentle)
4. Menggabungkan multiple garis untuk membentuk objek kompleks

---

### 8. Solusi dan Pembelajaran

1. **Incremental DDA**: Setiap iterasi menambahkan nilai tetap ke x dan y
2. **Decision Parameter**: Bresenham menggunakan integer untuk memutuskan apakah y bertambah
3. **Kemiringan Garis**: Gunakan steps = max(|dx|, |dy|) untuk semua jenis kemiringan
4. **Objek Kompleks**: Pecah menjadi garis-garis individual, gambar satu per satu

---

### 9. Kelebihan Masing-masing Algoritma

#### Kelebihan DDA:

- Mudah dipahami dan diimplementasikan
- Cocok untuk pembelajaran konsep dasar
- Dapat menangani semua jenis kemiringan dengan mudah

#### Kelebihan Bresenham:

- Sangat efisien (hanya operasi integer)
- Tidak ada error pembulatan
- Standar industri untuk rasterisasi garis

---

### 10. Kesimpulan

Algoritma DDA dan Bresenham adalah fondasi penting dalam grafika komputer untuk menggambar garis. DDA lebih mudah dipahami namun menggunakan floating-point, sementara Bresenham lebih efisien dengan operasi integer. Keduanya memanfaatkan pendekatan incremental untuk menentukan piksel yang membentuk garis. Praktikum ini memberikan pemahaman praktis tentang rasterisasi garis dan penerapannya untuk menggambar objek kompleks seperti rumah.

---

### 11. Referensi

- Computer Graphics: Principles and Practice (Foley, van Dam)
- Bresenham's Line Algorithm (Jack Bresenham, 1962)
- Matplotlib documentation untuk visualisasi
