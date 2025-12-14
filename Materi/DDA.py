import matplotlib.pyplot as plt
import numpy as np

try:
    x_a = float(input("Masukkan koordinat x untuk Titik A: "))
    y_a = float(input("Masukkan koordinat y untuk Titik A: "))
    x_b = float(input("Masukkan koordinat x untuk Titik B: "))
    y_b = float(input("Masukkan koordinat y untuk Titik B: "))
except ValueError:
    print("Input tidak valid. Pastikan Anda memasukkan angka.")
    exit()

def bresenham_line(x1, y1, x2, y2):
    
    x_coords = []
    y_coords = []
    
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    is_swapped = False
    if dy > dx:
        dx, dy = dy, dx
        is_swapped = True

    p = 2 * dy - dx
    
    x, y = x1, y1
    
    for i in range(dx + 1):
        x_coords.append(x)
        y_coords.append(y)

        if p >= 0:
            if is_swapped:
                x += sx
            else:
                y += sy
            p -= 2 * dx
        
        if p < 0:
            if is_swapped:
                y += sy
            else:
                x += sx

        p += 2 * dy
        
    return x_coords, y_coords

x_coords, y_coords = bresenham_line(x_a, y_a, x_b, y_b)

print("\nKoordinat titik-titik yang dihitung (Bresenham):")
for x, y in zip(x_coords, y_coords):
    print(f"({x}, {y})")

fig, ax = plt.subplots()

ax.scatter(x_coords, y_coords, color='blue', marker='o', s=50, label='Piksel Bresenham')

ax.plot(x_coords, y_coords, linestyle='-', color='red', linewidth=1, label='Garis Bresenham')

padding = 2
x_min = min(x_a, x_b) - padding
x_max = max(x_a, x_b) + padding
y_min = min(y_a, y_b) - padding
y_max = max(y_a, y_b) + padding

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

ax.set_xlabel("Sumbu X")
ax.set_ylabel("Sumbu Y")
ax.set_title("Algoritma Bresenham untuk Menggambar Garis")
ax.grid(True)
ax.legend()
ax.set_aspect('equal', adjustable='box') 
plt.show()

print("\nFinish task")