"""
POSTTEST PRAKTIKUM 10 - Grafika Komputer
Kombinasi Translasi dan Penskalaan pada Objek 3D

Demonstrasi bagaimana transformasi dapat diterapkan secara BERURUTAN:
- Urutan transformasi MEMPENGARUHI hasil akhir!
- Komposisi matriks: M_total = M2 @ M1 (M1 diterapkan lebih dulu)
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# =====================================================
# DEFINISI KUBUS 3D
# =====================================================
def create_cube(size=1, center=(0, 0, 0)):
    """Membuat vertices kubus"""
    cx, cy, cz = center
    s = size / 2
    vertices = np.array([
        [cx - s, cy - s, cz - s],
        [cx + s, cy - s, cz - s],
        [cx + s, cy + s, cz - s],
        [cx - s, cy + s, cz - s],
        [cx - s, cy - s, cz + s],
        [cx + s, cy - s, cz + s],
        [cx + s, cy + s, cz + s],
        [cx - s, cy + s, cz + s],
    ])
    return vertices

cube_faces = [
    [0, 1, 2, 3], [4, 5, 6, 7],
    [0, 1, 5, 4], [2, 3, 7, 6],
    [0, 3, 7, 4], [1, 2, 6, 5],
]

# =====================================================
# MATRIKS TRANSFORMASI 3D
# =====================================================

def translation_matrix(tx, ty, tz):
    """Matriks Translasi 3D"""
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ], dtype=float)

def scaling_matrix(sx, sy, sz):
    """Matriks Penskalaan 3D"""
    return np.array([
        [sx, 0,  0,  0],
        [0,  sy, 0,  0],
        [0,  0,  sz, 0],
        [0,  0,  0,  1]
    ], dtype=float)

def apply_transformation(vertices, matrix):
    """Menerapkan matriks transformasi ke vertices"""
    n = len(vertices)
    homogeneous = np.hstack([vertices, np.ones((n, 1))])
    transformed = homogeneous @ matrix.T
    return transformed[:, :3]

def compose_matrices(*matrices):
    """
    Komposisi beberapa matriks transformasi
    Urutan: matrices[0] diterapkan PERTAMA, matrices[-1] diterapkan TERAKHIR
    Rumus: M_total = M_n @ ... @ M_2 @ M_1
    """
    result = np.eye(4)
    for M in matrices:
        result = M @ result
    return result

# =====================================================
# VISUALISASI
# =====================================================

def plot_cube(ax, vertices, faces, color, alpha=0.7, label="", edge_color='black'):
    """Menggambar kubus pada axes 3D"""
    face_vertices = [[vertices[i] for i in face] for face in faces]
    collection = Poly3DCollection(face_vertices, alpha=alpha, 
                                   facecolor=color, edgecolor=edge_color, linewidth=1)
    ax.add_collection3d(collection)
    center = vertices.mean(axis=0)
    ax.scatter(*center, color=color, s=80, marker='o', edgecolor='black')
    if label:
        ax.text(center[0], center[1], center[2] + 0.8, label, fontsize=9, ha='center')

def setup_axes(ax, title, xlim=(-2, 10), ylim=(-2, 10), zlim=(-2, 10)):
    """Setup axes 3D"""
    ax.set_title(title, fontsize=10, fontweight='bold')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_zlim(zlim)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

# =====================================================
# MAIN PROGRAM
# =====================================================

# Kubus asli (ukuran 2, pusat di origin)
original = create_cube(size=2, center=(0, 0, 0))

# Parameter transformasi
tx, ty, tz = 5, 4, 3       # Translasi
sx, sy, sz = 1.5, 1.5, 1.5 # Penskalaan (1.5x)

# Buat matriks individual
T = translation_matrix(tx, ty, tz)
S = scaling_matrix(sx, sy, sz)

# =====================================================
# SKENARIO 1: Penskalaan DULU, baru Translasi (S -> T)
# =====================================================
# Langkah: Skala objek di origin, lalu pindahkan
M_scale_then_translate = compose_matrices(S, T)  # T @ S
scaled_first = apply_transformation(original, S)
result_ST = apply_transformation(scaled_first, T)

# =====================================================
# SKENARIO 2: Translasi DULU, baru Penskalaan (T -> S)  
# =====================================================
# Langkah: Pindahkan objek, lalu skala (dari origin baru)
M_translate_then_scale = compose_matrices(T, S)  # S @ T
translated_first = apply_transformation(original, T)
result_TS = apply_transformation(translated_first, S)

# =====================================================
# VISUALISASI PERBANDINGAN
# =====================================================

fig = plt.figure(figsize=(18, 12))
fig.suptitle('Kombinasi Translasi dan Penskalaan - Urutan BERBEDA = Hasil BERBEDA', 
             fontsize=14, fontweight='bold')

# ----- Row 1: Skenario 1 (Scale -> Translate) -----
# Step 1: Original
ax1 = fig.add_subplot(231, projection='3d')
plot_cube(ax1, original, cube_faces, 'blue', label='Original')
setup_axes(ax1, 'Skenario 1 - Step 1\nObjek Asli')

# Step 2: After Scaling
ax2 = fig.add_subplot(232, projection='3d')
plot_cube(ax2, original, cube_faces, 'blue', alpha=0.2)
plot_cube(ax2, scaled_first, cube_faces, 'orange', label='Scaled')
setup_axes(ax2, f'Skenario 1 - Step 2\nSetelah PENSKALAAN ({sx}x)')

# Step 3: After Translation
ax3 = fig.add_subplot(233, projection='3d')
plot_cube(ax3, original, cube_faces, 'blue', alpha=0.2)
plot_cube(ax3, scaled_first, cube_faces, 'orange', alpha=0.3)
plot_cube(ax3, result_ST, cube_faces, 'green', label='Final')
setup_axes(ax3, f'Skenario 1 - Step 3\nSetelah TRANSLASI ({tx},{ty},{tz})')

# ----- Row 2: Skenario 2 (Translate -> Scale) -----
# Step 1: Original
ax4 = fig.add_subplot(234, projection='3d')
plot_cube(ax4, original, cube_faces, 'blue', label='Original')
setup_axes(ax4, 'Skenario 2 - Step 1\nObjek Asli')

# Step 2: After Translation
ax5 = fig.add_subplot(235, projection='3d')
plot_cube(ax5, original, cube_faces, 'blue', alpha=0.2)
plot_cube(ax5, translated_first, cube_faces, 'cyan', label='Translated')
setup_axes(ax5, f'Skenario 2 - Step 2\nSetelah TRANSLASI ({tx},{ty},{tz})')

# Step 3: After Scaling
ax6 = fig.add_subplot(236, projection='3d')
plot_cube(ax6, original, cube_faces, 'blue', alpha=0.2)
plot_cube(ax6, translated_first, cube_faces, 'cyan', alpha=0.3)
plot_cube(ax6, result_TS, cube_faces, 'red', label='Final')
setup_axes(ax6, f'Skenario 2 - Step 3\nSetelah PENSKALAAN ({sx}x)', 
           xlim=(-2, 12), ylim=(-2, 12), zlim=(-2, 12))

plt.tight_layout()

# =====================================================
# CETAK INFORMASI DETAIL
# =====================================================

print("=" * 70)
print("KOMBINASI TRANSLASI DAN PENSKALAAN PADA OBJEK 3D")
print("=" * 70)

print("\n📦 OBJEK ASLI:")
print(f"   Ukuran: 2 x 2 x 2")
print(f"   Pusat: (0, 0, 0)")
print(f"   Vertices:\n{original}")

print("\n📊 PARAMETER TRANSFORMASI:")
print(f"   Translasi (T): tx={tx}, ty={ty}, tz={tz}")
print(f"   Penskalaan (S): sx={sx}, sy={sy}, sz={sz}")

print("\n" + "=" * 70)
print("🔷 SKENARIO 1: PENSKALAAN dulu, baru TRANSLASI (S → T)")
print("=" * 70)
print("\nLangkah 1 - Penskalaan:")
print(f"   Matriks S:\n{S}")
print(f"\n   Vertices setelah penskalaan:\n{scaled_first}")
print(f"   → Ukuran: {2*sx} x {2*sy} x {2*sz}, Pusat: (0, 0, 0)")

print("\nLangkah 2 - Translasi:")
print(f"   Matriks T:\n{T}")
print(f"\n   Vertices HASIL AKHIR:\n{result_ST}")
print(f"   → Ukuran: {2*sx} x {2*sy} x {2*sz}, Pusat: ({tx}, {ty}, {tz})")

print("\nMatriks Komposisi (T @ S):")
print(M_scale_then_translate)

print("\n" + "=" * 70)
print("🔶 SKENARIO 2: TRANSLASI dulu, baru PENSKALAAN (T → S)")
print("=" * 70)
print("\nLangkah 1 - Translasi:")
print(f"   Matriks T:\n{T}")
print(f"\n   Vertices setelah translasi:\n{translated_first}")
print(f"   → Ukuran: 2 x 2 x 2, Pusat: ({tx}, {ty}, {tz})")

print("\nLangkah 2 - Penskalaan (dari origin!):")
print(f"   Matriks S:\n{S}")
print(f"\n   Vertices HASIL AKHIR:\n{result_TS}")
center_TS = result_TS.mean(axis=0)
print(f"   → Ukuran: {2*sx} x {2*sy} x {2*sz}, Pusat: ({center_TS[0]:.1f}, {center_TS[1]:.1f}, {center_TS[2]:.1f})")

print("\nMatriks Komposisi (S @ T):")
print(M_translate_then_scale)

print("\n" + "=" * 70)
print("📊 PERBANDINGAN HASIL AKHIR:")
print("=" * 70)
print(f"""
┌─────────────────────┬────────────────────────────┬────────────────────────────┐
│       Aspek         │  Skenario 1 (S → T)        │  Skenario 2 (T → S)        │
│                     │  Skala dulu, Translasi     │  Translasi dulu, Skala     │
├─────────────────────┼────────────────────────────┼────────────────────────────┤
│ Ukuran Akhir        │  {2*sx} x {2*sy} x {2*sz}                   │  {2*sx} x {2*sy} x {2*sz}                   │
│ Pusat Akhir         │  ({tx}, {ty}, {tz})                 │  ({center_TS[0]:.1f}, {center_TS[1]:.1f}, {center_TS[2]:.1f})              │
│ Jarak dari Origin   │  √({tx}²+{ty}²+{tz}²) = {np.sqrt(tx**2+ty**2+tz**2):.2f}      │  √({center_TS[0]:.1f}²+{center_TS[1]:.1f}²+{center_TS[2]:.1f}²) = {np.sqrt(center_TS[0]**2+center_TS[1]**2+center_TS[2]**2):.2f}  │
└─────────────────────┴────────────────────────────┴────────────────────────────┘
""")

print("🔑 KESIMPULAN PENTING:")
print("-" * 70)
print("""
1. URUTAN TRANSFORMASI MEMPENGARUHI HASIL!
   - Skenario 1 (S→T): Objek diskala di origin, lalu dipindahkan
   - Skenario 2 (T→S): Objek dipindahkan, lalu diskala dari ORIGIN
   
2. PENSKALAAN selalu relatif terhadap ORIGIN (0,0,0)
   - Jika objek sudah di-translate, penskalaan akan mengubah posisi pusat!
   
3. RUMUS KOMPOSISI MATRIKS:
   - Untuk urutan M1 → M2 → M3, matriks total = M3 @ M2 @ M1
   - Matriks yang diterapkan TERAKHIR ditulis PERTAMA dalam perkalian
   
4. TIPS PRAKTIS:
   - Jika ingin skala objek di tempat: Translate ke origin → Scale → Translate balik
   - Urutan standar: Scale → Rotate → Translate (SRT)
""")

plt.show()
