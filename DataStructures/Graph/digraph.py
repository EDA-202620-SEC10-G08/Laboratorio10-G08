from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as al
from DataStructures.Graph import vertex as V
from DataStructures.Graph import edge as E


def new_graph(order):
    
    
    my_graph = {
        "vertices":mp.new_map(order, 0.5),
        "num_edges": 0
    }
    return my_graph

def insert_vertex(my_graph, key_u, info_u):
    vertice = V.new_vertex(key_u, info_u)
    mp.put(my_graph["vertices"], key_u, vertice)
    return my_graph

def add_edge(my_graph, key_u, key_v, weight=1.0):
    if not mp.contains(my_graph["vertices"], key_u):
        raise Exception("El vertice u no existe")

    if not mp.contains(my_graph["vertices"], key_v):
        raise Exception("El vertice v no existe")
    
    vertice_u = mp.get(my_graph["vertices"], key_u)

    arco = V.get_edge(vertice_u, key_v)
    if not arco:
        V.add_adjacent(vertice_u, key_v, weight)
        my_graph["num_edges"] += 1
    else:
        E.set_weight(arco, weight)

    return my_graph

def contains_vertex(my_graph, key_u):
    return mp.contains(my_graph["vertices"], key_u)

def order(my_graph):
    return mp.size(my_graph["vertices"])

def size(my_graph):
    return my_graph["num_edges"]

def degree(my_graph, key_u):
    
    if not mp.contains(my_graph["vertices"], key_u ):
        raise Exception("El vertice no existe")
    else:
        vertice_u = mp.get(my_graph["vertices"], key_u)
    
    return V.degree(vertice_u)

def adjacents(my_graph, key_u):
    if not mp.contains(my_graph["vertices"], key_u):
        raise Exception("El vertice no existe")
    else:
        vertice_u = mp.get(my_graph["vertices"], key_u)
        return mp.key_set(V.get_adjacents(vertice_u))

def vertices(my_graph):
    return mp.key_set(my_graph["vertices"])

def edges_vertex(my_graph, key_u):
    if not mp.contains(my_graph["vertices"], key_u):
        raise Exception("El vertice no existe")
    else:
        vertice_u = mp.get(my_graph["vertices"], key_u)
        return mp.value_set(V.get_adjacents(vertice_u))

def get_vertex(my_graph, key_u):
    return mp.get(my_graph["vertices"],key_u)

def update_vertex_info(my_graph, key_u, new_info_u):    
    if not mp.contains(my_graph["vertices"], key_u):
        return my_graph
    else:
        vertice_u = mp.get(my_graph["vertices"], key_u)
        V.set_value(vertice_u, new_info_u)
        return my_graph

def get_vertex_information(my_graph, key_u):
    if not mp.contains(my_graph["vertices"], key_u):
        raise Exception("El vertice no existe")
    else:
        vertice_u = mp.get(my_graph["vertices"], key_u)
        return V.get_value(vertice_u)
