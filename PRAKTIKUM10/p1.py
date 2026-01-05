import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

# Fungsi untuk menerapkan translasi pada objek
def translate_cube(x, y, z, tx, ty, tz):
    # Mengubah koordinat
    translation_matrix = np.array([tx, ty, tz])
    translated_x = x + translation_matrix[0]
    translated_y = y + translation_matrix[1]
    translated_z = z + translation_matrix[2]
    return translated_x, translated_y, translated_z

# Input translasi dari pengguna
tx = float(input("Masukkan nilai translasi pada sumbu x: "))
ty = float(input("Masukkan nilai translasi pada sumbu y: "))
tz = float(input("Masukkan nilai translasi pada sumbu z: "))

# Membuat objek kubus
def create_cube(length):
    x = np.array([0, 0, 0, 0, length, length, length, length])
    y = np.array([0, 0, length, length, 0, 0, length, length])
    z = np.array([0, length, 0, length, 0, length, 0, length])
    return x, y, z

length = 3  # panjang sisi kubus
x, y, z = create_cube(length)

# translasi pada objek
translated_x, translated_y, translated_z = translate_cube(x, y, z, tx, ty, tz)

# Fungsi untuk menggambar kubus dengan garis
def draw_cube_wireframe(ax, x, y, z, color, label):
    # Definisi edges kubus (menghubungkan titik-titik)
    edges = [
        [0, 1], [1, 3], [3, 2], [2, 0],  # bottom face
        [4, 5], [5, 7], [7, 6], [6, 4],  # top face
        [0, 4], [1, 5], [2, 6], [3, 7]   # vertical edges
    ]
    
    for edge in edges:
        points = np.array([edge[0], edge[1]])
        ax.plot3D([x[points[0]], x[points[1]]], 
                  [y[points[0]], y[points[1]]], 
                  [z[points[0]], z[points[1]]], 
                  color=color, linewidth=2)
    
    # Plot titik-titik untuk visualisasi
    ax.scatter(x, y, z, color=color, s=50, alpha=0.6, label=label)

# Visualisasi objek
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Penggambaran objek asli
draw_cube_wireframe(ax, x, y, z, 'cyan', 'Asli')

# Penggambaran objek yang sudah ditranslasi
draw_cube_wireframe(ax, translated_x, translated_y, translated_z, 'red', 'Translasi')

# Menambahkan label dan legenda
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Menghindari error dengan membuat handles untuk legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Tampilkan grafik
plt.show()