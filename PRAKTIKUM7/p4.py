import numpy as np
import matplotlib.pyplot as plt

def gambar_segi_enam(titik):
	titik_plot = np.vstack([titik, titik[0]])
	plt.plot(titik_plot[:,0], titik_plot[:,1], label='Segi Enam', color='b')

def rotasi(titik, sudut):
	radian = np.radians(sudut)
	rotasi_matrix = np.array([[np.cos(radian), -np.sin(radian)], [np.sin(radian), np.cos(radian)]])
	titik_rotated = np.dot(titik, rotasi_matrix.T)
	return titik_rotated

print('Masukkan koordinat titik-titik segi enam (x, y):')
titik = []
for i in range(6):
	x = float(input(f'Koordinat x titik {i+1}: '))
	y = float(input(f'Koordinat y titik {i+1}: '))
	titik.append([x, y])
titik = np.array(titik)
sudut_rotasi = float(input('Masukkan sudut rotasi (dalam derajat): '))

plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
gambar_segi_enam(titik)
plt.title('Segi Enam Sebelum Rotasi')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()

titik_rotated = rotasi(titik, sudut_rotasi)

plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
gambar_segi_enam(titik_rotated)
plt.title(f'Segi Enam Setelah Rotasi ({sudut_rotasi} Derajat)')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()