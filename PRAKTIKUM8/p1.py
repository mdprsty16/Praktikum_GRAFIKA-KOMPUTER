import matplotlib.pyplot as plt
import numpy as np

def gambar_segitiga(titik):
    x = [titik[0][0], titik[1][0], titik[2][0], titik[0][0]]
    y = [titik[0][1], titik[1][1], titik[2][1], titik[0][1]]

    plt.plot(x, y, marker='o')
    plt.fill(x, y, alpha=0.3)

def pencerminan(titik, sumbu):
    if sumbu == 'x':
        return [(x, -y) for (x, y) in titik]
    elif sumbu == 'y':
        return [(-x, y) for (x, y) in titik]
    else:
        raise ValueError("Sumbu tidak valid. Pilih 'x', 'y', atau 'origin'.")
    
titik_segitiga = []
print("Masukkan koordinat titik segitiga (format: x,y): ")
for i in range(3):
    koordinat = input(f"Titik {i+1}: ")
    x, y = map(float, koordinat.split(','))
    titik_segitiga.append((x, y))

sumbu = input("Masukkan sumbu pencerminan (x, y, origin): ")

plt.figure(figsize=(8, 8))
plt.title("Pencerminan Segitiga 2D")
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

gambar_segitiga(titik_segitiga)
titik_segitiga_pencerminan = pencerminan(titik_segitiga, sumbu)
gambar_segitiga(titik_segitiga_pencerminan)

plt.legend(['Segitiga Asli', 'Segitiga Setelah Pencerminan'])
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()