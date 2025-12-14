import numpy as np
import matplotlib.pyplot as plt

def gambar_lingkaran(radius, center):
	theta = np.linspace(0, 2 * np.pi, 200)
	x = radius * np.cos(theta) + center[0]
	y = radius * np.sin(theta) + center[1]
	plt.plot(x, y, label='Lingkaran', color='b')

def rotasi(center, radius, sudut):
	theta = np.linspace(0, 2 * np.pi, 200)
	rad = np.radians(sudut)
	x_rot = radius * np.cos(theta + rad) + center[0]
	y_rot = radius * np.sin(theta + rad) + center[1]
	return x_rot, y_rot

center_x = float(input('Masukkan koordinat pusat x: '))
center_y = float(input('Masukkan koordinat pusat y: '))
radius = float(input('Masukkan radius lingkaran: '))
sudut_rotasi = float(input('Masukkan sudut rotasi (dalam derajat): '))

plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
gambar_lingkaran(radius, (center_x, center_y))
plt.title('Lingkaran Sebelum Rotasi')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()

x_rot, y_rot = rotasi((center_x, center_y), radius, sudut_rotasi)

plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.plot(x_rot, y_rot, label='Lingkaran Rotasi', color='r')
plt.title(f'Lingkaran Setelah Rotasi ({sudut_rotasi} Derajat)')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()