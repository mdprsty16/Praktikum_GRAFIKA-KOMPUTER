import matplotlib.pyplot as plt 
import matplotlib.patches as patches

fig, ax = plt.subplots()

body_bottom = patches.Rectangle((0, 1), 6, 2, 
edgecolor='blue', facecolor='#87CEEB', linewidth=2)
ax.add_patch(body_bottom)

body_top = patches.Rectangle((1, 2.5), 4, 1, 
edgecolor='blue', facecolor='#87CEEB', linewidth=2)
ax.add_patch(body_top)

wheel_left = patches.Circle((1.5, 0.5), 0.5, 
edgecolor='black', facecolor='gray', linewidth=2)
ax.add_patch(wheel_left)

wheel_right = patches.Circle((4.5, 0.5), 0.5, 
edgecolor='black', facecolor='gray', linewidth=2)
ax.add_patch(wheel_right)

ax.set_xlim(-1, 7)
ax.set_ylim(-1, 4)

plt.grid(True)

ax.set_aspect('equal', adjustable='box')

plt.show()