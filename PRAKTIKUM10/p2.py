# Import library
import numpy as np
import matplotlib.pyplot as plt

# Fungsi membuat limas
def create_pyramid(base_length, height):
    base = np.array([
        [0, 0, 0],
        [base_length, 0, 0],
        [base_length, base_length, 0],
        [0, base_length, 0],
        [0, 0, 0]  # menutup alas
    ])

    apex = np.array([base_length/2, base_length/2, height])
    return base, apex

# Fungsi penskalaan
def scale_object(points, sx, sy, sz):
    scale_matrix = np.array([sx, sy, sz])
    return points * scale_matrix

# Parameter objek
base_length = 4
height = 4

# Input skala
sx = float(input("Masukkan skala X: "))
sy = float(input("Masukkan skala Y: "))
sz = float(input("Masukkan skala Z: "))

# Membuat objek
base, apex = create_pyramid(base_length, height)

# Skala objek
scaled_base = scale_object(base, sx, sy, sz)
scaled_apex = scale_object(apex, sx, sy, sz)

# Visualisasi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Limas asli (garis)
ax.plot(base[:,0], base[:,1], base[:,2], color='blue')
for i in range(4):
    ax.plot(
        [base[i,0], apex[0]],
        [base[i,1], apex[1]],
        [base[i,2], apex[2]],
        color='blue'
    )

# Limas hasil skala (garis)
ax.plot(scaled_base[:,0], scaled_base[:,1], scaled_base[:,2], color='red')
for i in range(4):
    ax.plot(
        [scaled_base[i,0], scaled_apex[0]],
        [scaled_base[i,1], scaled_apex[1]],
        [scaled_base[i,2], scaled_apex[2]],
        color='red'
    )

# Label
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Penskalaan 3D Limas (Wireframe / Garis)')

plt.show()
