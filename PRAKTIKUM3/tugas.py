import matplotlib.pyplot as plt

def dda_algorithm(x0, y0, x1, y1):
    x, y = x0, y0
    dx = x1 - x0
    dy = y1 - y0
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    # handle the case where start and end are the same point
    if steps == 0:
        plt.plot([round(x)], [round(y)], marker="o", color="b")
        return
    x_inc = dx / steps
    y_inc = dy / steps
    x_points = [round(x)]
    y_points = [round(y)]
    for _ in range(int(steps)):
        x += x_inc
        y += y_inc
        x_points.append(round(x))
        y_points.append(round(y))
    plt.plot(x_points, y_points, marker="o", color="b")

def draw_house():
    plt.figure(figsize=(6, 6))
    dda_algorithm(2, 2, 2, 6)
    dda_algorithm(2, 6, 6, 6)
    dda_algorithm(6, 6, 6, 2)
    dda_algorithm(6, 2, 2, 2)
    dda_algorithm(2, 6, 4, 8)
    dda_algorithm(4, 8, 6, 6)
    dda_algorithm(2, 4, 3, 4)
    dda_algorithm(3, 2, 3, 4)
    dda_algorithm(3, 4, 4, 4)
    dda_algorithm(4, 4, 4, 2)
    dda_algorithm(2, 5, 3, 5)
    dda_algorithm(3, 5, 3, 4)
    dda_algorithm(5, 4, 5, 5)
    dda_algorithm(5, 5, 6, 5)
    dda_algorithm(6, 5, 6, 4)
    dda_algorithm(6, 4, 5, 4)
    plt.title("Gambar Rumah dengan Algoritma DDA")
    plt.xlim(0, 8)
    plt.ylim(0, 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

draw_house()