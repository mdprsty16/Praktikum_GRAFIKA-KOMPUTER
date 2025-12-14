import matplotlib.pyplot as plt

def midpoint_circle(h, k, r):
    x = 0
    y = r
    points = []

    p = 1 - r
    while x <= y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x - 2 * y + 1

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

plt.figure(figsize=(8, 8))
for point in circle_points:
    plt.plot(point[0], point[1], 'bo')

plt.title("Lingkaran menggunakan Algoritma Midpoint Circle")
plt.xlim(-radius-1, radius+1)
plt.ylim(-radius-1, radius+1)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()