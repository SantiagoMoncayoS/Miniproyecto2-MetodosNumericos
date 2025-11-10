
import numpy as np

def sor_laplace(nx:int, ny:int, Lx:float, Ly:float, vp1:float, vp2:float,
                x1=2.0, x2=6.0, y1=2.0, y2=4.0, tol=1e-6, max_iter=20000, omega=None,
                boundary='dirichlet0', return_history=False):
    from .geometry import make_grid, plate_masks, boundary_mask
    x, y, dx, dy = make_grid(nx, ny, Lx, Ly)
    ax = 1.0/(dx*dx); ay = 1.0/(dy*dy); denom = 2.0*(ax+ay)

    V = np.zeros((ny, nx), dtype=float)

    bd = boundary_mask(nx, ny)
    m1, m2 = plate_masks(x, y, x1, x2, y1, y2)
    fixed = m1 | m2

    # set plates
    V[m1] = vp1; V[m2] = vp2

    if omega is None:
        nmax = max(nx, ny)
        omega = 2.0/(1.0 + np.sin(np.pi/nmax))

    history = []
    for it in range(1, max_iter+1):
        max_update = 0.0

        # Gauss-Seidel SOR interior points
        for j in range(1, ny-1):
            jm1, jp1 = j-1, j+1
            for i in range(1, nx-1):
                if fixed[j, i]:  # skip plates
                    continue
                im1, ip1 = i-1, i+1
                V_old = V[j, i]
                rhs = ax*(V[j, ip1] + V[j, im1]) + ay*(V[jp1, i] + V[jm1, i])
                V_new = (1.0 - omega)*V_old + omega*(rhs/denom)
                upd = abs(V_new - V_old)
                if upd > max_update: max_update = upd
                V[j, i] = V_new

        # Enforce boundaries/plates after each sweep
        # Plates (Dirichlet internas)
        V[m1] = vp1; V[m2] = vp2

        if boundary == 'dirichlet0':
            V[bd] = 0.0
        elif boundary == 'neumann':
            # Zero normal derivative: copy interior neighbor to boundary
            V[0, :]  = V[1, :]      # bottom
            V[-1, :] = V[-2, :]     # top
            V[:, 0]  = V[:, 1]      # left
            V[:, -1] = V[:, -2]     # right
        else:
            raise ValueError("boundary must be 'dirichlet0' or 'neumann'")

        history.append(max_update)
        if max_update < tol: break

    info = {"iterations": it, "converged": max_update < tol, "omega": omega, "final_update": max_update, "dx": dx, "dy": dy, "boundary": boundary}
    if return_history: info["history"] = np.array(history, dtype=float)
    return x, y, V, (bd, m1, m2), info

def electric_field(x, y, V):
    dx = x[1]-x[0]; dy = y[1]-y[0]
    dVdx = np.gradient(V, dx, axis=1)
    dVdy = np.gradient(V, dy, axis=0)
    Ex = -dVdx; Ey = -dVdy
    return Ex, Ey
