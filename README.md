
# Miniproyecto 2 – Métodos Numéricos para Ecuaciones en Derivadas Parciales

Repositorio de entrega del **Miniproyecto 2** para la materia *Métodos Numéricos para Ecuaciones en Derivadas Parciales* (2025-2).  
Profesor: **José Hernán Ortiz Ocampo**

---

## 📄 Descripción general

Este proyecto implementa la **solución numérica de la ecuación de Laplace 2D**  
∇²V = 0
en un dominio rectangular con **dos placas internas** y frontera externa **Dirichlet o Neumann**.  
El método numérico empleado es **diferencias finitas en 5 puntos** con **relajación sucesiva (SOR)**.

El trabajo incluye:
- Visualización de las **líneas equipotenciales** y el **campo eléctrico**.
- Comparación entre condiciones de frontera **Dirichlet homogénea** (V = 0) y **Neumann** (∂V/∂n = 0).
- Cálculo y graficación del **módulo del campo eléctrico** |E| = sqrt(Ex² + Ey²)
.
- Implementación de una **interfaz por línea de comandos (CLI)** para personalizar los parámetros.

---

## 📂 Contenido del repositorio

- `src/` → Código fuente principal del proyecto  
  - `main.py` → Script principal ejecutable con opciones CLI (`--vp1`, `--vp2`, `--boundary`, etc.).  
  - `solver.py` → Implementación del método SOR y cálculo del campo eléctrico.  
  - `geometry.py` → Generación de la malla y definición de las máscaras de placas y fronteras.  
  - `plotting.py` → Rutinas de graficación de potencial, campo y módulo del campo.  

- `tests/` → Pruebas unitarias básicas para verificar la generación de máscaras.  

- `figures/` → Carpeta donde se guardan automáticamente las figuras generadas:  
  - `potential.png` → Mapa de potencial \(V(x,y)\).  
  - `field_quiver.png` → Diagrama de vectores del campo \(E = -\nabla V\).  
  - `field_magnitude.png` → Mapa de magnitud \(|E|\).  

- `outputs/` → Archivos `.npz` con los datos numéricos de cada simulación (`x`, `y`, `V`, `Ex`, `Ey`, `info`).  

- `requirements.txt` → Dependencias necesarias (`numpy`, `matplotlib`).  

- `LICENSE`, `.gitignore`, `README.md` → Metadatos y documentación del proyecto.  

---

## ⚙️ Configuración del entorno de ejecución

Se recomienda **Python 3.10 o superior**.

### 🔹 Opción A – Manual por terminal (Windows)
```bash
python -m venv env1
.\env1\Scripts\activate
pip install -r requirements.txt
python -m src.main --vp1 6 --vp2 -6 --boundary dirichlet0 --field-vmax 6
```

### 🔹 Opción B – Linux/Mac
```bash
python3 -m venv env1
source env1/bin/activate
pip install -r requirements.txt
python -m src.main --vp1 6 --vp2 -6 --boundary dirichlet0 --field-vmax 6
```

---

## 🧮 Ejemplos de ejecución

### 1️⃣ Caso base – Frontera Dirichlet (V = 0)
```bash
python -m src.main --vp1 6 --vp2 -6 --boundary dirichlet0 --field-vmax 6
```

### 2️⃣ Frontera aislada – Condición Neumann
```bash
python -m src.main --vp1 6 --vp2 -6 --boundary neumann --field-vmax 6
```

### 3️⃣ Exploración de ω y tolerancia
```bash
python -m src.main --omega 1.9 --tol 1e-7 --nx 201 --ny 151
```

---

## 📊 Resultados esperados

- Campos equipotenciales simétricos entre las placas (y = 2 y y = 4).  
- Campo eléctrico concentrado entre las placas y decreciente hacia los bordes.  
- Diferencias visibles al comparar condiciones Dirichlet vs Neumann.  
- |E| máximo ≈ 6 para Vp1 = +6, Vp2 = −6 (con separación d = 2).

