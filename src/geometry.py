
import numpy as np

def make_grid(nx: int, ny: int, Lx: float = 8.0, Ly: float = 6.0):
    x = np.linspace(0.0, Lx, nx)
    y = np.linspace(0.0, Ly, ny)
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    return x, y, dx, dy

def plate_masks(x, y, x1=2.0, x2=6.0, y1=2.0, y2=4.0):
    """Placas robustas: se fijan en la fila más cercana a y1 y y2."""
    X, Y = np.meshgrid(x, y, indexing='xy')
    j1 = int(np.argmin(np.abs(y - y1)))
    j2 = int(np.argmin(np.abs(y - y2)))
    in_x = (X[0,:] >= x1) & (X[0,:] <= x2)  # sobre columnas
    m1 = np.zeros_like(X, dtype=bool); m1[j1, in_x] = True
    m2 = np.zeros_like(X, dtype=bool); m2[j2, in_x] = True
    return m1, m2

def boundary_mask(nx, ny):
    bd = np.zeros((ny, nx), dtype=bool)
    bd[0, :]=True; bd[-1,:]=True; bd[:,0]=True; bd[:,-1]=True
    return bd
