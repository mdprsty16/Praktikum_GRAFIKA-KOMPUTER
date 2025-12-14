import matplotlib.pyplot as plt  # impor modul matplotlib untuk menggambar grafik

def draw_square(vertices, title):
    # fungsi untuk menggambar persegi berdasarkan daftar koordinat vertices
    x, y = zip(*vertices)  # pisahkan koordinat x dan y dari daftar tupel vertices
    x += (x[0],)  # tambahkan titik pertama di akhir agar garis tertutup (kembali ke awal)
    y += (y[0],)  # tambahkan titik pertama di akhir agar garis tertutup (kembali ke awal)

    plt.figure()  # buat figure baru untuk gambar
    plt.plot(x, y, marker='o')  # gambar garis yang menghubungkan titik-titik dan tandai setiap titik
    plt.title(title)  # beri judul pada grafik
    plt.xlim(-10, 10)  # atur batas sumbu-x agar konsisten
    plt.ylim(-10, 10)  # atur batas sumbu-y agar konsisten
    plt.axhline(0, color='black', linewidth=0.5, ls='--')  # gambar garis horizontal sumbu-x
    plt.axvline(0, color='black', linewidth=0.5, ls='--')  # gambar garis vertikal sumbu-y
    plt.grid()  # tampilkan grid pada plot
    plt.gca().set_aspect('equal', adjustable='box')  # pastikan skala x dan y sama (persegi tidak terdistorsi)
    plt.show()  # tampilkan jendela plot

def scale_square(vertices, scale_factor):
    # fungsi untuk mengskalakan setiap titik berdasarkan faktor skala
    scaled_vertices = [(x * scale_factor, y * scale_factor) for x, y in vertices]
    # kembalikan daftar koordinat baru setelah dikalikan dengan faktor skala
    return scaled_vertices

print("Masukkan titik-titik persegi (x1 y1), (x2 y2), (x3 y3), (x4 y4):")
# minta input titik 1, ubah ke float dan pisahkan menjadi x1, y1
x1, y1 = map(float, input("Titik 1: ").split())
# minta input titik 2, ubah ke float dan pisahkan menjadi x2, y2
x2, y2 = map(float, input("Titik 2: ").split())
# minta input titik 3, ubah ke float dan pisahkan menjadi x3, y3
x3, y3 = map(float, input("Titik 3: ").split())
# minta input titik 4, ubah ke float dan pisahkan menjadi x4, y4
x4, y4 = map(float, input("Titik 4: ").split())

# gabungkan ke dalam daftar vertices sesuai urutan
square_vertices = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
# minta input faktor skala dan ubah menjadi float
scale_factor = float(input("Masukkan faktor skala: "))

# gambar persegi asli sebelum penskalaan
draw_square(square_vertices, "Persegi Asli")

# hitung koordinat setelah penskalaan
scaled_square_vertices = scale_square(square_vertices, scale_factor)
# gambar persegi setelah penskalaan dengan judul yang mencantumkan faktor skala
draw_square(scaled_square_vertices, f"Persegi Setelah Penskalaan (Faktor Skala = {scale_factor})")