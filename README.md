# Sistema Público de Cicloinfraestructura Intermunicipal (Cundinamarca)

Proyecto final de **Estructuras de Información** basado en la apuesta *Movilidad Contemporánea* del Plan de Desarrollo de Cundinamarca.

## Descripción del Modelo
* **Tipo de Grafo:** Simple, no dirigido, conexo y ponderado (`nx.Graph()`).
* **Nodos (22 vértices):** 8 estaciones/puntos actuales de Sabana Occidente + 14 nodos propuestos de expansión intermodal (Funza, Mosquera, Madrid, Bojacá y conexión con Bogotá).
* **Aristas (32 enlaces):** Tramos de ciclorruta ponderados bajo la función $w(u,v) = \text{distancia (km)} \times \text{factor de riesgo vial}$.

## Algoritmos Implementados
1. **BFS (Búsqueda en Anchura):** Análisis de cobertura por niveles desde `Funza_Parque`.
2. **DFS (Búsqueda en Profundidad):** Exploración de corredores continuos.
3. **Dijkstra:** Cálculo de la ruta óptima y más segura entre `Funza_Parque` y `Bojaca_Parque`.

## Requisitos y Ejecución
```bash
pip install networkx matplotlib
python ciclorrutas_cundinamarca.py
```
