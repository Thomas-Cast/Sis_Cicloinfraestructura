import networkx as nx
import matplotlib.pyplot as plt

def construir_red(incluir_propuesta=False):
    G = nx.Graph()
    
    # 1. GRAFO BASE ACTUAL (8 nodos y 11 aristas)
    nodos_actuales = [
        ("Funza_Parque", {"municipio": "Funza", "estado": "Actual"}),
        ("Funza_Furatena", {"municipio": "Funza", "estado": "Actual"}),
        ("Funza_SieteTrojes", {"municipio": "Funza", "estado": "Actual"}),
        ("Funza_Serrezuelita", {"municipio": "Funza", "estado": "Actual"}),
        ("Mosquera_Planadas", {"municipio": "Mosquera", "estado": "Actual"}),
        ("Mosquera_Parque", {"municipio": "Mosquera", "estado": "Actual"}),
        ("Madrid_Sosiego", {"municipio": "Madrid", "estado": "Actual"}),
        ("Madrid_Parque", {"municipio": "Madrid", "estado": "Actual"})
    ]
    G.add_nodes_from(nodos_actuales)
    
    aristas_actuales = [
        ("Funza_Parque", "Funza_Furatena", 1.5),
        ("Funza_Parque", "Funza_SieteTrojes", 2.1),
        ("Funza_Parque", "Funza_Serrezuelita", 1.98),
        ("Funza_Furatena", "Mosquera_Planadas", 2.88),
        ("Funza_Furatena", "Funza_SieteTrojes", 1.7),
        ("Mosquera_Planadas", "Mosquera_Parque", 1.9),
        ("Funza_SieteTrojes", "Mosquera_Parque", 3.84),
        ("Funza_Serrezuelita", "Madrid_Sosiego", 9.86),
        ("Mosquera_Parque", "Madrid_Sosiego", 6.3),
        ("Mosquera_Parque", "Madrid_Parque", 9.92),
        ("Madrid_Sosiego", "Madrid_Parque", 2.0)
    ]
    for u, v, w in aristas_actuales:
        G.add_edge(u, v, weight=w, tipo="Actual")
        
    # 2. PROPUESTA DE EXPANSIÓN (+14 nodos estratégicos -> Total = 22 nodos)
    if incluir_propuesta:
        nodos_propuestos = [
            ("Funza_GimnasioBora", {"municipio": "Funza", "estado": "Propuesto"}),
            ("Funza_RegioTram", {"municipio": "Funza", "estado": "Propuesto"}),
            ("Mosquera_ElTrebol", {"municipio": "Mosquera", "estado": "Propuesto"}),
            ("Mosquera_Novaterra", {"municipio": "Mosquera", "estado": "Propuesto"}),
            ("Mosquera_VillaNueva", {"municipio": "Mosquera", "estado": "Propuesto"}),
            ("Mosquera_RegioTram", {"municipio": "Mosquera", "estado": "Propuesto"}),
            ("Madrid_LaProsperidad", {"municipio": "Madrid", "estado": "Propuesto"}),
            ("Madrid_Loreto", {"municipio": "Madrid", "estado": "Propuesto"}),
            ("Madrid_ZonaFranca", {"municipio": "Madrid", "estado": "Propuesto"}),
            ("Madrid_RegioTram", {"municipio": "Madrid", "estado": "Propuesto"}),
            ("Bojaca_ChivoNegro", {"municipio": "Bojaca", "estado": "Propuesto"}),
            ("Bojaca_Parque", {"municipio": "Bojaca", "estado": "Propuesto"}),
            ("Bogota_PuenteGrande", {"municipio": "Bogota", "estado": "Propuesto"}),
            ("Bogota_Fontibon_HB", {"municipio": "Bogota", "estado": "Propuesto"})
        ]
        G.add_nodes_from(nodos_propuestos)
        
        aristas_propuestas = [
            ("Funza_Parque", "Funza_GimnasioBora", 1.4),
            ("Funza_Furatena", "Funza_GimnasioBora", 1.6),
            ("Funza_Serrezuelita", "Funza_RegioTram", 1.3),
            ("Funza_GimnasioBora", "Funza_RegioTram", 1.9),
            ("Funza_RegioTram", "Mosquera_RegioTram", 2.8),
            ("Mosquera_Planadas", "Mosquera_Novaterra", 2.2),
            ("Mosquera_Parque", "Mosquera_VillaNueva", 1.6),
            ("Mosquera_VillaNueva", "Mosquera_ElTrebol", 1.8),
            ("Mosquera_Novaterra", "Mosquera_RegioTram", 1.5),
            ("Mosquera_Novaterra", "Bogota_PuenteGrande", 3.85),
            ("Bogota_PuenteGrande", "Bogota_Fontibon_HB", 3.19),
            ("Mosquera_ElTrebol", "Madrid_Sosiego", 3.41),
            ("Mosquera_RegioTram", "Madrid_ZonaFranca", 3.74),
            ("Madrid_ZonaFranca", "Madrid_LaProsperidad", 2.1),
            ("Madrid_LaProsperidad", "Madrid_Sosiego", 1.7),
            ("Madrid_Parque", "Madrid_Loreto", 1.5),
            ("Madrid_Loreto", "Madrid_RegioTram", 1.2),
            ("Madrid_ZonaFranca", "Madrid_RegioTram", 2.3),
            ("Madrid_Loreto", "Bojaca_ChivoNegro", 5.28),
            ("Madrid_RegioTram", "Bojaca_ChivoNegro", 5.61),
            ("Bojaca_ChivoNegro", "Bojaca_Parque", 4.62)
        ]
        for u, v, w in aristas_propuestas:
            G.add_edge(u, v, weight=w, tipo="Propuesto")
            
    return G

