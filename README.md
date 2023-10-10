# Simulation
## VelocityPlotter.py
This program allows one to plot the velocity vector field within a fluid
undergoing Coaxial Couette Flow governed by the Navier-Stokes equations - in
cylindrical polar coordinates $$(r, θ, z)$$. The fluid is free to flow between two
infinitely long cylinders with radii `r1` (for the inner) and `r2` (for the
outer). The outer cylinder remains stationary, whilst the inner cylinder rotates
at `rpm` revolutions per minute, inducing a flow in the fluid.

The number of vectors shown within in the velocity vector field can be altered as
follows: 
- `radial_points` adjusts the number of points in the radial $$r$$ direction.
- `angular_points` adjusts the number of points in the angular $$θ$$ direction.
- `vertical_points` adjusts the number of points in the vertical $$z$$ direction.
