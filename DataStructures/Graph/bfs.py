from DataStructures.Queue import queue as q
from DataStructures.Map import map_linear_probing as mlp
from DataStructures.Graph import digraph as D
from DataStructures.List import array_list as al
from DataStructures.Stack import stack as st


def bfs(my_graph, source):
    visited_map = mlp.new_map(D.order(my_graph), 0.5)
    bfs_vertex(my_graph, source, visited_map)
    return visited_map

def bfs_vertex(my_graph, source, visited_map):
    cola = q.new_queue()
    q.enqueue(cola, source)
    valor ={
        "distance_to": 0,
        "edge_from": None
    }
    mlp.put(visited_map, source, valor)    
    while not q.is_empty(cola):
        actual = q.dequeue(cola)
        adyacentes = D.adjacents(my_graph, actual)
        for i in range(al.size(adyacentes)):
            vecino = al.get_element(adyacentes, i)
            if not mlp.contains(visited_map, vecino):
                q.enqueue(cola, vecino)
                valor = {
                    "edge_from": actual,
                    "distance_to": mlp.get(visited_map, actual)["distance_to"] + 1
                }
                mlp.put(visited_map,vecino, valor)
        
    return visited_map

def has_path_to(key_v, visited_map):
    return mlp.contains(visited_map, key_v)

def path_to(key_v, visited_map):
    if has_path_to(visited_map, key_v):
        camino = st.new_stack()
        while key_v != None:
            v = mlp.get(visited_map, key_v)["edge_from"]
            st.push(camino, key_v)
            key_v = v
        return camino
    else:
        return None
