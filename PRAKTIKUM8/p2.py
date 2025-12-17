import matplotlib.pyplot as plt

def gambar_persegi_panjang(ax, x, y, lebar, tinggi, label='Persegi Panjang', edgecolor='blue'):
    persegi_panjang = plt.Rectangle((x, y), lebar, tinggi, fill=None, edgecolor=edgecolor, linewidth=2, label=label)
    ax.add_patch(persegi_panjang)

def pencerminan_persegi_panjang(x, y, lebar, tinggi, sumbu):
    if sumbu == 'x':
        return x, -y - tinggi, lebar, tinggi
    elif sumbu == 'y':
        return -x - lebar, y, lebar, tinggi
    elif sumbu == 'origin':
        return -x - lebar, -y - tinggi, lebar, tinggi

x = float(input("Masukkan koordinat x sudut kiri bawah: "))
y = float(input("Masukkan koordinat y sudut kiri bawah: "))
lebar = float(input("Masukkan lebar persegi panjang: "))
tinggi = float(input("Masukkan tinggi persegi panjang: "))
sumbu = input("Masukkan sumbu pencerminan (x, y, atau origin): ").strip().lower()

fig, ax = plt.subplots(figsize=(8, 8))

gambar_persegi_panjang(ax, x, y, lebar, tinggi, label='Persegi Panjang Asli', edgecolor='blue')

x_baru, y_baru, lebar_baru, tinggi_baru = pencerminan_persegi_panjang(x, y, lebar, tinggi, sumbu)
gambar_persegi_panjang(ax, x_baru, y_baru, lebar_baru, tinggi_baru, label='Persegi Panjang Setelah Pencerminan', edgecolor='red')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', adjustable='box')
ax.axhline(0, color='black',linewidth=0.5, ls='--')
ax.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title("Pencerminan Persegi Panjang 2D")
plt.show()