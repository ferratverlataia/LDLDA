from algoritmo import AlgoritmoBarrido
from Punto import Punto
from Segmento import Segmento
import LDLDA
BREAKLINE = 4

def createVert(file):
    vert = open(file + ".ver", "r").read().split("\n")
    vertices = dict()
    for idx, el in enumerate(vert):
        if idx >= 4:
            info = el.split()
            if len(info) > 1:
                vertices[info[0]] = LDLDA.vertice(int(info[1]), int(info[2]))

    ari = open(file + ".ari", "r").read().split("\n")
    aristas = dict()

    for x, el in enumerate(ari):
        if x >= 4:
            info = el.split()
            print(info)
            if len(info) > 1:
                origen = vertices[info[1]]
                aristas[info[0]] = LDLDA.arista(origen)

    car = open(file + ".car", "r").read().split("\n")
    caras = dict()

    for y, el in enumerate(car):
        if y >= 4:
            info = el.split()
            print(info)
            if len(info) > 1:
                interno, externo = None, None
                if info[1] in aristas:
                    nueva_car.cmpint(aristas[info[1]])
                if info[2] in aristas:
                    nueva_car.cmpext(aristas[info[2]])
                nueva_car = LDLDA.cara()

                caras[info[0]] = nueva_car



def example01():
    # face 1
    ver01 = createVert("layer01")



def main():
    example01()
    '''  
    
    segmentos = [s1,s2]
    
    for s in segmentos:
      print(s)
    
    barr = AlgoritmoBarrido(segmentos)
    barr.barrer()
    print(barr.R)'''

if __name__=="__main__":
    main()



