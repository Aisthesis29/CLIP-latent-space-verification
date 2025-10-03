import numpy as np
import matplotlib.pyplot as plt

def sph2cart(theta, phi, r=1.0):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

# --- Figure & 3D axis ---
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])

# --- Unit sphere (light) ---
u = np.linspace(0, 2*np.pi, 60)
v = np.linspace(0, np.pi, 30)
X = np.outer(np.cos(u), np.sin(v))
Y = np.outer(np.sin(u), np.sin(v))
Z = np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(X, Y, Z, linewidth=0, alpha=0.15)

# --- XYZ axes ---
lim = 1.2
ax.plot([-lim, lim], [0, 0], [0, 0], color='k')  # X
ax.plot([0, 0], [-lim, lim], [0, 0], color='k')  # Y
ax.plot([0, 0], [0, 0], [-lim, lim], color='k')  # Z
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)

# Optional: hide ticks/cube panes
ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
ax.xaxis.pane.set_visible(False)
ax.yaxis.pane.set_visible(False)
ax.zaxis.pane.set_visible(False)
ax.xaxis._axinfo["grid"]['linewidth'] = 0
ax.yaxis._axinfo["grid"]['linewidth'] = 0
ax.zaxis._axinfo["grid"]['linewidth'] = 0

# --- Random colored dots uniformly on the sphere ---
num_points = 200
u1 = np.random.rand(num_points)
u2 = np.random.rand(num_points)
theta = np.arccos(1 - 2*u1)      # [0, pi], ensures uniform density
phi   = 2*np.pi * u2             # [0, 2pi)

xr, yr, zr = sph2cart(theta, phi, r=1.0)
colors = np.random.rand(num_points, 3)  # random RGB
ax.scatter(xr, yr, zr, c=colors, s=20, alpha=0.9)

plt.show()
