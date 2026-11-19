from DataStructures.Queue import queue as q
from DataStructures.Map import map_linear_probing as mlp
from DataStructures.Graph import digraph as D


def bfs(my_graph, source):
    visited_map = mlp.new_map(D.order(my_graph), 0.5)
    mlp.put(visited_map, source, visited_map)
    return visited_map

def bfs_vertex(my_graph, source, visited_map):
    cola = q.new_queue()
    q.enqueue(cola, source)
    valor ={
        "distance_to": 0,
        "edge_from": None
    }
    mlp.put(visited_map, source, valor)    
    while q.size(cola) != 0:
    

def has_path_to():
    pass

def path_to():
    pass
