from DataStructures.Graph import digraph as D
from DataStructures.Map import map_linear_probing as mlp
from DataStructures.List import array_list as al
from DataStructures.Stack import stack as st


def dfs(my_graph, source):
    visited_map = mlp.new_map(D.order(my_graph), 0.5)
    valor = {
        "marked": True,
        "edge_from": None
    }
    mlp.put(visited_map, source, valor)
    dfs_vertex(my_graph, source, visited_map)
    return visited_map
    

def dfs_vertex(my_graph, vertex, visited_map):
    adyacentes = D.adjacents(my_graph, vertex)
    for i in range(al.size(adyacentes)):
        vecino = al.get_element(adyacentes, i)
        if not mlp.contains(visited_map, vecino):
            valor = {
                "marked": True,
                "edge_from": vertex
            }
            mlp.put(visited_map, vecino, valor )
            dfs_vertex(my_graph, vecino, visited_map)
    return visited_map


def has_path_to(key_v, visited_map):
    return mlp.contains(visited_map, key_v)

def path_to(key_v, visited_map):
    if has_path_to(key_v, visited_map):
        camino = st.new_stack()
        while key_v != None:
            anterior = mlp.get(visited_map, key_v)["edge_from"]
            st.push(camino, key_v)
            key_v = anterior
        return camino
    
    else:
        return None