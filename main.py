from gurobipy import GRB, Model, quicksum
'''
Conjunto de nutrientes I
donde $i \in I$
Este rando va de b_i a l_i
Son porcentajes de masa masa que van de 0 a 1
si bi es 0,15 significa que el 15% al menos
debe consisitir en masa de nutriente i

Tenemos el conjunto J de distintos cereales
$j \in J$ en la mezcla final

Cada uno tiene un costo por kilogramo de c_j
y contiene un %  masa masa a_{ij}
de nutriente $i \in I$
'''

class Modelo:
    
    def __init__(self) -> None:
        # Leer los archivos
        with open('limites.csv', 'r') as limites:
            limites_header = limites.readline().split(',')
            self.limites = [line.strip().split(',') for line in limites.readlines()]
            self.largo_limites = len(self.limites // 2)
        
        with open('costos.csv', 'r') as costos:
            costos_header = costos.readline().split(',')
            self.costos = [line.strip().split(',') for line in costos.readlines()]
            self.largo_costos = len(self.costos // 2)
            
        with open('contenidos_nutricionales.csv', 'r') as contenidos:
            contenidos_header = contenidos.readline().split(',')
            self.contenidos = [line.strip().split(',') for line in contenidos.readlines()]
            # Definicion de parametros:
            self.J = {j: self.costos[j] for j in range(len(contenidos_header))}
            self.I = {i+1: (self.limites[2*i], self.limites[2*i + 1]) for i in range(len(self.limites) // 2)}


    def modelar(self):
        # Implementando el modelo
        model = Model()
        model.setParam("TimeLimit", 60)

        # Variables

        '''
        Proporción (masa-masa)
        En la que estará presente el cereal 
        $j \in J$ en la mezcla final
        '''

        x_j = model.addVar(vtype=GRB.CONTINUOUS, name="x_j")

        model.update()

        # Restricciones

        '''
        La mezcla esta unicamente compuesta
        por cereales
        '''

        model.addConstr(x_j == 1, name="cereal")