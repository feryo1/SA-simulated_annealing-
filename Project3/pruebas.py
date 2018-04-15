import re
import SimulatedAnnealing as sa
import random
datos = []
ciudades = {}
with open('kroA100.txt') as fp:
    for line in fp:
        if re.match('^[1-9]+', line) is not None:
            renglon = (line.strip()).split(' ')
            datos.append([int(renglon[1]), int(renglon[2])])
            ciudades[int(renglon[0])] = (int(renglon[1]), int(renglon[2]))

print(ciudades)
# initial state, a randomly-ordered itinerary
init_state = list(ciudades.keys())
random.shuffle(init_state)

# create a distance matrix
distance_matrix = {}
for ka, va in ciudades.items():
    distance_matrix[ka] = {}
    for kb, vb in ciudades.items():
        if kb == ka:
            distance_matrix[ka][kb] = 0.0
        else:
            distance_matrix[ka][kb] = sa.distance(va, vb)

tsp = sa.TravellingSalesmanProblem(init_state, distance_matrix)
tsp.steps = 100000
# since our state is just a list, slice is the fastest way to copy
tsp.copy_strategy = "slice"
state, e = tsp.anneal()

while state[0] != 8:
    state = state[1:] + state[:1]  # rotate NYC to start

print()
print("%i mile route:" % e)
for city in state:
    print("\t", city)