if __name__ == "__main__":
    G_base = construir_red(incluir_propuesta=False)
    G_prop = construir_red(incluir_propuesta=True)

    print("=== MÉTRICAS GENERALES ===")
    print(f"Grafo Base      -> Vértices: {G_base.number_of_nodes()} | Aristas: {G_base.number_of_edges()} | Conexo: {nx.is_connected(G_base)}")
    print(f"Grafo Propuesto -> Vértices: {G_prop.number_of_nodes()} | Aristas: {G_prop.number_of_edges()} | Conexo: {nx.is_connected(G_prop)}")

    # 1. Recorridos BFS y DFS desde Funza_Parque
    origen = "Funza_Parque"
    destino = "Bojaca_Parque"
    
    recorrido_bfs = list(nx.bfs_tree(G_prop, source=origen).nodes())
    recorrido_dfs = list(nx.dfs_tree(G_prop, source=origen).nodes())
    
    print(f"\n=== RECORRIDO BFS DESDE {origen} ===")
    print(recorrido_bfs)
    
    print(f"\n=== RECORRIDO DFS DESDE {origen} ===")
    print(recorrido_dfs)

    # 2. Ruta Óptima con Dijkstra
    ruta_optima = nx.dijkstra_path(G_prop, source=origen, target=destino, weight="weight")
    costo_optimo = nx.dijkstra_path_length(G_prop, source=origen, target=destino, weight="weight")
    
    print(f"\n=== RUTA ÓPTIMA DIJKSTRA ({origen} -> {destino}) ===")
    print("Camino:", " -> ".join(ruta_optima))
    print("Peso total (km * riesgo):", round(costo_optimo, 2))

    # 3. Visualización
    plt.figure(figsize=(18, 12))
    pos = nx.spring_layout(G_prop, seed=42, k=1.15)
    
    colores_nodos = [
        "#4ea8de" if G_prop.nodes[n]["estado"] == "Actual" else "#52b788"
        for n in G_prop.nodes()
    ]
    
    nx.draw(
        G_prop, pos, with_labels=True, node_color=colores_nodos,
        node_size=1800, font_size=8, font_weight="bold",
        edge_color="#adb5bd", width=1.5
    )
    
    aristas_ruta = list(zip(ruta_optima[:-1], ruta_optima[1:]))
    nx.draw_networkx_edges(G_prop, pos, edgelist=aristas_ruta, edge_color="#e63946", width=4)
    nx.draw_networkx_edge_labels(G_prop, pos, edge_labels=nx.get_edge_attributes(G_prop, "weight"), font_size=7)
    
    plt.title("Sistema Público de Cicloinfraestructura Intermunicipal (22 Nodos) - Ruta Óptima en Rojo", fontsize=12)
    plt.tight_layout()
    plt.show()
