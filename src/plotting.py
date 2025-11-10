
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def _ensure_dir(outdir):
    Path(outdir).mkdir(parents=True, exist_ok=True)

def plot_potential(x, y, V, outdir='figures', fname='potential.png',
                   cmap='viridis', levels=60, contour_levels=30, draw_plates=True):
    _ensure_dir(outdir)
    X, Y = np.meshgrid(x, y, indexing='xy')
    plt.figure(figsize=(8,5))
    cp = plt.contourf(X, Y, V, levels=levels, cmap=cmap)
    plt.colorbar(cp, label='V')
    cs = plt.contour(X, Y, V, colors='k', linewidths=0.6, levels=contour_levels)
    plt.clabel(cs, inline=True, fontsize=7, fmt='%.2f')
    if draw_plates:
        for yplate in [2.0, 4.0]:
            plt.plot([2.0, 6.0], [yplate, yplate], 'k-', lw=1.5)
    plt.xlabel('x'); plt.ylabel('y'); plt.title('Potential V(x,y)')
    outpath = Path(outdir)/fname
    plt.tight_layout(); plt.savefig(outpath, dpi=200); plt.close()
    return str(outpath)

def plot_field_quiver(x, y, Ex, Ey, stride=4, outdir='figures', fname='field_quiver.png'):
    _ensure_dir(outdir)
    X, Y = np.meshgrid(x, y, indexing='xy')
    plt.figure(figsize=(8,5))
    plt.quiver(X[::stride, ::stride], Y[::stride, ::stride],
               Ex[::stride, ::stride], Ey[::stride, ::stride], scale=50)
    for yplate in [2.0, 4.0]:
        plt.plot([2.0, 6.0], [yplate, yplate], 'k-', lw=1.5)
    plt.xlabel('x'); plt.ylabel('y'); plt.title('Electric Field E = -∇V')
    outpath = Path(outdir)/fname
    plt.tight_layout(); plt.savefig(outpath, dpi=200); plt.close()
    return str(outpath)

def plot_field_magnitude(x, y, Ex, Ey, outdir='figures', fname='field_magnitude.png',
                         vmax=None, cmap='coolwarm'):
    _ensure_dir(outdir)
    X, Y = np.meshgrid(x, y, indexing='xy')
    Emag = np.hypot(Ex, Ey)
    plt.figure(figsize=(8,5))
    cp = plt.contourf(X, Y, Emag, levels=60, cmap=cmap, vmin=0.0, vmax=vmax)
    plt.colorbar(cp, label='|E|')
    for yplate in [2.0, 4.0]:
        plt.plot([2.0, 6.0], [yplate, yplate], 'k-', lw=1.5)
    plt.xlabel('x'); plt.ylabel('y'); plt.title('Field magnitude |E(x,y)|')
    outpath = Path(outdir)/fname
    plt.tight_layout(); plt.savefig(outpath, dpi=200); plt.close()
    return str(outpath), Emag.max()
