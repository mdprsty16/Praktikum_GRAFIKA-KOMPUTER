import matplotlib.pyplot as plt
import numpy as np

def plot_belah_ketupat(original_points, sheared_points):
    plt.figure(figsize=(6, 6))
    plt.subplot(1, 2, 1)
    plt.plot(*zip(*original_points, original_points[0]), marker='o')
    plt.title('Belah Ketupat Asli')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(*zip(*sheared_points, sheared_points[0]), marker='o')
    plt.title('Belah Ketupat Setelah Geser')
    plt.grid(True)

    plt.show()

def shear_belah_ketupat(points, shear_x, shear_y):
    shear_matrix = np.array([[1, shear_x],
                             [shear_y, 1]])

    sheared_points = []
    for point in points:
        new_point = np.dot(shear_matrix, point)
        sheared_points.append(new_point)
    return sheared_points

print("Masukan faktor shear horizontal (shear_x): ")
shear_x = float(input())
print("Masukan faktor shear vertikal (shear_y): ")
shear_y = float(input())

belah_ketupat_points = np.array([[0, 2], [2, 0], [0, -2], [-2, 0]])

sheared_points = shear_belah_ketupat(belah_ketupat_points, shear_x, shear_y)
plot_belah_ketupat(belah_ketupat_points, sheared_points)