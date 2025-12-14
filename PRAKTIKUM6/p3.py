import numpy as np
import matplotlib.pyplot as plt
def draw_circle(center, radius, title):
    """Fungsi untuk menggambar lingkaran berdasarkan pusat dan radius."""
    theta = np.linspace(0, 2 * np.pi, 200)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    plt.figure()
    plt.plot(x, y)
    plt.title(title)
    # Atur batas sumbu agar lingkaran selalu terlihat dengan margin
    margin = 1.2
    xmin = center[0] - radius * margin
    xmax = center[0] + radius * margin
    ymin = center[1] - radius * margin
    ymax = center[1] + radius * margin
    # Pastikan ukuran minimum jendela plotting (untuk kasus radius kecil)
    xmin = min(xmin, -10)
    xmax = max(xmax, 10)
    ymin = min(ymin, -10)
    ymax = max(ymax, 10)
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def scale_circle(radius, scale_factor):
    """Fungsi untuk melakukan penskalaan lingkaran berdasarkan faktor skala yang diberikan."""
    return radius * scale_factor

if __name__ == "__main__":
    try:
        center_x, center_y = map(float, input("Masukkan pusat lingkaran (x y): ").split())
        radius = float(input("Masukkan radius lingkaran: "))
        scale_factor = float(input("Masukkan faktor skala untuk lingkaran: "))
    except Exception as e:
        print("Input tidak valid:", e)
        raise SystemExit(1)

    circle_center = (center_x, center_y)
    # Gambar lingkaran asli
    draw_circle(circle_center, radius, "Lingkaran Asli")
    # Lakukan penskalaan dan gambar hasilnya
    new_radius = scale_circle(radius, scale_factor)
    draw_circle(circle_center, new_radius, f"Lingkaran Setelah Penskalaan (Faktor Skala = {scale_factor})")