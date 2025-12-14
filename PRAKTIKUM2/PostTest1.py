import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots()

def gambar_segitiga_merah(panjang_sisi):
    t1 = (0, 0)
    t2 = (panjang_sisi, 0)
    tinggi_segitiga = (panjang_sisi * (np.sqrt(3))) / 2
    t3 = (panjang_sisi / 2, tinggi_segitiga)

    segitiga = patches.Polygon([t1, t2, t3], closed=True, edgecolor='red', facecolor='none', linewidth=2)
    ax.add_patch(segitiga)

    ax.set_xlim(-5, panjang_sisi + 5)
    ax.set_ylim(-5, tinggi_segitiga + 5)

    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

gambar_segitiga_merah(10)
