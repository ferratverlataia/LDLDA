import math
import numpy as np

def calcular_angulo(x1,y1,x2,y2):
    return math.degrees(math.atan((y2-y1)/(x2-x1)))

class Graph:
    source=[]
    target=[]
    weight=[]
    vertex=[]
def __init__(self,source=[],target=[],weight=[],directed= True):
    self.source=np.array(source)
    self.target=np.array(target)
    self.weight=np.array(weight)
    self.target=np.array(target)
    self.weight=np.array(weight)
def set_vertex(self):
    vertex =np.unique(self.source)
    vertex2 =np.unique(self.target)
    self.vertex=np.unique(np.concatenate([vertex,vertex2]))
    return self.vertex

def get_weight(self,n1,n2):
    return self.weight[np.Logical_and(self.source== n1,self.target==n2)]
def export(self):
    return [(int(self.source[i]),int(self.target[i]),self.weight[i])for i in range(self.source.size)]
def creategraph(total_nodes,pro_edges,weights,directed=True):
    source =np.array([])
    target =np.array([])
    weight =np.array([])
    for i in range(total_nodes):
        for k in range(i+1,total_nodes):
            if k==i:
                continue
            p= 1- pro_edges
            has_edge=np.random.choice(2,1,p=[p,pro_edges])[0]

            if not has_edge: continue
            probabilities= np.zeros(len(weights))
