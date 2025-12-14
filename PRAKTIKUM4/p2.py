import matplotlib.pyplot as plt

def midpoint_circle(h, k, r):
    x = 0
    y = r
    points = []
    p = 1 - r

    # add initial symmetric points for (0, r)
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
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x - 2 * y + 1

        # add symmetric points for current (x, y)
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

def main():
    center_x = int(input("Masukkan koordinat x pusat lingkaran: "))
    center_y = int(input("Masukkan koordinat y pusat lingkaran: "))
    radius = int(input("Masukkan nilai radius lingkaran: "))

    circle_points = midpoint_circle(center_x, center_y, radius)

    plt.figure(figsize=(8, 8))
    for point in circle_points:
        plt.plot(point[0], point[1], 'bo')

    plt.title(f"Lingkaran dengan pusat ({center_x}, {center_y}) dan radius {radius}")
    plt.xlim(center_x - radius - 1, center_x + radius + 1)
    plt.ylim(center_y - radius - 1, center_y + radius + 1)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    main()