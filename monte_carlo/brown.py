import math
import random

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

kroki = 1000
dt = 0.1

x = [0.0]
y = [0.0]

for _ in range(1, kroki):
    dx = math.sqrt(dt) * random.gauss(0, 1)
    dy = math.sqrt(dt) * random.gauss(0, 1)

    x.append(x[-1] + dx)
    y.append(y[-1] + dy)

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=1)

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def init():
    line.set_data([], [])
    return line,

def update(t):
    line.set_data(x[:t], y[:t])
    return line,

ani = FuncAnimation(fig, update, frames=kroki, init_func=init, interval=20, blit=True)
plt.show()
