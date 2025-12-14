import matplotlib.pyplot as plt

def bresenham_line(x_start, y_start, dx, dy):
    """
    Mengimplementasikan Algoritma Bresenham untuk kemiringan (m) antara 0 dan 1 (0 < m <= 1),
    di mana dx > dy.
    """
    x = x_start
    y = y_start
    p = 2 * dy - dx
    const_p_neg = 2 * dy
    const_p_pos = 2 * dy - 2 * dx
    
    points = [(x, y)]
    
    for _ in range(dx): # Iterasi sebanyak dx langkah
        x += 1
        if p >= 0:
            y += 1
            p += const_p_pos
        else:
            p += const_p_neg
        points.append((x, y))
    return points

def plot_bresenham_line(points, x_start, y_start, x_end, y_end):
    """
    Menggambar garis Bresenham menggunakan matplotlib.
    """
    
    # Ekstrak koordinat x dan y dari list points
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    plt.figure(figsize=(8, 8)) # Ukuran plot
    
    # Gambar semua titik sebagai kotak (piksel)
    # Gunakan scatter plot untuk menyoroti setiap titik
    plt.scatter(x_coords, y_coords, color='cyan', s=500, marker='s', edgecolors='white', linewidths=0.8, alpha=0.8, label='Bresenham Pixels')
    
    # Tampilkan koordinat x dan y di dalam kotak piksel
    for i, (x, y) in enumerate(points):
        # Penyesuaian offset agar teks di tengah kotak
        plt.text(x, y - 0.05, f'({x},{y})', ha='center', va='center', color='black', fontsize=8, weight='bold')

    # Atur grid agar terlihat seperti piksel
    # Batas plot sedikit lebih besar dari rentang koordinat
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    
    plt.xticks(range(min_x - 1, max_x + 2))
    plt.yticks(range(min_y - 1, max_y + 2))
    
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.title('Visualisasi Algoritma Bresenham', fontsize=16)
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)
    
    plt.gca().set_aspect('equal', adjustable='box') # Memastikan skala x dan y sama
    plt.legend()
    plt.show()

# --- Eksekusi Kode ---
x_start = 10
y_start = 10
dx = 7
dy = 6

# Dapatkan titik akhir untuk label
x_end = x_start + dx
y_end = y_start + dy

# Jalankan fungsi Bresenham untuk mendapatkan titik-titik
hasil_titik = bresenham_line(x_start, y_start, dx, dy)

# Tampilkan plot
plot_bresenham_line(hasil_titik, x_start, y_start, x_end, y_end)

print("Titik-titik yang dihasilkan oleh Algoritma Bresenham:")
print(hasil_titik)