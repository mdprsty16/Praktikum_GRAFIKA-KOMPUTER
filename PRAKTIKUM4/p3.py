import matplotlib.pyplot as plt

def plot_circle(x_center, y_center, x, y):
    plt.plot(x_center + x, y_center + y, 'ro')
    plt.plot(x_center - x, y_center + y, 'ro')
    plt.plot(x_center + x, y_center - y, 'ro')          
    plt.plot(x_center - x, y_center - y, 'ro')
    plt.plot(x_center + y, y_center + x, 'ro')
    plt.plot(x_center - y, y_center + x, 'ro')
    plt.plot(x_center + y, y_center - x, 'ro')
    plt.plot(x_center - y, y_center - x, 'ro')
def bresenham_circle(x_center, y_center, radius):
    x = 0 
    y = radius
    d = 3 - 2 * radius

    plot_circle(x_center, y_center, x, y)

    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        plot_circle(x_center, y_center, x, y)

# Input from user
center_x = int(input("Masukkan koordinat x pusat lingkaran (x_center): "))
center_y = int(input("Masukkan koordinat y pusat lingkaran (y_center): "))
radius = int(input("Masukkan nilai radius lingkaran (radius): "))

bresenham_circle(center_x, center_y, radius)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()