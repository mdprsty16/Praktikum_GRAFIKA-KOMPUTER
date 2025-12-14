import matplotlib.pyplot as plt

def midpoint_circle(h, k, r):
    x = 0
    y = r
    p = 5/4 - r   # ini rumus midpoint yang benar
    points = []

    # titik awal
    points.extend([
        (h + x, k + y),
        (h - x, k + y),
        (h + x, k - y),
        (h - x, k - y),
        (h + y, k + x),
        (h - y, k + x),
        (h + y, k - x),
        (h - y, k - x),
    ])

    while x < y:
        x += 1
        if p < 0:
            p = p + 2*x + 3
        else:
            y -= 1
            p = p + 2*(x - y) + 5

        points.extend([
            (h + x, k + y),
            (h - x, k + y),
            (h + x, k - y),
            (h - x, k - y),
            (h + y, k + x),
            (h - y, k + x),
            (h + y, k - x),
            (h - y, k - x),
        ])

    return points


center_x = 0
center_y = 0
radius = 10

circle_points = midpoint_circle(center_x, center_y, radius)

plt.figure(figsize=(8,8))
for point in circle_points:
    plt.plot(point[0], point[1], 'ko')

plt.title("Lingkaran (Algoritma Midpoint Circle sesuai buku)")
plt.xlim(-radius-2, radius+2)
plt.ylim(-radius-2, radius+2)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
