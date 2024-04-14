from gurobipy import GRB, Model, quicksum

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