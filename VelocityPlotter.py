import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

# function to be plotted
def v(r, r1, r2, omega):
    dist = r2**2 - r1**2
    a = (-1 * omega * r1**2) / dist
    b = (omega * r1**2 * r2**2)/dist
    return a*r + b/r

# convert from RPM to rad/s
def convertFromRPM(rpm):
    return rpm*0.104719755

# define parameters
# revs per min
rpm = 10
# inner radius
r1 = 3.775/100 # in metres
# outer radius
r2 = 6.95/100 # in metres

# plot
# Define the cylindrical polar coordinates
radial_points = 10
angular_points = 20
vertical_points = 1
r = np.linspace(r1, r2, radial_points)
theta = np.linspace(0, 2 * np.pi, angular_points)
z = np.linspace(0, 0.1, vertical_points)

# Create a meshgrid of the cylindrical polar coordinates
R, Theta, Z = np.meshgrid(r, theta, z)

# Define the vector field in cylindrical polar coordinates
Vr = 0
Vtheta = v(R,r1,r2,convertFromRPM(rpm))
Vz = 0

# Convert the cylindrical polar coordinates to Cartesian coordinates
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Convert Vtheta to cartesian
vec_X = -np.sin(Theta)*Vtheta
vec_Y = np.cos(Theta)*Vtheta
vec_Z = 0

# Create a 3D plot of the vector field
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, vec_X, vec_Y, vec_Z, length = 0.3, normalize = False)
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('z (m)')
plt.show()
