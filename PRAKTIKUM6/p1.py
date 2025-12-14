import matplotlib.pyplot as plt

def draw_triangle(vertices, title):
    """Fungsi untuk menggambar segitiga berdasarkan titik-titik yang diberikan."""
    # Memecah titik menjadi koordinat x dan y
    x, y = zip(*vertices)

    # Menutup segitiga dengan menambahkan titik pertama ke akhir
    x   += (x[0],)
    y   += (y[0],)

    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')  # Garis horizontal
    plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Garis vertikal
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def scale_triangle(vertices, scale_factor):
    """Melakukan penskalaan segitiga berdasarkan faktor skala."""
    scaled_vertices = [(x * scale_factor, y * scale_factor) for x, y in vertices]
    return scaled_vertices

# Input titik-titik segitiga
print("Masukkan titik-titik segitiga (x1, y1), (x2, y2), (x3, y3):")
x1, y1 = map(float, input("Titik 1 (x1 y1): ").split())
x2, y2 = map(float, input("Titik 2 (x2 y2): ").split())
x3, y3 = map(float, input("Titik 3 (x3 y3): ").split())
triangle_vertices = [(x1, y1), (x2, y2), (x3, y3)]

# Input faktor skala
scale_factor = float(input("Masukkan faktor skala: "))
triangle_vertices = [(x1, y1), (x2, y2), (x3, y3)]

# Menggambar segitiga asli
draw_triangle(triangle_vertices, "Segitiga Asli")

# Melakukan penskalaan
scaled_triangle = scale_triangle(triangle_vertices, scale_factor)

# Menggambar segitiga hasil penskalaan
draw_triangle(scaled_triangle, f"Segitiga Setelah Penskalaan (Skala = {scale_factor})")