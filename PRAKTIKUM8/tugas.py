import matplotlib.pyplot as plt

def gambar_belahketupat(ax, titik, label='Belah Ketupat', edgecolor='blue'):
    # titik berisi 4 titik: atas, kanan, bawah, kiri
    x = [titik[0][0], titik[1][0], titik[2][0], titik[3][0], titik[0][0]]
    y = [titik[0][1], titik[1][1], titik[2][1], titik[3][1], titik[0][1]]
    ax.plot(x, y, marker='o', color=edgecolor, linewidth=2, label=label)
    ax.fill(x, y, alpha=0.3, color=edgecolor)

def pencerminan_sumbu_x(titik):
    return [(x, -y) for (x, y) in titik]

# Input pusat dan diagonal belah ketupat
print("Masukkan data belah ketupat:")
cx = float(input("Koordinat x pusat: "))
cy = float(input("Koordinat y pusat: "))
d1 = float(input("Panjang diagonal horizontal: "))
d2 = float(input("Panjang diagonal vertikal: "))

# Membuat titik-titik belah ketupat (atas, kanan, bawah, kiri)
titik_belahketupat = [
    (cx, cy + d2/2),      # atas
    (cx + d1/2, cy),      # kanan
    (cx, cy - d2/2),      # bawah
    (cx - d1/2, cy)       # kiri
]

fig, ax = plt.subplots(figsize=(8, 8))

# Gambar belah ketupat asli
gambar_belahketupat(ax, titik_belahketupat, label='Belah Ketupat Asli', edgecolor='blue')

# Pencerminan terhadap sumbu x
titik_pencerminan = pencerminan_sumbu_x(titik_belahketupat)
gambar_belahketupat(ax, titik_pencerminan, label='Belah Ketupat Setelah Pencerminan (Sumbu X)', edgecolor='red')

ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_aspect('equal', adjustable='box')
ax.axhline(0, color='black', linewidth=0.5, ls='--')
ax.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title("Pencerminan Belah Ketupat terhadap Sumbu X")
plt.show()
