import sys  


def min_key(key, mst_set, V):
    
    min_val = sys.maxsize
    min_index = -1

    for v in range(V):
        if key[v] < min_val and mst_set[v] == False:
            min_val = key[v]
            min_index = v

    return min_index


def print_mst(parent, graph, V):
    print("Edge \tWeight")
    for i in range(1, V):
        print("{} - {} \t{}".format(parent[i], i, graph[i][parent[i]]))



def prim_mst(graph):
    V = len(graph) 
    key = [sys.maxsize] * V
    parent = [None] * V
    mst_set = [False] * V
    key[0] = 0
    parent[0] = -1  

    for _ in range(V):
       
        u = min_key(key, mst_set, V)
        mst_set[u] = True

       
        for v in range(V):
          
            if graph[u][v] > 0 and mst_set[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

   
    print_mst(parent, graph, V)

# Example usage
if __name__ == "__main__":
  
    graph = [[0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0]]

    
    prim_mst(graph)
