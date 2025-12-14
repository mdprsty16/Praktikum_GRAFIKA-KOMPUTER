import numpy as np
import matplotlib.pyplot as plt

def gambar_jajargenjang(titik, warna, label):
    titik_plot = np.vstack([titik, titik[0]])
    plt.plot(titik_plot[:, 0], titik_plot[:, 1], color=warna, label=label)

def rotasi_180(titik):
    rotasi_matrix = np.array([[-1, 0],
                              [0, -1]])
    return np.dot(titik, rotasi_matrix.T)

print("Masukkan koordinat titik-titik jajargenjang:")

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))
x4 = float(input("x4: "))
y4 = float(input("y4: "))

titik_asli = np.array([[x1, y1],
                        [x2, y2],
                        [x3, y3],
                        [x4, y4]])

titik_rotasi = rotasi_180(titik_asli)

plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

gambar_jajargenjang(titik_asli, 'b', 'Jajargenjang Asli')
gambar_jajargenjang(titik_rotasi, 'r', 'Jajargenjang Rotasi 180°')

plt.title('Rotasi Jajargenjang 180 Derajat')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()
