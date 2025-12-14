import numpy as np
import matplotlib.pyplot as plt

def draw_circle(center, radius, title):
    """Fungsi untuk menggambar lingkaran berdasarkan pusat dan radius."""
    theta = np.linspace(0, 2 * np.pi, 100)      # Membuat sudut dari 0 hingga 2π
    x = center[0] + radius * np.cos(theta)      # Menghitung koordinat x
    y = center[1] + radius * np.sin(theta)      # Menghitung koordinat y

    plt.plot(x, y)                               # Menggambar lingkaran
    plt.title(title)
    plt.xlim(-10, 10)                            # Mengatur batas sumbu x
    plt.ylim(-10, 10)                            # Mengatur batas sumbu y
    plt.axhline(0, color='black', linewidth=0.5, ls='--')  # Garis horizontal di sumbu x
    plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Garis vertikal di sumbu y
    plt.grid(True)                               # Menampilkan grid
    plt.gca().set_aspect('equal', adjustable='box') # Skala sama pada x dan y

def draw_rectangle(bottom_left, width, height, title):
    """Fungsi untuk menggambar persegi panjang berdasarkan titik kiri bawah, lebar, dan tinggi."""
    x = [bottom_left[0], bottom_left[0] + width, bottom_left[0] + width, bottom_left[0], bottom_left[0]]
    y = [bottom_left[1], bottom_left[1], bottom_left[1] + height, bottom_left[1] + height, bottom_left[1]]

    plt.plot(x, y)                               # Menggambar persegi panjang
    plt.title(title)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')

def scale_circle(center, radius, scale_factor):
    """Fungsi untuk melakukan penskalaan lingkaran berdasarkan faktor skala yang diberikan."""
    new_radius = radius * scale_factor
    return new_radius

def scale_rectangle(bottom_left, width, height, scale_factor):
    """Fungsi untuk melakukan penskalaan persegi panjang berdasarkan faktor skala."""
    new_width = width * scale_factor
    new_height = height * scale_factor
    return new_width, new_height

# INPUT DATA
circle_center_x, circle_center_y = map(float, input("Masukkan pusat lingkaran (x y): ").split())
circle_radius = float(input("Masukkan radius lingkaran: "))
scale_factor_circle = float(input("Masukkan faktor skala untuk lingkaran: "))

rect_bottom_left_x, rect_bottom_left_y = map(float, input("Masukkan titik kiri bawah persegi panjang (x y): ").split())
rect_width = float(input("Masukkan lebar persegi panjang: "))
rect_height = float(input("Masukkan tinggi persegi panjang: "))
scale_factor_rectangle = float(input("Masukkan faktor skala untuk persegi panjang: "))
circle_center = (circle_center_x, circle_center_y)
rect_bottom_left = (rect_bottom_left_x, rect_bottom_left_y)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
draw_circle(circle_center, circle_radius, "Lingkaran Asli")

# HASIL PENSKALAAN
new_circle_radius = scale_circle(circle_center, circle_radius, scale_factor_circle)
draw_circle(circle_center, new_circle_radius, f"Lingkaran Setelah Penskalaan (Faktor Skala: {scale_factor_circle})")    

plt.subplot(1, 2, 2)
draw_rectangle(rect_bottom_left, rect_width, rect_height, "Persegi Panjang Asli")

new_width, new_height = scale_rectangle(rect_bottom_left, rect_width, rect_height, scale_factor_rectangle)
draw_rectangle(rect_bottom_left, new_width, new_height, f"Persegi Panjang Setelah Penskalaan (Faktor Skala: {scale_factor_rectangle})")

plt.tight_layout()
plt.show()