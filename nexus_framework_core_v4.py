"""
=========================================================
NEXUS FRAMEWORK CORE V4
Criticality / Phase Dynamics Engine
=========================================================

Autor:
Erick Rojas (Efeseis-F6)

---------------------------------------------------------
NOVEDADES V4
---------------------------------------------------------

- Criticalidad autoorganizada
- Mapa de fases Nexus
- Temperatura informacional
- Susceptibilidad dinámica
- Magnetización ternaria
- Detección de transición de fase
- Evolución parcialmente reversible
- Tensor dinámico de coherencia
- Fronteras de dominio
- Métricas avanzadas
- Snapshots automáticos
- Exportación total CSV

---------------------------------------------------------
REQUISITOS
---------------------------------------------------------

pip install numpy matplotlib pandas

---------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import deque
import os

# =====================================================
# CONFIGURACIÓN
# =====================================================

GRID_SIZE = 120
ITERATIONS = 500

TRITS = [-1, 0, 1]

# Parámetros Nexus
ALPHA = 0.50
BETA = 0.34
GAMMA = 0.14
DELTA = 0.07
OMEGA = 0.05

# Temperatura informacional
TEMPERATURE = 0.12

np.random.seed(42)

# =====================================================
# DIRECTORIO SNAPSHOTS
# =====================================================

SNAPSHOT_DIR = "nexus_snapshots_v4"

if not os.path.exists(SNAPSHOT_DIR):
    os.makedirs(SNAPSHOT_DIR)

# =====================================================
# CAMPO INFORMACIONAL
# =====================================================

phi = np.random.choice(TRITS, size=(GRID_SIZE, GRID_SIZE))

# =====================================================
# HISTORIAL
# =====================================================

coherence_history = []
entropy_history = []
energy_history = []
curvature_history = []
cluster_history = []
correlation_history = []
magnetization_history = []
susceptibility_history = []

# =====================================================
# VECINOS
# =====================================================

def get_neighbors(field, x, y):

    neighbors = []

    for dx, dy in [
        (-1,0),(1,0),
        (0,-1),(0,1)
    ]:

        nx = (x + dx) % GRID_SIZE
        ny = (y + dy) % GRID_SIZE

        neighbors.append(field[nx, ny])

    return neighbors

# =====================================================
# COHERENCIA
# =====================================================

def coherence(field):

    coherent = 0
    total = 0

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):

            current = field[x, y]

            for n in get_neighbors(field, x, y):

                total += 1

                if current == n:
                    coherent += 1

    return coherent / total

# =====================================================
# ENTROPÍA
# =====================================================

def entropy(field):

    values, counts = np.unique(field, return_counts=True)

    probs = counts / counts.sum()

    s = 0

    for p in probs:
        s -= p * np.log2(p)

    return s

# =====================================================
# CURVATURA
# =====================================================

def local_curvature(field, x, y):

    center = field[x, y]

    diff = 0

    for n in get_neighbors(field, x, y):
        diff += abs(center - n)

    return diff / 4

# =====================================================
# ENERGÍA
# =====================================================

def informational_energy(field):

    energy = 0

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):

            current = field[x, y]

            for n in get_neighbors(field, x, y):
                energy += abs(current - n)

    return energy / 2

# =====================================================
# CORRELACIÓN ESPACIAL
# =====================================================

def spatial_correlation(field):

    corr = 0
    total = 0

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):

            current = field[x, y]

            for n in get_neighbors(field, x, y):

                corr += current * n
                total += 1

    return corr / total

# =====================================================
# MAGNETIZACIÓN TERNARIA
# =====================================================

def magnetization(field):

    return np.sum(field) / (GRID_SIZE * GRID_SIZE)

# =====================================================
# SUSCEPTIBILIDAD
# =====================================================

def susceptibility(field):

    m = magnetization(field)

    fluctuations = np.var(field)

    return fluctuations / (TEMPERATURE + 1e-6)

# =====================================================
# DETECCIÓN DE CLUSTERS
# =====================================================

def detect_clusters(field):

    visited = np.zeros_like(field, dtype=bool)

    clusters = 0

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):

            if visited[x, y]:
                continue

            state = field[x, y]

            queue = deque()
            queue.append((x, y))

            visited[x, y] = True

            size = 0

            while queue:

                cx, cy = queue.popleft()

                size += 1

                for dx, dy in [
                    (-1,0),(1,0),
                    (0,-1),(0,1)
                ]:

                    nx = (cx + dx) % GRID_SIZE
                    ny = (cy + dy) % GRID_SIZE

                    if not visited[nx, ny]:

                        if field[nx, ny] == state:

                            visited[nx, ny] = True
                            queue.append((nx, ny))

            if size > 12:
                clusters += 1

    return clusters

# =====================================================
# TENSOR DE COHERENCIA
# =====================================================

def coherence_tensor(field, x, y):

    current = field[x, y]

    tensor = 0

    for n in get_neighbors(field, x, y):
        tensor += current * n

    return tensor / 4

# =====================================================
# FRONTERAS DE DOMINIO
# =====================================================

def domain_boundaries(field):

    boundaries = 0

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):

            current = field[x, y]

            for n in get_neighbors(field, x, y):

                if current != n:
                    boundaries += 1

    return boundaries / 2

# =====================================================
# OPERADORES NEXUS
# =====================================================

def operator_sync(neighbors):

    total = np.sum(neighbors)

    if total > 0:
        return 1

    elif total < 0:
        return -1

    return 0

def operator_cross(a, b):
    return a * b

# =====================================================
# DINÁMICA REVERSIBLE PARCIAL
# =====================================================

def reversible_component(current, previous):

    if np.random.rand() < 0.02:
        return previous

    return current

# =====================================================
# EVOLUCIÓN V4
# =====================================================

def evolve(field, previous_field):

    new_field = np.copy(field)

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):

            current = field[x, y]

            neighbors = get_neighbors(field, x, y)

            sync = operator_sync(neighbors)

            cross = operator_cross(current, sync)

            curvature = local_curvature(field, x, y)

            tensor = coherence_tensor(field, x, y)

            thermal_noise = np.random.normal(0, TEMPERATURE)

            value = (
                ALPHA * current +
                BETA * sync +
                GAMMA * cross +
                OMEGA * tensor -
                DELTA * curvature +
                thermal_noise
            )

            # Dinámica reversible parcial

            value = reversible_component(
                value,
                previous_field[x, y]
            )

            # Cuantización ternaria

            if value > 0.4:
                new_field[x, y] = 1

            elif value < -0.4:
                new_field[x, y] = -1

            else:
                new_field[x, y] = 0

    return new_field

# =====================================================
# CONSERVACIÓN GLOBAL
# =====================================================

def preserve_balance(old_field, new_field):

    old_sum = np.sum(old_field)
    new_sum = np.sum(new_field)

    diff = old_sum - new_sum

    flat = new_field.flatten()

    for _ in range(abs(diff)):

        idx = np.random.randint(0, len(flat))

        if diff > 0:
            flat[idx] = min(flat[idx] + 1, 1)

        elif diff < 0:
            flat[idx] = max(flat[idx] - 1, -1)

    return flat.reshape((GRID_SIZE, GRID_SIZE))

# =====================================================
# VISUALIZACIÓN
# =====================================================

plt.ion()

fig, ax = plt.subplots(figsize=(9,9))

image = ax.imshow(phi)

# =====================================================
# LOOP PRINCIPAL
# =====================================================

print("\n======================================")
print(" NEXUS FRAMEWORK CORE V4 ")
print("======================================\n")

previous_phi = np.copy(phi)

stable_counter = 0
previous_entropy = None

for t in range(ITERATIONS):

    old_phi = np.copy(phi)

    phi = evolve(phi, previous_phi)

    phi = preserve_balance(old_phi, phi)

    previous_phi = old_phi

    # ==========================================
    # MÉTRICAS
    # ==========================================

    c = coherence(phi)

    s = entropy(phi)

    e = informational_energy(phi)

    corr = spatial_correlation(phi)

    m = magnetization(phi)

    susc = susceptibility(phi)

    clusters = detect_clusters(phi)

    boundaries = domain_boundaries(phi)

    # Curvatura promedio

    curv_sum = 0

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            curv_sum += local_curvature(phi, x, y)

    avg_curv = curv_sum / (GRID_SIZE**2)

    # ==========================================
    # HISTORIAL
    # ==========================================

    coherence_history.append(c)
    entropy_history.append(s)
    energy_history.append(e)
    curvature_history.append(avg_curv)
    cluster_history.append(clusters)
    correlation_history.append(corr)
    magnetization_history.append(m)
    susceptibility_history.append(susc)

    # ==========================================
    # ATTRACTOR
    # ==========================================

    if previous_entropy is not None:

        if abs(previous_entropy - s) < 0.00003:
            stable_counter += 1
        else:
            stable_counter = 0

    previous_entropy = s

    # ==========================================
    # VISUALIZACIÓN
    # ==========================================

    image.set_data(phi)

    ax.set_title(
        f"iter={t} | "
        f"C={c:.3f} | "
        f"S={s:.3f} | "
        f"M={m:.3f}"
    )

    plt.pause(0.001)

    # ==========================================
    # SNAPSHOTS
    # ==========================================

    if t in [0,10,25,50,100]:

        plt.imsave(
            f"{SNAPSHOT_DIR}/snapshot_{t}.png",
            phi
        )

    # ==========================================
    # LOG
    # ==========================================

    if t % 10 == 0:

        print(
            f"iter={t:03d} | "
            f"C={c:.4f} | "
            f"S={s:.4f} | "
            f"E={e:.0f} | "
            f"Corr={corr:.4f} | "
            f"M={m:.4f} | "
            f"Chi={susc:.4f} | "
            f"Clusters={clusters} | "
            f"Boundaries={boundaries:.0f}"
        )

    # ==========================================
    # DETECCIÓN DE ESTABILIDAD
    # ==========================================

    if stable_counter > 35:

        print("\n>>> ATTRACTOR DETECTADO")
        print(f">>> Sistema estabilizado en iteración {t}")

        break

# =====================================================
# EXPORTAR CSV
# =====================================================

df = pd.DataFrame({

    "iteration": np.arange(len(coherence_history)),
    "coherence": coherence_history,
    "entropy": entropy_history,
    "energy": energy_history,
    "curvature": curvature_history,
    "clusters": cluster_history,
    "correlation": correlation_history,
    "magnetization": magnetization_history,
    "susceptibility": susceptibility_history

})

df.to_csv("nexus_v4_metrics.csv", index=False)

print("\nCSV exportado: nexus_v4_metrics.csv")

# =====================================================
# DISTRIBUCIÓN FINAL
# =====================================================

print("\nDistribución final de trits:")

unique, counts = np.unique(phi, return_counts=True)

for u, ccount in zip(unique, counts):

    print(f"Trit {u}: {ccount}")

# =====================================================
# GRÁFICOS
# =====================================================

plt.figure(figsize=(10,5))
plt.plot(coherence_history)
plt.title("Coherencia Global")

plt.figure(figsize=(10,5))
plt.plot(entropy_history)
plt.title("Entropía")

plt.figure(figsize=(10,5))
plt.plot(energy_history)
plt.title("Energía Informacional")

plt.figure(figsize=(10,5))
plt.plot(curvature_history)
plt.title("Curvatura")

plt.figure(figsize=(10,5))
plt.plot(cluster_history)
plt.title("Clusters")

plt.figure(figsize=(10,5))
plt.plot(correlation_history)
plt.title("Correlación Espacial")

plt.figure(figsize=(10,5))
plt.plot(magnetization_history)
plt.title("Magnetización")

plt.figure(figsize=(10,5))
plt.plot(susceptibility_history)
plt.title("Susceptibilidad")

plt.show()

# =====================================================
# RESULTADOS FINALES
# =====================================================

print("\n======================================")
print(" RESULTADOS FINALES V4 ")
print("======================================")

print(f"Coherencia final : {coherence_history[-1]:.4f}")
print(f"Entropía final   : {entropy_history[-1]:.4f}")
print(f"Energía final    : {energy_history[-1]:.2f}")
print(f"Curvatura final  : {curvature_history[-1]:.4f}")
print(f"Correlación      : {correlation_history[-1]:.4f}")
print(f"Magnetización    : {magnetization_history[-1]:.4f}")
print(f"Susceptibilidad  : {susceptibility_history[-1]:.4f}")
print(f"Clusters finales : {cluster_history[-1]}")

print("\nInterpretación Nexus:")
print("- Coherencia alta → sincronización global")
print("- Entropía residual → complejidad adaptativa")
print("- Correlación → orden espacial")
print("- Magnetización → polarización emergente")
print("- Susceptibilidad → sensibilidad crítica")
print("- Clusters → estructuras autoorganizadas")

print("\nFin de Nexus Framework Core V4.")
# =====================================================
# EXPORTACIÓN DE GRÁFICOS 
# =====================================================

PLOTS_DIR = os.path.join(SNAPSHOT_DIR, "final_plots")
os.makedirs(PLOTS_DIR, exist_ok=True)

def save_plot(data, title, filename):
    plt.figure(figsize=(14, 7))  
    plt.plot(data)
    plt.title(title)
    plt.xlabel("Iterations")
    plt.ylabel("Value")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, filename), dpi=300)
    plt.close()

# =====================================================
# GRÁFICOS FINALES (ALTA RESOLUCIÓN)
# =====================================================

save_plot(coherence_history, "Coherencia Global (Nexus V4)", "coherence.png")
save_plot(entropy_history, "Entropía Informacional", "entropy.png")
save_plot(energy_history, "Energía Informacional", "energy.png")
save_plot(curvature_history, "Curvatura Media", "curvature.png")
save_plot(cluster_history, "Clusters Emergentes", "clusters.png")
save_plot(correlation_history, "Correlación Espacial", "correlation.png")
save_plot(magnetization_history, "Magnetización Ternaria", "magnetization.png")
save_plot(susceptibility_history, "Susceptibilidad Crítica", "susceptibility.png")

# =====================================================
# FIGURA COMPUESTA 
# =====================================================

plt.figure(figsize=(16, 10))

plt.subplot(2, 2, 1)
plt.plot(coherence_history)
plt.title("Coherencia")

plt.subplot(2, 2, 2)
plt.plot(entropy_history)
plt.title("Entropía")

plt.subplot(2, 2, 3)
plt.plot(energy_history)
plt.title("Energía")

plt.subplot(2, 2, 4)
plt.plot(correlation_history)
plt.title("Correlación")

plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "summary_panel.png"), dpi=300)
plt.close()

print("\nFIGURAS EXPORTADAS EN ALTA RESOLUCIÓN:")
print(PLOTS_DIR)
