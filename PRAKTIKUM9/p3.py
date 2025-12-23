import matplotlib.pyplot as plt
import numpy as np

def plot_lingkaran(original_points, sheared_points):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(original_points[0], original_points[1], label='Lingkaran Asli')
    plt.title('Lingkaran Asli')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(sheared_points[0], sheared_points[1], label='Lingkaran Setelah Shear')
    plt.title('Lingkaran Setelah Shear')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)

    plt.show()

def shear_lingkaran(points, shear_x, shear_y):
    shear_matrix = np.array([[1, shear_x],
                             [shear_y, 1]])

    sheared_points = np.dot(shear_matrix, points)
    return sheared_points

print("Masukan faktor shear horizontal (shear_x): ")
shear_x = float(input())
print("Masukan faktor shear vertikal (shear_y): ")
shear_y = float(input())

theta = np.linspace(0, 2 * np.pi, 100)
radius = 5
x = radius * np.cos(theta)
y = radius * np.sin(theta)

lingkaran_points = np.array([x, y])
sheared_points = shear_lingkaran(lingkaran_points, shear_x, shear_y)
plot_lingkaran(lingkaran_points, sheared_points)