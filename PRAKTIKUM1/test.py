import matplotlib.pyplot as plt

canvas_width = 10
canvas_height = 10

canvas = plt.figure(figsize=(canvas_width, canvas_height))
ax = canvas.add_subplot(111)

ax.axis('off')

x_coords = [3, 7, 5, 3]
y_coords = [3, 3, 7, 3]

ax.plot(x_coords, y_coords, 'b-')

plt.show() 