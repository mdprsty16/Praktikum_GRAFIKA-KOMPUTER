import matplotlib.pyplot as plt 
import matplotlib.patches as patches

fig, ax = plt.subplots()

def gambar_dua_persegi_panjang():
    
    lebar_pp1 = 100
    tinggi_pp1 = 50
    
    lebar_pp2 = 70  
    tinggi_pp2 = 40 

    pp1 = patches.Rectangle((0, 0), lebar_pp1, tinggi_pp1, 
    edgecolor='blue', facecolor='lightblue', linewidth=2)
    ax.add_patch(pp1)

    pp2 = patches.Rectangle((lebar_pp1, 0), lebar_pp2, tinggi_pp2, 
    edgecolor='red', facecolor='lightcoral', linewidth=2)
    ax.add_patch(pp2)
    
    total_lebar = lebar_pp1 + lebar_pp2
    max_tinggi = max(tinggi_pp1, tinggi_pp2) 

    ax.set_xlim(-10, total_lebar + 10)
    ax.set_ylim(-10, max_tinggi + 10)

    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

gambar_dua_persegi_panjang()