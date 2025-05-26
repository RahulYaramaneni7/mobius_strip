### 📦 Requirements
**Install the dependencies:**

```
pip install numpy matplotlib
```
### MOBIUS-STRIP
![mobius_strip](https://github.com/user-attachments/assets/2ba8644c-e574-4f55-bd3f-9051fc12d0b3)
**import all the header files**
```
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
```

**Define the MobiusStrip Class**

A Möbius strip in three dimensions is modeled by the MobiusStrip class. After setting the settings for the strip's width, resolution, and radius, it generates a grid of points (u, v) over which it determines the 3D coordinates (x, y, z) that depict the Möbius strip's shape.
```
class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=200):
        self.R = R            
        self.w = w            
        self.n = n           
        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, self.n),
            np.linspace(-self.w / 2, self.w / 2, self.n)
        )
        self.x, self.y, self.z = self._generate_coordinates()
```
**Parametric Equations for Coordinates**

The _generate_coordinates method computes the 3D (x, y, z) points of the Möbius strip using parametric equations based on the grid values u and v.
```
def _generate_coordinates(self):
    u = self.u
    v = self.v
    x = (self.R + v * np.cos(u / 2)) * np.cos(u)
    y = (self.R + v * np.cos(u / 2)) * np.sin(u)
    z = v * np.sin(u / 2)
    return x, y, z
```
**Compute Surface Area**

By numerically approximating partial derivatives, calculating their cross product to identify local area elements, and adding them over the full grid, the compute_surface_area technique determines the surface area of the Möbius strip.
```
def compute_surface_area(self):
    dxu = np.gradient(self.x, axis=0)
    dxv = np.gradient(self.x, axis=1)
    dyu = np.gradient(self.y, axis=0)
    dyv = np.gradient(self.y, axis=1)
    dzu = np.gradient(self.z, axis=0)
    dzv = np.gradient(self.z, axis=1)

    cross_x = dyu * dzv - dzu * dyv
    cross_y = dzu * dxv - dxu * dzv
    cross_z = dxu * dyv - dyu * dxv

    dA = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
    surface_area = np.sum(dA) * (2 * np.pi / self.n) * (self.w / self.n)
    return surface_area
```
**Compute Edge Length**

By calculating the 3D curve coordinates along one boundary, adding up the distances between successive points, and doubling it to include both edges, the compute_edge_length method determines the entire length of the Möbius strip's edge.
```
def compute_edge_length(self):
    u_edge = np.linspace(0, 2 * np.pi, self.n)
    v_edge = self.w / 2
    x_edge = (self.R + v_edge * np.cos(u_edge / 2)) * np.cos(u_edge)
    y_edge = (self.R + v_edge * np.cos(u_edge / 2)) * np.sin(u_edge)
    z_edge = v_edge * np.sin(u_edge / 2)

    dx = np.diff(x_edge)
    dy = np.diff(y_edge)
    dz = np.diff(z_edge)
    edge_length = 2 * np.sum(np.sqrt(dx**2 + dy**2 + dz**2))
    return edge_length
```

**3D Plot of the Möbius Strip**

The plot method visualizes the Möbius strip in 3D using Matplotlib, displaying its surface with color shading and labeled axes.
```
def plot(self):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(self.x, self.y, self.z, rstride=5, cstride=5, cmap='viridis', edgecolor='k', alpha=0.8)
    ax.set_title("Möbius Strip")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.tight_layout()
    plt.show()
```
**call**

```
if __name__ == "__main__":
    mobius = MobiusStrip(R=1.0, w=0.4, n=300)
    area = mobius.compute_surface_area()
    edge = mobius.compute_edge_length()

    print(f"Approximate Surface Area: {area:.4f}")
    print(f"Approximate Edge Length: {edge:.4f}")

    mobius.plot()

```

### Output

![image](https://github.com/user-attachments/assets/4b6f5069-03dc-4f0d-badf-0e85f6e2a7e9)

