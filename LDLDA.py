class vertice:
    def __init__(self):
        self.coord=tuple()
        self.aristaincidente= list()


class cara:
    def __init__(self):
        self.cmpint=list()
        self.cmpext=list()
class arista:
    def __init__(self,inicio):
        self.origin=inicio
        self.caraincidente=None
        self.Pareja=None
        self.anterior=None
        self.siguiente=None
