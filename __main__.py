import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

angle = 50
velocity = 100
radians = np.deg2rad(angle)
gravity = 9.8
height = 50

time = (velocity * np.sin(radians) + np.sqrt((velocity * np.sin(radians)) ** 2 + 2 * gravity * height)) / gravity
time = np.arange(0, time + 0.1, 0.1)

x = velocity * np.cos(radians) * time
y = height + velocity * np.sin(radians) * time - gravity * time ** 2 / 2

max_height = np.max(y)
max_distance = np.max(x)

fig, ax = plt.subplots()
plt.minorticks_on()

plt.xlabel('distance (m)', color='g')
plt.ylabel('height (m)', color='g', rotation=90)

ax.set_xlim(0, max_distance / 0.95)
ax.set_ylim(0, max_height / 0.95)

line, = ax.plot(0, 0, 'black')
scat = ax.scatter(0, 0, c='g', zorder=np.size(time) + 1)


def animate(i):
    if y[i] == max_height:
        plt.scatter(x[np.where(y == max_height)], max_height, c='r', zorder=np.size(time) + 1)

    if x[i] == max_distance or y[i] < 0:
        plt.scatter(x[i - 1], y[i - 1], c='r', zorder=np.size(time) + 1)
    else:
        scat.set_offsets(np.c_[x[i], y[i]])

    line.set_xdata(x[0:i+1])
    line.set_ydata(y[0:i+1])

    return line,


ani = animation.FuncAnimation(fig, func=animate, frames=np.size(time), interval=1, repeat=False)
# ani.save('animation.gif', writer='imagemagick', fps=30)
plt.show()
