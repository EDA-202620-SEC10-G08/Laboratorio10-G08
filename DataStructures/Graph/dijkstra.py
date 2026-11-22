from DataStructures.Graph import digraph as D 
from DataStructures.Graph import dijsktra_structure as ds
from DataStructures.Map import map_linear_probing as mlp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.List import array_list as al
from DataStructures.Graph import edge as E
import math
from DataStructures.Stack import stack as st


def dijkstra(my_graph, source):
    estructura = ds.new_dijsktra_structure(source, D.order(my_graph))
    if D.contains_vertex(my_graph, source):
        vertices = D.vertices(my_graph)
        for i in range(al.size(vertices)):
            vertice = al.get_element(vertices, i)
            mlp.put(estructura["visited"], vertice, {"marked": False, "edge_from": None, "dist_to": math.inf})

        valor = {
            "marked": False,
            "dist_to": 0.0,
            "edge_from": None
        }
        mlp.put(estructura["visited"], source, valor)
        pq.insert(estructura["pq"], 0.0, source)
        
        while not pq.is_empty(estructura["pq"]):
            v = pq.remove(estructura["pq"])
            info_v = mlp.get(estructura["visited"], v)
            info_v["marked"] = True
            
            arcos = D.edges_vertex(my_graph, v)
            
            for i in range(al.size(arcos)):
                arco = al.get_element(arcos, i)
                destino = E.to(arco)
                peso = E.weight(arco)
                info_w = mlp.get(estructura["visited"], destino)
                    
                if not info_w["marked"] and info_v["dist_to"] + peso < info_w["dist_to"]:
                    info_w["edge_from"] = v
                    info_w["dist_to"] = info_v["dist_to"] + peso
                    
                    if pq.contains(estructura["pq"], destino):
                        pq.improve_priority(estructura["pq"], info_w["dist_to"], destino)
                    else:
                        pq.insert(estructura["pq"], info_w["dist_to"], destino)
    
    return estructura
    
def dist_to(aux_structure, key_v):
    elemento = mlp.get(aux_structure["visited"], key_v)
    if elemento == None:
        return math.inf
    return elemento["dist_to"]
    

def has_path_to(structure, vertex):
    info = mlp.get(structure["visited"], vertex)
    if info is None:
        return False
    return info["marked"]

def path_to(aux_structure, key_v):
    if has_path_to(aux_structure, key_v):
        camino = st.new_stack()
        while key_v != None:
            anterior = mlp.get(aux_structure["visited"], key_v)["edge_from"]
            st.push(camino, key_v)
            key_v = anterior
        return camino
    else:
        return None
            
        
