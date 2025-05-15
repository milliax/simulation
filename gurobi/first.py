import gurobipy as gp
from gurobipy import GRB

# set data
element = [1, 2, 3, 4]
sets = {
    "A": {"elements": [1, 2], "cost": 3},
    "B": {"elements": [2, 3], "cost": 2},
    "C": {"elements": [3, 4], "cost": 1},
    "D": {"elements": [4], "cost": 2},
}

# create model
model = gp.Model("The name")

# create variables
x = model.addVars(sets.keys(), vtype=GRB.BINARY, name="workers")

# create objective
model.setObjective(
    gp.quicksum(sets[i]["cost"] * x[i] for i in sets.keys()), GRB.MINIMIZE
)

# create constraints
for e in element:
    model.addConstr(
        gp.quicksum(x[s] for s in sets.keys() if e in sets[s]["elements"]) >= 1,
        name=f"cover_{e}",
    )

# optimize model
model.optimize()
model.write("Model_Set_Covering_Problem.lp")

# print results
if model.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    for s in sets:
        if x[s].x > 0.5:
            print(f"Set {s} is selected with cost {sets[s]['cost']}")
    print("Objective value:", model.objVal)

else:
    print("No optimal solution found.")
