import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar garis menggunakan algoritma DDA
def dda_algorithm(x0, y0, x1, y1):
    # Menghitung perubahan koordinat
    dx = x1 - x0
    dy = y1 - y0

    # Menentukan jumlah langkah berdasarkan jarak terpanjang (step)
    steps = max(abs(dx), abs(dy))

    # Menghitung perubahan x dan y per langkah
    # Penggunaan float() memastikan hasil adalah pecahan
    Xinc = dx / float(steps) 
    Yinc = dy / float(steps) 

    # Inisialisasi titik awal
    x = x0
    y = y0

    # Menyimpan titik-titik hasil algoritma DDA
    x_points = [x]  # Tambahkan titik awal
    y_points = [y]  # Tambahkan titik awal

    # Loop untuk menghitung titik-titik sepanjang garis
    # Loop dijalankan sebanyak 'steps' kali (untuk menghitung piksel berikutnya)
    for i in range(int(steps)):
        x += Xinc
        y += Yinc
        
        # Menyimpan koordinat dengan pembulatan ke integer terdekat
        x_points.append(round(x))
        y_points.append(round(y))
        
    # Menggambar garis menggunakan matplotlib
    plt.plot(x_points, y_points, marker='o', color='b')
    plt.title(f"Garis DDA dari ({x0}, {y0}) ke ({x1}, {y1})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# Meminta input dari pengguna untuk titik awal dan titik akhir
try:
    print("--- Input Titik Awal (x0, y0) ---")
    x0 = int(input("Masukkan koordinat x0 (titik awal): "))
    y0 = int(input("Masukkan koordinat y0 (titik awal): "))
    print("--- Input Titik Akhir (x1, y1) ---")
    x1 = int(input("Masukkan koordinat x1 (titik akhir): "))
    y1 = int(input("Masukkan koordinat y1 (titik akhir): "))
    
    # Memanggil fungsi DDA untuk menggambar garis
    dda_algorithm(x0, y0, x1, y1)

except ValueError:
    print("\nError: Masukkan harus berupa bilangan bulat (integer).")