import matplotlib.pyplot as plt
import numpy as np

def gambar_persegi_panjang(titik, judul):
    x = [p[0] for p in titik] + [titik[0][0]]
    y = [p[1] for p in titik] + [titik[0][1]]
    plt.plot(x, y, marker='o')
    plt.title(judul)
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')

def shear(points, shear_x, shear_y):
    shear_matrix = np.array([
        [1, shear_x],
        [shear_y, 1]
    ])
    return np.dot(points, shear_matrix.T)

x = 0
y = 0
lebar = 8
tinggi = 4
shear_x = 0.8
shear_y = 0.3

persegi_panjang = np.array([
    [x, y],
    [x + lebar, y],
    [x + lebar, y + tinggi],
    [x, y + tinggi]
])

hasil_shear = shear(persegi_panjang, shear_x, shear_y)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
gambar_persegi_panjang(persegi_panjang, "Persegi Panjang Asli")
plt.subplot(1, 2, 2)
gambar_persegi_panjang(hasil_shear, "Persegi Panjang Setelah Shear")

plt.tight_layout()
plt.show()
