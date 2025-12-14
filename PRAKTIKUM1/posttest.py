import matplotlib.pyplot as plt

x_kiri = [1] * 30
y_kiri = [i * 0.1 + 1 for i in range(30)]

x_kanan = [6] * 30
y_kanan = [i * 0.1 + 1 for i in range(30)]

x_atas = [i * 0.1 + 1 for i in range(50)]
y_atas = [4] * 50

x_bawah = [i * 0.1 + 1 for i in range(50)]
y_bawah = [1] * 50

plt.scatter(x_kiri, y_kiri, color='red', s=10)   
plt.scatter(x_kanan, y_kanan, color='green', s=10)
plt.scatter(x_atas, y_atas, color='blue', s=10)
plt.scatter(x_bawah, y_bawah, color='orange', s=10)

plt.axis('off')       
plt.axis("equal")     

plt.show()
