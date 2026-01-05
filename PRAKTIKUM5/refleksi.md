# REFLEKSI PRAKTIKUM 5

## Transformasi Translasi pada Objek 2D

---

### 1. Tujuan Praktikum

Praktikum 5 bertujuan untuk memahami dan mengimplementasikan transformasi **Translasi** pada berbagai objek 2D menggunakan Python, NumPy, dan matplotlib.

---

### 2. Konsep yang Dipelajari

#### A. Apa itu Translasi?

Translasi adalah transformasi geometri yang memindahkan setiap titik objek dengan jarak dan arah yang sama. Translasi tidak mengubah bentuk, ukuran, atau orientasi objek - hanya memindahkan posisinya.

#### B. Vektor Translasi

Translasi didefinisikan oleh vektor translasi (dx, dy) di mana:

- `dx` = perpindahan pada sumbu X (horizontal)
- `dy` = perpindahan pada sumbu Y (vertikal)

#### C. Rumus Transformasi

Untuk titik (x, y) yang ditranslasi dengan vektor (dx, dy) menjadi (x', y'):

```
x' = x + dx
y' = y + dy
```

Dalam notasi matriks (koordinat homogen):

```
| x' |   | 1  0  dx |   | x |
| y' | = | 0  1  dy | × | y |
| 1  |   | 0  0  1  |   | 1 |
```

---

### 3. Implementasi Program

#### Program 1 (p1.py) - Translasi Segitiga (Nilai Tetap)

- Membuat segitiga dengan titik-titik yang sudah ditentukan: (1,2), (3,5), (6,2)
- Vektor translasi tetap: (2, 3)
- Menampilkan segitiga asli (biru) dan hasil translasi (merah)
- Visualisasi dalam satu grafik dengan legend

#### Program 2 (p2.py) - Translasi Segitiga (Input Dinamis)

- User memasukkan koordinat 3 titik segitiga dalam format x,y
- User memasukkan vektor translasi (dx, dy)
- Dilengkapi validasi input dengan error handling
- Batas sumbu otomatis menyesuaikan dengan margin

#### Program 3 (p3.py) - Translasi Persegi Panjang

- Mendukung mode demo (--demo) dan mode interaktif
- User memasukkan 4 titik persegi panjang
- Menggunakan argparse untuk command line arguments
- Visualisasi persegi panjang sebelum dan sesudah translasi

#### Program 4 (p4.py) - Translasi Lingkaran

- Translasi pada lingkaran dilakukan dengan memindahkan titik pusat
- User memasukkan pusat, radius, dan vektor translasi
- Radius lingkaran tetap, hanya posisi yang berubah
- Mendukung mode demo untuk testing cepat

#### Tugas (tugas.py) - Visualisasi Jajargenjang

- Membuat jajargenjang dengan titik-titik yang ditentukan
- Menghitung titik intersection dengan garis pembatas horizontal
- Menampilkan grid dan pengaturan sumbu yang detail
- Visualisasi jajargenjang dengan garis pembatas tengah

---

### 4. Perbandingan Translasi pada Berbagai Objek

| Objek           | Metode Translasi             | Hasil                      |
| --------------- | ---------------------------- | -------------------------- |
| Segitiga        | Translasi setiap titik sudut | Segitiga berpindah posisi  |
| Persegi Panjang | Translasi 4 titik sudut      | Persegi panjang berpindah  |
| Lingkaran       | Translasi titik pusat        | Lingkaran berpindah posisi |
| Jajargenjang    | Translasi setiap titik sudut | Jajargenjang berpindah     |

---

### 5. Karakteristik Transformasi Translasi

1. **Mempertahankan Bentuk**: Objek tidak berubah bentuknya
2. **Mempertahankan Ukuran**: Dimensi objek tetap sama
3. **Mempertahankan Orientasi**: Sudut dan arah objek tidak berubah
4. **Rigid Transformation**: Termasuk transformasi rigid (tidak mendeformasi objek)
5. **Reversible**: Dapat dibalik dengan translasi (-dx, -dy)

---

### 6. Teknik Implementasi yang Dipelajari

#### A. List Comprehension untuk Translasi

```python
def translasi(titik, vektor):
    return [(x + vektor[0], y + vektor[1]) for x, y in titik]
```

#### B. Input Validation

```python
def input_point(prompt):
    while True:
        try:
            s = input(prompt)
            x, y = map(float, s.split(','))
            return (x, y)
        except Exception:
            print("Format salah...")
```

#### C. Command Line Arguments

```python
parser = argparse.ArgumentParser()
parser.add_argument('--demo', action='store_true')
```

---

### 7. Kesulitan yang Dihadapi

1. Memahami format input koordinat yang user-friendly
2. Mengatur batas sumbu (xlim, ylim) agar kedua objek terlihat
3. Implementasi validasi input yang robust
4. Menggambar objek tertutup (menutup poligon dengan titik awal)

---

### 8. Solusi dan Pembelajaran

1. **Format Input**: Menggunakan format "x,y" dengan split dan map
2. **Batas Sumbu**: Menghitung min/max dari semua titik + margin
3. **Validasi Input**: Menggunakan try-except dalam loop while
4. **Poligon Tertutup**: Menambahkan titik pertama di akhir array dengan np.vstack

---

### 9. Perbedaan dengan Transformasi Lain

| Transformasi | Mengubah Posisi | Mengubah Ukuran | Mengubah Orientasi |
| ------------ | --------------- | --------------- | ------------------ |
| Translasi    | ✓               | ✗               | ✗                  |
| Scaling      | ✗               | ✓               | ✗                  |
| Rotasi       | ✗               | ✗               | ✓                  |
| Shearing     | ✗               | ✗               | ✓                  |

---

### 10. Kesimpulan

Transformasi translasi adalah transformasi geometri paling sederhana yang memindahkan objek tanpa mengubah properti lainnya. Praktikum ini memberikan pemahaman praktis tentang cara mengimplementasikan translasi pada berbagai bentuk geometri (segitiga, persegi panjang, lingkaran, jajargenjang) dengan berbagai pendekatan input (nilai tetap, input interaktif, command line arguments).

---

### 11. Referensi

- NumPy documentation untuk operasi array
- Matplotlib documentation untuk visualisasi
- Argparse documentation untuk command line interface
- Konsep transformasi geometri 2D dalam grafika komputer
