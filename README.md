
# Laplace Solver (Miniproyecto 2) — placas paralelas con frontera seleccionable

Resuelve \(\nabla^2 V = 0\) en \([0,8]\times[0,6]\) con dos placas internas:
- Placa 1: y=2, x∈[2,6] a potencial `Vp1`
- Placa 2: y=4, x∈[2,6] a potencial `Vp2`

Método: diferencias finitas 5-puntos + SOR. Placas son **Dirichlet internas**.  
La **frontera externa** puede elegirse:
- `dirichlet0` (por defecto): V=0 en todo el borde
- `neumann` (aislado): \(\partial V/\partial n = 0\) en el borde

Incluye gráficos de V, quiver de E y mapa de |E| (con escala fija opcional).

## Uso rápido
```bash
python -m venv .venv && . .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Ejecutar como módulo (recomendado)
python -m src.main --vp1 6 --vp2 -6 --boundary dirichlet0 --field-vmax 6
```
Archivos de salida:
- `figures/potential.png`
- `figures/field_quiver.png`
- `figures/field_magnitude.png`
- `outputs/solution.npz`

## Opciones CLI
```
--nx, --ny          # nodos en x,y (incluyendo bordes); default 161x121
--vp1, --vp2        # potencial de las placas (default +6 y -6)
--boundary          # dirichlet0 | neumann  (default dirichlet0)
--tol, --max-iter, --omega
--field-vmax        # tope de color para |E| (default 6)
```
## Notas técnicas
- Las placas ahora son robustas: se fijan en la **fila más cercana** a y=2 y y=4, así no dependes de que la malla caiga exactamente sobre esas coordenadas.
- `neumann` se impone copiando el valor del nodo interior adyacente en cada borde (\(\partial V/\partial n=0\)).
- \(\omega\) se estima como \(2/(1+\sin(\pi/\max(n_x,n_y)))\) si no lo pasas.
