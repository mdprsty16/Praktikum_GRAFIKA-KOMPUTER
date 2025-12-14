def bresenham_line(x0, y0, x1, y1):
    pixels = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x = x0
    y = y0
    P1 = 2 * dy
    P2 = 2 * dy - 2 * dx
    p = P1 - dx
    pixels.append((x, y))
    for i in range(dx):
        if p < 0:
            x = x + 1
            p = p + P1
        else:
            x = x + 1
            y = y + 1
            p = p + P2
        pixels.append((x, y))
    return pixels

x_start, y_start = 3, 2
x_end, y_end = 10, 5

koordinat_hasil = bresenham_line(x_start, y_start, x_end, y_end)

print(f"Menggambar garis dari ({x_start}, {y_start}) ke ({x_end}, {y_end}):")
print("-" * 50)
print("Koordinat Piksel yang Diperoleh:")
print(koordinat_hasil)
print("-" * 50)
