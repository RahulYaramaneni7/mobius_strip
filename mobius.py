import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=200):
        self.R = R            # Radius from center to strip
        self.w = w            # Width of the strip
        self.n = n            # Resolution
        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, self.n),
            np.linspace(-self.w / 2, self.w / 2, self.n)
        )
        self.x, self.y, self.z = self._generate_coordinates()

    def _generate_coordinates(self):
        u = self.u
        v = self.v
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def compute_surface_area(self):
        # Numerical surface area using small patch approximation
        dxu = np.gradient(self.x, axis=0)
        dxv = np.gradient(self.x, axis=1)
        dyu = np.gradient(self.y, axis=0)
        dyv = np.gradient(self.y, axis=1)
        dzu = np.gradient(self.z, axis=0)
        dzv = np.gradient(self.z, axis=1)

        # Cross product of partial derivatives
        cross_x = dyu * dzv - dzu * dyv
        cross_y = dzu * dxv - dxu * dzv
        cross_z = dxu * dyv - dyu * dxv

        dA = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        surface_area = np.sum(dA) * (2 * np.pi / self.n) * (self.w / self.n)
        return surface_area

    def compute_edge_length(self):
        # Compute edge coordinates at v = ±w/2
        u_edge = np.linspace(0, 2 * np.pi, self.n)
        v_edge = self.w / 2
        x_edge = (self.R + v_edge * np.cos(u_edge / 2)) * np.cos(u_edge)
        y_edge = (self.R + v_edge * np.cos(u_edge / 2)) * np.sin(u_edge)
        z_edge = v_edge * np.sin(u_edge / 2)

        # Distance between consecutive edge points
        dx = np.diff(x_edge)
        dy = np.diff(y_edge)
        dz = np.diff(z_edge)
        edge_length = 2 * np.sum(np.sqrt(dx**2 + dy**2 + dz**2))  # Top + bottom edge
        return edge_length

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

if __name__ == "__main__":
    # Example usage
    mobius = MobiusStrip(R=1.0, w=0.4, n=300)
    area = mobius.compute_surface_area()
    edge = mobius.compute_edge_length()

    print(f"Approximate Surface Area: {area:.4f}")
    print(f"Approximate Edge Length: {edge:.4f}")

    mobius.plot()
    
