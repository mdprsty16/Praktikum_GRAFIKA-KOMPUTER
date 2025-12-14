import numpy as np
import matplotlib.pyplot as plt

def gambar_segitiga(titik):
	segitiga = plt.Polygon(titik, closed=True, fill=False, edgecolor='b')
	plt.gca().add_patch(segitiga)

def rotasi(titik, sudut):
	radian = np.radians(sudut)
	rotasi_matrix = np.array([[np.cos(radian), -np.sin(radian)], [np.sin(radian), np.cos(radian)]])
	titik_rotated = np.dot(titik, rotasi_matrix.T)
	return titik_rotated

x1 = float(input('Masukkan koordinat x1: '))
y1 = float(input('Masukkan koordinat y1: '))
x2 = float(input('Masukkan koordinat x2: '))
y2 = float(input('Masukkan koordinat y2: '))
x3 = float(input('Masukkan koordinat x3: '))
y3 = float(input('Masukkan koordinat y3: '))
sudut_rotasi = float(input('Masukkan sudut rotasi (dalam derajat): '))

titik_asli = np.array([[x1, y1], [x2, y2], [x3, y3]])

plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
gambar_segitiga(titik_asli)
plt.title('Segitiga Sebelum Rotasi')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

titik_rotated = rotasi(titik_asli, sudut_rotasi)

plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
seg = plt.Polygon(titik_rotated, closed=True, fill=False, edgecolor='r')
plt.gca().add_patch(seg)
plt.title(f'Segitiga Setelah Rotasi ({sudut_rotasi} Derajat)')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()