from algoritmo import AlgoritmoBarrido
from Punto import Punto
from Segmento import Segmento
import LDLDA
BREAKLINE = 4

def createLDLA(file):
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
            if len(info) > 1:
                origen = vertices[info[1]]
                aristas[info[0]] = LDLDA.arista(origen)

    car = open(file + ".car", "r").read().split("\n")
    caras = dict()

    for y, el in enumerate(car):
        if y >= 4:
            info = el.split()
            if len(info) > 1:
                nueva_car = LDLDA.cara()

                if info[1] in aristas:
                    nueva_car.cmpint.append(aristas[info[1]])
                if info[2] in aristas:
                    nueva_car.cmpext.append(aristas[info[2]])

                caras[info[0]] = nueva_car

    for idx, el in enumerate(vert):
        if idx >= 4:
            info = el.split()
            if len(info) > 1:
                actual = vertices[info[0]]
                actual.aristaincidente.append(aristas[info[3]])

    for idx, el in enumerate(aristas):
        if idx >= 4:
            info = el.split()
            if len(info) > 1:
                actual = aristas[info[0]]
                actual.Pareja = aristas[info[2]]
                actual.caraincidente = caras[info[3]]
                actual.siguiente = aristas[info[4]]
                actual.siguiente = aristas[info[5]]


def main():
    ver01 = createLDLA("layer01")
    ver02 = createLDLA("layer02")

    '''  
    
    segmentos = [s1,s2]
    
    for s in segmentos:
      print(s)
    
    barr = AlgoritmoBarrido(segmentos)
    barr.barrer()
    print(barr.R)'''

if __name__=="__main__":
    main()



