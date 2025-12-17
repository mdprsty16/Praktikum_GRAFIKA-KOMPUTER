import matplotlib.pyplot as plt

def gambar_lingkaran(ax, x, y, radius, label='Lingkaran', edgecolor='blue'):
    lingkaran = plt.Circle((x, y), radius, fill=None, edgecolor=edgecolor, linewidth=2, label=label)
    ax.add_patch(lingkaran)

def pencerminan_lingkaran(x, y, radius, sumbu):
    if sumbu == 'x':
        return x, -y, radius
    elif sumbu == 'y':
        return -x, y, radius
    elif sumbu == 'origin':
        return -x, -y, radius

x = float(input("Masukkan koordinat x pusat lingkaran: "))
y = float(input("Masukkan koordinat y pusat lingkaran: "))
radius = float(input("Masukkan radius lingkaran: "))
sumbu = input("Masukkan sumbu pencerminan (x, y, atau origin): ").strip().lower()

fig, ax = plt.subplots(figsize=(8, 8))

gambar_lingkaran(ax, x, y, radius, label='Lingkaran Asli', edgecolor='blue')

x_baru, y_baru, radius_baru = pencerminan_lingkaran(x, y, radius, sumbu)
gambar_lingkaran(ax, x_baru, y_baru, radius_baru, label='Lingkaran Setelah Pencerminan', edgecolor='red')

ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_aspect('equal', adjustable='box')
ax.axhline(0, color='black', linewidth=0.5, ls='--')
ax.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title("Pencerminan Lingkaran 2D")
plt.show()
