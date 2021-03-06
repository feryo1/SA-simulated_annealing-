import networkx as nx
import matplotlib.pyplot as plt
import sys
import Salesman1 as sm
import numpy as np
import re
import time
import SimulatedAnnealing as sa
import random
import os

def procesar1():
    G = nx.Graph()
    G.add_edge('Ayala','Xochiltepec',weight=82.80)    
    G.add_edge('Puente de Ixtla','Jojutla',weight=25.90)   
    G.add_edge('Tlaltizapan','Yecapixtla',weight=78.40)
    G.add_edge('Tepoztlan','Zacatepec',weight=69.80)
    G.add_edge('Axochiapan','Zacatepec',weight=74.50)    
    G.add_edge('Jojutla','Yecapixtla',weight=123.0)
    G.add_edge('Tepoztlan','Xochiltepec',weight=114.0)    
    G.add_edge('Tepoztlan','Puente de Ixtla',weight=76.30)    
    G.add_edge('Tlaltizapan','Zacatepec',weight=12.90)
    G.add_edge('Tlaltizapan','Ayala',weight=32.2)   
    G.add_edge('Jojutla','Ayala',weight=67.4)    
    G.add_edge('Yecapixtla','Axochiapan',weight=61.90) 
    G.add_edge('Axochiapan','Xochiltepec',weight=75.60)
    G.add_edge('Zacatepec','Jojutla',weight=7.80)    
    G.add_edge('Yecapixtla','Puente de Ixtla',weight=108.00)  
    G.add_edge('Puente de Ixtla','Ayala',weight=76.0) 
    G.add_edge('Tetela del Volcan','Miacatlan',weight=127.18)
    G.add_edge('Yecapixtla','Miacatlan',weight=109.65)
    G.add_edge('Emiliano Zapata','Temixco',weight=30.7)
    G.add_edge('Atlatlahucan','Miacatlan',weight=86.3)
    G.add_edge('Tlaltizapan','Atlatlahucan',weight=49.7)
    G.add_edge('Axochiapan','Miacatlan',weight=94.8)
    G.add_edge('Tlaltizapan','Zacatepec',weight=10.3)
    G.add_edge('Zacatepec','Miacatlan',weight=30.3)
    G.add_edge('Tlaltizapan','Axochiapan',weight=55.8)
    G.add_edge('Tetela del Volcan','Miacatlan',weight=127.5)
    G.add_edge('Tlaltizapan','Tetela del Volcan',weight=168.18)
    G.add_edge('Zacatepec','Tepalcingo',weight=49.5)
    G.add_edge('Tlaltizapan','Temixco',weight=32.6)
    G.add_edge('Axochiapan','Zacatepec',weight=65.4)
    G.add_edge('Tlaltizapan','Tepalcingo',weight=39.5)

    ################    dibujar el grafo
    elarge=[(u,v) for (u,v,d) in G.edges(data=True)]
    pos = {'Cuernavaca': [18.92,-99.22], 'Jiutepec': [18.89,-99.17],
                  'Cuautla': [18.81,-98.95], 'Temixco': [18.85,-99.23],
                  'Yautepec': [18.88,-99.06], 'Emiliano Zapata': [18.84,-99.18],
                  'Ayala': [18.76,-98.98], 'Xochiltepec': [18.77,-99.23],
                  'Puente de Ixtla': [18.61,-99.32], 'Jojutla': [18.61,-99.17],
                  'Tlaltizapan': [18.68,-99.12], 'Yecapixtla': [18.88,-98.86],
                  'Tepoztlan': [18.98,-99.09], 'Zacatepec': [18.65,-99.19],
                  'Axochiapan': [18.50,-98.75], 'Tlaquiltenango': [18.63,-99.16],
                  'Tepalcingo': [18.59,-98.84], 'Miacatlan': [18.77,-99.35],
                  'Tetela del Volcan': [18.89,-98.71], 'Atlatlahucan': [18.93,-98.89]
                  }
    datos = []
    for key, value in pos.items():
        datos.append(value)
    #drawing nodes
    nx.draw_networkx_nodes(G,pos,node_size=100,node_color='b')
    #drawing edges
    nx.draw_networkx_edges(G,pos,edgelist=elarge,width=2,alpha=0.5,edge_color='r')

    #drawing labels
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

    print(G.nodes())
    ####Origen-Destino
    origen = (input("Ingresa origen:")).title()
    if not (G.has_node(origen)):
        print("Origen no encontrado")
        sys.exit()
    destino = (input("Ingresa destino:")).title()
    if not (G.has_node(destino)):
        print("Origen no encontrado")
        sys.exit()

    ####rutas
    print("Ruta mas corta:")
    start_time = time.time()
    print(nx.shortest_path(G, origen, destino, weight='weight'))#ruta mas corta
    print("--- SPA: %s seconds ---" % (time.time() - start_time))
    print("Distancia: ",nx.shortest_path_length(G, origen, destino, weight='weight'))#distancia mas corta
    plt.axis('off')
    plt.show()

    print("Minimum Spanning tree:")
    start_time = time.time()
    T=nx.minimum_spanning_tree(G)
    print("--- MST: %s seconds ---" % (time.time() - start_time))
    print(sorted(T.edges(data=True)))
    plt.figure()
    elarge=[(u,v) for (u,v,d) in T.edges(data=True)]
    nx.draw_networkx_nodes(G,pos,node_size=100,node_color='b')
    nx.draw_networkx_edges(G,pos,edgelist=elarge,width=2,alpha=0.5,edge_color='r')
    plt.axis('off')
    plt.show()

    #nombres=("Cuernavaca","Jiutepec","Cuautla","Temixco","Yautepec","Emiliano Zapata","Ayala","Xochiltepec","Puente de Ixtla","Jojutla","Tlaltizapan","Yecapixtla","Tepoztlan","Zacatepec","Axochiapan","Tlaquiltenango","Tepalcingo","Miacatlan","Tetela del Volcan","Atlatlahucan")
    #datos = [[18.92,-99.22],[18.89,-99.17],[18.81,-98.95],[18.85,-99.23],[18.88,-99.06],[18.84,-99.18],[18.76,-98.98],[18.77,-99.23],[18.61,-99.32],[18.61,-99.17],[18.68,-99.12],[18.88,-98.86],[18.98,-99.09],[18.65,-99.19],[18.50,-98.75],[18.63,-99.16]],[18.59,-98.84],[18.77,-99.35],[18.89,-98.71],[18.93,-98.89]]
    
    #nombres=("Colotlan","Encarnacion de Diaz","Lagos de Moreno","San Juan de los Lagos","Jalostotitlan","Tepatitlan","Arandas","Zapotlanejo","Degollado","La Barca","Ocotlan","Ajijic","Guadalajara","Tala","Ameca","Tecolotlan","Tapalpa","Ciudad Guzman","Puerto Vallarta","Autlan de Navarro")
    #datos = [[22.11,-103.26],[21.52,-102.24],[21.26,-101.92],[21.24,-102.33],[21.16,-102.46],[20.80,-102.76],[20.70,-102.34],[20.61,-103.06],[20.44,-102.13],[20.29,-102.54],[20.34,-102.76],[20.29,-103.26],[20.65,-103.35],[20.54,-103.7],[20.54,-104.04],[20.20,-104.04],[19.94,-103.76],[19.70,-103.46],[20.65,-105.22],[19.77,-104.36]]
    nombres=("Cuernavaca","Jiutepec","Cuautla","Temixco","Yautepec","Emiliano Zapata","Ayala","Xochiltepec","Puente de Ixtla","Jojutla","Tlaltizapan","Yecapixtla","Tepoztlan","Zacatepec","Axochiapan","Tlaquiltenango","Tepalcingo","Miacatlan","Tetela del Volcan","Atlatlahucan")
    datos = [[18.92,-99.22],[18.89,-99.17],[18.81,-98.95],[18.85,-99.23],[18.88,-99.06],[18.84,-99.18],[18.76,-98.98],[18.77,-99.23],[18.61,-99.32],[18.61,-99.17],[18.68,-99.12],[18.88,-98.86],[18.98,-99.09],[18.65,-99.19],[18.50,-98.75],[18.63,-99.16],[18.59,-98.84],[18.77,-99.35],[18.89,-98.71],[18.93,-98.89]]
  
    points = datos
    print(nombres)
    origen = (input("TSP - Ingresa ciudad:")).title()
    if origen.title()  not in nombres:
        print("Ciudad no encontrada")
        sys.exit()
    ind = nombres.index(origen)
    start_time = time.time()
    resultado = sm.optimized_travelling_salesman(points, points[ind])
    print("--- TSPc: %s seconds ---" % (time.time() - start_time))
    print(resultado)
    show = list()
    #datos = [[22.11,-103.26],[21.52,-102.24],[21.26,-101.92],[21.24,-102.33],[21.16,-102.46],[20.80,-102.76],[20.70,-102.34],[20.61,-103.06],[20.44,-102.13],[20.29,-102.54],[20.34,-102.76],[20.29,-103.26],[20.65,-103.35],[20.54,-103.7],[20.54,-104.04],[20.20,-104.04],[19.94,-103.76],[19.70,-103.46],[20.65,-105.22],[19.77,-104.36]]
    datos = [[18.92,-99.22],[18.89,-99.17],[18.81,-98.95],[18.85,-99.23],[18.88,-99.06],[18.84,-99.18],[18.76,-98.98],[18.77,-99.23],[18.61,-99.32],[18.61,-99.17],[18.68,-99.12],[18.88,-98.86],[18.98,-99.09],[18.65,-99.19],[18.50,-98.75],[18.63,-99.16],[18.59,-98.84],[18.77,-99.35],[18.89,-98.71],[18.93,-98.89]]
    for i in resultado:
        ind = datos.index(i)
        show.append(nombres[ind])
    print("Ruta: ", show)
    print("Distancia: ",sm.total_distance(resultado)*111.325)
    output = np.vstack(resultado)
    x = output[:,0]
    y = output[:,1]
    plt.figure()
    plt.plot(x, y, '-o')
    plt.plot(x[0], y[0], 'og')
    plt.axis('off')
    plt.show()

    start_time = time.time()
    init_state = list(pos.keys())
    random.shuffle(init_state)

    # create a distance matrix
    distance_matrix = {}
    for ka, va in pos.items():
        distance_matrix[ka] = {}
        for kb, vb in pos.items():
            if kb == ka:
                distance_matrix[ka][kb] = 0.0
            else:
                distance_matrix[ka][kb] = sa.distance(va, vb)

    tsp = sa.TravellingSalesmanProblem(init_state, distance_matrix)
    tsp.steps = 100
    # since our state is just a list, slice is the fastest way to copy
    tsp.copy_strategy = "slice"
    state, e = tsp.anneal()

    while state[0] != origen:
        state = state[1:] + state[:1]  # rotate NYC to start
    print("--- TSPa: %s seconds ---" % (time.time() - start_time))
    print("%f Km" % (e*1.60934)) #mile to km
    x = []
    y = []
    for i in state:
        dx, dy = pos[i]
        x.append(dx)
        y.append(dy)
    plt.figure()
    plt.plot(x, y, '-o')
    plt.plot(x[0], y[0], 'og')
    plt.axis('off')
    plt.show()

