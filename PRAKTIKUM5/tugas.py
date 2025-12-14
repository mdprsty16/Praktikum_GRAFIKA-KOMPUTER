import matplotlib.pyplot as plt
import numpy as np

# Definisi Vertices (Titik Sudut)
vertices_x = [10, 40, 60, 30, 10]
vertices_y = [10, 10, 30, 30, 10]

# Garis Pembatas (garis tengah horizontal pada y=20)
mid_y = 20
xs_intersect = []
verts = list(zip(vertices_x, vertices_y))
for i in range(len(verts) - 1):
	x1, y1 = verts[i]
	x2, y2 = verts[i+1]
	if (y1 - mid_y) * (y2 - mid_y) <= 0 and (y1 != y2):
		t = (mid_y - y1) / (y2 - y1)
		xi = x1 + t * (x2 - x1)
		xs_intersect.append(xi)

xs_intersect = sorted(xs_intersect)
if len(xs_intersect) >= 2:
	dividing_line_x = [xs_intersect[0], xs_intersect[-1]]
	dividing_line_y = [mid_y, mid_y]
else:
	dividing_line_x = [10, 50]
	dividing_line_y = [mid_y, mid_y]

# Pembuatan Plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(vertices_x, vertices_y, color='black', linewidth=2)
ax.plot(dividing_line_x, dividing_line_y, color='black', linewidth=1.5)

# Pengaturan Grid dan Sumbu
ax.set_xticks(np.arange(0, 61, 10))
ax.set_yticks(np.arange(0, 31, 5))
ax.grid(True, linestyle='-', alpha=0.6)
ax.set_xlim(0, 60)
ax.set_ylim(0, 30)
ax.set_aspect('equal', adjustable='box')

# Judul Plot
ax.set_title('Translasi Jajargenjang', fontsize=14)
plt.tight_layout()
plt.show()
