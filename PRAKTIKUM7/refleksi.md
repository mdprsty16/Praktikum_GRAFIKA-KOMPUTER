# REFLEKSI PRAKTIKUM 7

## Transformasi Rotasi pada Objek 2D

---

### 1. Tujuan Praktikum

Praktikum 7 bertujuan untuk memahami dan mengimplementasikan transformasi **Rotasi** pada berbagai objek 2D menggunakan Python, NumPy, dan matplotlib.

---

### 2. Konsep yang Dipelajari

#### A. Apa itu Rotasi?

Rotasi adalah transformasi geometri yang memutar objek di sekitar titik pusat (origin) dengan sudut tertentu. Transformasi ini mempertahankan bentuk dan ukuran objek, hanya mengubah orientasinya.

#### B. Matriks Rotasi 2D

```
| cos(θ)  -sin(θ) |
| sin(θ)   cos(θ) |
```

Di mana:

- `θ` = sudut rotasi dalam radian
- Rotasi positif = berlawanan arah jarum jam (counter-clockwise)
- Rotasi negatif = searah jarum jam (clockwise)

#### C. Rumus Transformasi

Untuk titik (x, y) yang dirotasi sebesar sudut θ menjadi (x', y'):

```
x' = x * cos(θ) - y * sin(θ)
y' = x * sin(θ) + y * cos(θ)
```

---

### 3. Implementasi Program

#### Program 1 (p1.py) - Rotasi Segitiga

- Membuat objek segitiga dengan 3 titik sudut yang diinput user
- Mengimplementasikan transformasi rotasi menggunakan matriks rotasi
- User memasukkan koordinat segitiga dan sudut rotasi dalam derajat
- Menampilkan perbandingan segitiga sebelum dan sesudah rotasi

#### Program 2 (p2.py) - Rotasi Persegi Panjang

- Membuat objek persegi panjang dengan 4 titik sudut
- User memasukkan koordinat 4 titik dan sudut rotasi
- Menerapkan transformasi rotasi pada persegi panjang
- Visualisasi persegi panjang sebelum dan sesudah rotasi

#### Program 3 (p3.py) - Rotasi Lingkaran

- Membuat objek lingkaran menggunakan persamaan parametrik
- User memasukkan pusat, radius, dan sudut rotasi
- Menerapkan rotasi pada titik-titik pembentuk lingkaran
- Karena lingkaran simetris, hasil rotasi terlihat sama (kecuali ada penanda)

#### Program 4 (p4.py) - Rotasi Segi Enam

- Membuat objek segi enam dengan 6 titik sudut
- User memasukkan koordinat 6 titik secara manual
- Menerapkan transformasi rotasi menggunakan perkalian matriks
- Visualisasi segi enam sebelum dan sesudah rotasi

#### Tugas (tugas.py) - Rotasi Jajargenjang 180°

- Membuat objek jajargenjang dengan 4 titik sudut
- Menerapkan rotasi khusus 180 derajat
- Matriks rotasi 180° disederhanakan menjadi: `[[-1, 0], [0, -1]]`
- Menampilkan jajargenjang asli dan hasil rotasi dalam satu grafik

---

### 4. Perbandingan Hasil Rotasi pada Berbagai Objek

| Objek           | Hasil Rotasi                                          |
| --------------- | ----------------------------------------------------- |
| Segitiga        | Segitiga berputar sesuai sudut, bentuk tetap          |
| Persegi Panjang | Persegi panjang berputar, sisi-sisi tetap tegak lurus |
| Lingkaran       | Tetap terlihat sama (simetri rotasi)                  |
| Segi Enam       | Segi enam berputar, orientasi sudut berubah           |
| Jajargenjang    | Posisi berpindah ke kuadran berlawanan (rotasi 180°)  |

---

### 5. Karakteristik Transformasi Rotasi

1. **Isometri**: Rotasi mempertahankan jarak antar titik (bentuk dan ukuran tetap)
2. **Mempertahankan Sudut**: Sudut-sudut dalam objek tidak berubah
3. **Titik Pusat**: Rotasi selalu dilakukan terhadap titik origin (0, 0)
4. **Determinan = 1**: Matriks rotasi memiliki determinan 1 (tidak mengubah luas)
5. **Reversible**: Rotasi dapat dibalik dengan merotasi sudut negatif

---

### 6. Konversi Derajat ke Radian

Dalam implementasi, sudut perlu dikonversi dari derajat ke radian:

```python
radian = np.radians(sudut_derajat)
# atau
radian = sudut_derajat * np.pi / 180
```

---

### 7. Kesulitan yang Dihadapi

1. Memahami arah rotasi positif dan negatif
2. Mengkonversi sudut dari derajat ke radian dengan benar
3. Memahami perkalian matriks untuk transformasi titik
4. Rotasi terhadap titik selain origin memerlukan langkah tambahan (translasi)

---

### 8. Solusi dan Pembelajaran

1. **Arah Rotasi**: Sudut positif = counter-clockwise, sudut negatif = clockwise
2. **Konversi Sudut**: Menggunakan `np.radians()` untuk konversi otomatis
3. **Perkalian Matriks**: Menggunakan `np.dot()` untuk perkalian matriks dengan vektor titik
4. **Rotasi Non-Origin**: Untuk rotasi terhadap titik lain, perlu translasi ke origin dulu, rotasi, lalu translasi balik

---

### 9. Kesimpulan

Transformasi rotasi adalah salah satu transformasi geometri dasar yang sangat penting dalam grafika komputer. Dengan memahami matriks rotasi 2D, kita dapat memutar objek apapun di sekitar titik origin. Praktikum ini memberikan pemahaman praktis tentang bagaimana matematika matriks diterapkan dalam visualisasi grafis menggunakan Python dan matplotlib.

---

### 10. Referensi

- NumPy documentation untuk operasi matriks
- Matplotlib documentation untuk visualisasi
- Konsep transformasi geometri 2D dalam grafika komputer