def procesar2(archivo):
    datos = []
    ciudades = {}
    with open(archivo) as fp:
        for line in fp:
            if re.match('^[1-9]+', line) is not None:
                renglon = (line.strip()).split(' ')
                datos.append([int(renglon[1]), int(renglon[2])])
                ciudades[int(renglon[0])] = (int(renglon[1]), int(renglon[2]))

    start_time = time.time()
    #resultado = sm.optimized_travelling_salesman(datos)
    resultado = sm.travelling_salesman(datos)
    
    print("--- TSPc: %s seconds ---" % (time.time() - start_time))

    output = np.vstack(resultado)
    x = output[:,0]
    y = output[:,1]
    plt.figure()
    plt.plot(x, y, '-o')
    plt.plot(x[0], y[0], 'og')
    plt.axis('off')
    plt.show()

    start_time = time.time()
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
    tsp.steps = 100
    # since our state is just a list, slice is the fastest way to copy
    tsp.copy_strategy = "slice"
    state, e = tsp.anneal()

    while state[0] != 1:
        state = state[1:] + state[:1]  # rotate NYC to start
    print("--- TSPa: %s seconds ---" % (time.time() - start_time))
    print("%f Km" % (e*1.60934)) #mile to km
    x = []
    y = []
    for i in state:
        dx, dy = ciudades[i]
        x.append(dx)
        y.append(dy)
    plt.figure()
    plt.plot(x, y, '-o')
    plt.plot(x[0], y[0], 'og')
    plt.axis('off')
    plt.show()

def print_menu():
    print('1. 20 Ciudades')
    print('2. 100 Ciudades')
    print('3. 150 Ciudades')
    print('4. 200 Ciudades')
    print('5. Salir')
    print()

menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Ingresa un numero (1-5): "))
    if menu_choice == 1:
        procesar1()
    elif menu_choice == 2:
        os.system('test.py')
        #procesar2('kroA100.txt')
    elif menu_choice == 3:
        procesar2('kroA150.txt')
    elif menu_choice == 4:
        procesar2('kroA200.txt')
    elif menu_choice != 5:
        print_menu()

#referencia
#https://networkx.github.io/documentation/networkx-1.9/examples/drawing/weighted_graph.html
#https://github.com/networkx/networkx/
#https://networkx.github.io/documentation/networkx-1.9/examples/drawing/weighted_graph.html


#obtener ruta mas rapida
#obtener MST (la ruta mas eficiente pasando por todos los nodos)

#instalar
#pip install networkx[all]