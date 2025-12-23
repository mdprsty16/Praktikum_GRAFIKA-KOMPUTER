import matplotlib.pyplot as plt
import numpy as np

def plot_segitiga(original_points, sheared_points):
    plt.figure(figsize=(6, 6))
    plt.subplot(1, 2, 1)
    plt.plot(*zip(*original_points, original_points[0]), marker='o')
    plt.title('Segitiga Asli')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(*zip(*sheared_points, sheared_points[0]), marker='o')
    plt.title('Segitiga Setelah Shear')
    plt.grid(True)

    plt.show()

def shear_segitiga(points, shear_x, shear_y):
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
segitiga_points = np.array([[0, 0], [4, 0], [2, 3]])
sheared_points = shear_segitiga(segitiga_points, shear_x, shear_y)
plot_segitiga(segitiga_points, sheared_points)