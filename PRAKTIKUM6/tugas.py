import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_cylinder_data(radius, height, center_x=0, center_y=0, z_start=0):
    # Membuat grid untuk permukaan tabung
    z = np.linspace(z_start, z_start + height, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    
    # Konversi koordinat polar ke Cartesian
    x_grid = radius * np.cos(theta_grid) + center_x
    y_grid = radius * np.sin(theta_grid) + center_y
    
    return x_grid, y_grid, z_grid

# --- Parameter Awal ---
radius_awal = 2.5
tinggi_awal = 5.0
faktor_skala = 2.0

# Generate data tabung awal
x, y, z = get_cylinder_data(radius_awal, tinggi_awal)

# --- Membuat Plot ---
fig = plt.figure(figsize=(8, 10))

# 1. Plot Tabung Awal (Gambar Atas)
ax1 = fig.add_subplot(2, 1, 1, projection='3d')
ax1.plot_surface(x, y, z, color='black', alpha=0.9) # Alpha untuk transparansi
ax1.set_title("Tabung Awal")
ax1.set_xlim(-10, 10)
ax1.set_ylim(-10, 10)
ax1.set_zlim(0, 10)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# 2. Plot Tabung Setelah Penskalaan (Gambar Bawah)
# Proses Penskalaan: Kalikan koordinat x, y, dan z dengan faktor skala
x_scaled = x * faktor_skala
y_scaled = y * faktor_skala
z_scaled = z * faktor_skala

ax2 = fig.add_subplot(2, 1, 2, projection='3d')
# Menggunakan wireframe atau surface dengan edge color agar mirip gambar kedua
ax2.plot_surface(x_scaled, y_scaled, z_scaled, color='gray', alpha=0.5, edgecolor='black', linewidth=0.5)
ax2.set_title(f"Tabung Setelah Penskalaan (Faktor Skala: {faktor_skala})")
ax2.set_xlim(-10, 10)
ax2.set_ylim(-10, 10)
ax2.set_zlim(0, 10) # Sesuaikan batas Z agar tabung terlihat penuh
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

plt.tight_layout()
plt.show()