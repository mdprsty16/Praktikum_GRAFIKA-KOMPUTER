"""
PRETEST PRAKTIKUM 10 - Grafika Komputer
Translasi dan Penskalaan pada Objek 3D

Perbedaan Translasi vs Penskalaan:
- TRANSLASI: Memindahkan objek ke posisi baru TANPA mengubah ukuran/bentuk
- PENSKALAAN: Mengubah ukuran objek (memperbesar/memperkecil) dari titik pusat
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# =====================================================
# DEFINISI KUBUS 3D (Objek Asli)
# =====================================================
def create_cube(size=1, center=(0, 0, 0)):
    """Membuat vertices kubus dengan ukuran dan pusat tertentu"""
    cx, cy, cz = center
    s = size / 2
    
    # 8 vertices kubus
    vertices = np.array([
        [cx - s, cy - s, cz - s],  # 0: kiri-bawah-belakang
        [cx + s, cy - s, cz - s],  # 1: kanan-bawah-belakang
        [cx + s, cy + s, cz - s],  # 2: kanan-atas-belakang
        [cx - s, cy + s, cz - s],  # 3: kiri-atas-belakang
        [cx - s, cy - s, cz + s],  # 4: kiri-bawah-depan
        [cx + s, cy - s, cz + s],  # 5: kanan-bawah-depan
        [cx + s, cy + s, cz + s],  # 6: kanan-atas-depan
        [cx - s, cy + s, cz + s],  # 7: kiri-atas-depan
    ])
    return vertices

# Definisi 6 faces kubus (indeks vertices)
cube_faces = [
    [0, 1, 2, 3],  # belakang
    [4, 5, 6, 7],  # depan
    [0, 1, 5, 4],  # bawah
    [2, 3, 7, 6],  # atas
    [0, 3, 7, 4],  # kiri
    [1, 2, 6, 5],  # kanan
]

# =====================================================
# MATRIKS TRANSFORMASI 3D
# =====================================================

def translation_matrix(tx, ty, tz):
    """
    Matriks Translasi 3D (4x4)
    Memindahkan objek sebesar (tx, ty, tz)
    
    | 1  0  0  tx |
    | 0  1  0  ty |
    | 0  0  1  tz |
    | 0  0  0  1  |
    """
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def scaling_matrix(sx, sy, sz):
    """
    Matriks Penskalaan 3D (4x4)
    Mengubah ukuran objek dengan faktor (sx, sy, sz)
    
    | sx  0   0   0 |
    | 0   sy  0   0 |
    | 0   0   sz  0 |
    | 0   0   0   1 |
    """
    return np.array([
        [sx, 0,  0,  0],
        [0,  sy, 0,  0],
        [0,  0,  sz, 0],
        [0,  0,  0,  1]
    ])

def apply_transformation(vertices, matrix):
    """Menerapkan matriks transformasi ke vertices"""
    # Konversi ke homogeneous coordinates (tambah kolom 1)
    n = len(vertices)
    homogeneous = np.hstack([vertices, np.ones((n, 1))])
    
    # Kalikan dengan matriks transformasi
    transformed = homogeneous @ matrix.T
    
    # Kembalikan ke koordinat 3D (buang kolom terakhir)
    return transformed[:, :3]

# =====================================================
# VISUALISASI
# =====================================================

def plot_cube(ax, vertices, faces, color, alpha=0.7, label=""):
    """Menggambar kubus pada axes 3D"""
    face_vertices = [[vertices[i] for i in face] for face in faces]
    collection = Poly3DCollection(face_vertices, alpha=alpha, 
                                   facecolor=color, edgecolor='black', linewidth=1)
    ax.add_collection3d(collection)
    
    # Tandai titik pusat
    center = vertices.mean(axis=0)
    ax.scatter(*center, color=color, s=50, marker='o')
    if label:
        ax.text(center[0], center[1], center[2] + 0.5, label, fontsize=9)

# =====================================================
# MAIN PROGRAM
# =====================================================

# Buat kubus asli (ukuran 2, di pusat origin)
original_vertices = create_cube(size=2, center=(0, 0, 0))

# Parameter transformasi
tx, ty, tz = 4, 3, 2      # Translasi: geser (4, 3, 2)
sx, sy, sz = 2, 2, 2      # Penskalaan: perbesar 2x

# Terapkan transformasi
T = translation_matrix(tx, ty, tz)
S = scaling_matrix(sx, sy, sz)

translated_vertices = apply_transformation(original_vertices, T)
scaled_vertices = apply_transformation(original_vertices, S)

# =====================================================
# VISUALISASI PERBANDINGAN
# =====================================================

fig = plt.figure(figsize=(16, 5))
fig.suptitle('Perbandingan Translasi vs Penskalaan pada Objek 3D (Kubus)', fontsize=14, fontweight='bold')

# ----- Subplot 1: Objek Asli -----
ax1 = fig.add_subplot(131, projection='3d')
ax1.set_title('Objek Asli\n(Kubus ukuran 2, pusat di origin)', fontsize=10)
plot_cube(ax1, original_vertices, cube_faces, 'blue', label='Original')
ax1.set_xlim(-5, 8)
ax1.set_ylim(-5, 8)
ax1.set_zlim(-5, 8)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# ----- Subplot 2: Setelah Translasi -----
ax2 = fig.add_subplot(132, projection='3d')
ax2.set_title(f'Setelah TRANSLASI\n(tx={tx}, ty={ty}, tz={tz})', fontsize=10)
plot_cube(ax2, original_vertices, cube_faces, 'blue', alpha=0.3, label='Original')
plot_cube(ax2, translated_vertices, cube_faces, 'green', label='Translated')
ax2.set_xlim(-5, 8)
ax2.set_ylim(-5, 8)
ax2.set_zlim(-5, 8)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

# ----- Subplot 3: Setelah Penskalaan -----
ax3 = fig.add_subplot(133, projection='3d')
ax3.set_title(f'Setelah PENSKALAAN\n(sx={sx}, sy={sy}, sz={sz})', fontsize=10)
plot_cube(ax3, original_vertices, cube_faces, 'blue', alpha=0.3, label='Original')
plot_cube(ax3, scaled_vertices, cube_faces, 'red', label='Scaled')
ax3.set_xlim(-5, 8)
ax3.set_ylim(-5, 8)
ax3.set_zlim(-5, 8)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')

plt.tight_layout()

# =====================================================
# CETAK INFORMASI TRANSFORMASI
# =====================================================

print("=" * 60)
print("PERBANDINGAN TRANSLASI vs PENSKALAAN PADA OBJEK 3D")
print("=" * 60)

print("\n📦 OBJEK ASLI (Kubus):")
print(f"   Vertices:\n{original_vertices}")
print(f"   Ukuran: 2 x 2 x 2")
print(f"   Pusat: (0, 0, 0)")

print("\n" + "-" * 60)
print("🔄 TRANSLASI (Perpindahan)")
print("-" * 60)
print(f"Parameter: tx={tx}, ty={ty}, tz={tz}")
print("\nMatriks Translasi:")
print(T)
print(f"\nHasil Vertices setelah translasi:\n{translated_vertices}")
print(f"\n✅ HASIL TRANSLASI:")
print(f"   - Ukuran: TETAP (2 x 2 x 2)")
print(f"   - Pusat BARU: ({tx}, {ty}, {tz})")
print(f"   - Bentuk: TIDAK BERUBAH")

print("\n" + "-" * 60)
print("📐 PENSKALAAN (Perubahan Ukuran)")
print("-" * 60)
print(f"Parameter: sx={sx}, sy={sy}, sz={sz}")
print("\nMatriks Penskalaan:")
print(S)
print(f"\nHasil Vertices setelah penskalaan:\n{scaled_vertices}")
print(f"\n✅ HASIL PENSKALAAN:")
print(f"   - Ukuran BARU: {2*sx} x {2*sy} x {2*sz}")
print(f"   - Pusat: TETAP di (0, 0, 0)")
print(f"   - Bentuk: DIPERBESAR {sx}x dari pusat")

print("\n" + "=" * 60)
print("📊 KESIMPULAN PERBEDAAN:")
print("=" * 60)
print("""
┌─────────────────┬─────────────────────────┬─────────────────────────┐
│     Aspek       │      TRANSLASI          │      PENSKALAAN         │
├─────────────────┼─────────────────────────┼─────────────────────────┤
│ Posisi          │ BERUBAH (pindah)        │ TETAP (dari pusat)      │
│ Ukuran          │ TETAP                   │ BERUBAH (besar/kecil)   │
│ Bentuk          │ TETAP                   │ TETAP (proporsional)    │
│ Orientasi       │ TETAP                   │ TETAP                   │
│ Jarak ke Origin │ BERUBAH                 │ TETAP (pusat)           │
└─────────────────┴─────────────────────────┴─────────────────────────┘

TRANSLASI: Memindahkan SELURUH titik objek dengan offset yang SAMA
           (x', y', z') = (x + tx, y + ty, z + tz)

PENSKALAAN: Mengalikan SETIAP koordinat dengan faktor skala
           (x', y', z') = (x * sx, y * sy, z * sz)
""")

plt.show()
