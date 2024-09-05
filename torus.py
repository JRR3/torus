import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use("agg")

Tfinal = 20
n_points = 1000
t_vec = np.linspace(0,Tfinal,n_points)
Rmax = 5
Rmin = 1
fmin = 1

rot_angle = np.linspace(0, 2 * np.pi , n_points)
c = np.cos(rot_angle)
s = np.sin(rot_angle)
m = np.zeros((n_points,3,3))
m[:,0,0] = c
m[:,0,1] = -s
m[:,1,0] = s
m[:,1,1] = c
m[:,2,2] = 1

xp = Rmax + Rmin * np.cos(2*np.pi*fmin*t_vec)
yp = xp * 0
zp = 0    + Rmin * np.sin(2*np.pi*fmin*t_vec)

c_vec = np.vstack((xp,yp,zp)).T
out_vec = 0 * c_vec

for k, (mat,vec) in enumerate(zip(m,c_vec)):
    out_vec[k] = mat @ vec

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(out_vec[:,0],out_vec[:,1],out_vec[:,2])

# ax.set_aspect("equal")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

fname = "torus.pdf"
fig.savefig(fname)
