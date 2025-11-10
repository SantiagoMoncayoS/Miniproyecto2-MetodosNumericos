
import argparse
import numpy as np
from pathlib import Path
from .solver import sor_laplace, electric_field
from .plotting import plot_potential, plot_field_quiver, plot_field_magnitude

def main():
    p = argparse.ArgumentParser(description='Laplace solver for a parallel-plate capacitor in a rectangle.')
    p.add_argument('--nx', type=int, default=161)
    p.add_argument('--ny', type=int, default=121)
    p.add_argument('--Lx', type=float, default=8.0)
    p.add_argument('--Ly', type=float, default=6.0)
    p.add_argument('--vp1', type=float, default=6.0)
    p.add_argument('--vp2', type=float, default=-6.0)
    p.add_argument('--boundary', type=str, default='dirichlet0', choices=['dirichlet0','neumann'])
    p.add_argument('--tol', type=float, default=1e-6)
    p.add_argument('--max-iter', type=int, default=50000)
    p.add_argument('--omega', type=float, default=None)
    p.add_argument('--save-prefix', type=str, default='solution')
    p.add_argument('--field-vmax', type=float, default=6.0)
    args = p.parse_args()

    x, y, V, masks, info = sor_laplace(
        nx=args.nx, ny=args.ny, Lx=args.Lx, Ly=args.Ly,
        vp1=args.vp1, vp2=args.vp2,
        tol=args.tol, max_iter=args.max_iter, omega=args.omega,
        boundary=args.boundary
    )
    Ex, Ey = electric_field(x, y, V)

    outdir = Path('outputs'); outdir.mkdir(exist_ok=True, parents=True)
    np.savez(outdir/f'{args.save_prefix}.npz', x=x, y=y, V=V, Ex=Ex, Ey=Ey, info=info)

    plot_potential(x, y, V, outdir='figures', fname='potential.png', cmap='viridis', contour_levels=30)
    plot_field_quiver(x, y, Ex, Ey, stride=max(1, int(min(args.ny, args.nx)/40)), outdir='figures', fname='field_quiver.png')
    mag_path, emax = plot_field_magnitude(x, y, Ex, Ey, outdir='figures', fname='field_magnitude.png',
                                          vmax=args.field_vmax, cmap='coolwarm')

    print('Iterations:', info['iterations'])
    print('Converged:', info['converged'])
    print('omega:', info['omega'])
    print('final max update:', info['final_update'])
    print('Boundary:', info['boundary'])
    print('Max |E| (computed):', emax)
    print('Saved |E| plot with vmax =', args.field_vmax, 'at', mag_path)

if __name__ == '__main__':
    main()
