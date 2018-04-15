from anneal import SimAnneal
import matplotlib.pyplot as plt
import random
import os


def todo(files):
    coords = []
    with open(files,'r') as f:
        i = 0
        for line in f.readlines():
            line = [float(x.replace('\n','')) for x in line.split(' ')]
            coords.append([])
            for j in range(1,3):
                coords[i].append(line[j])
            i += 1
            
    if __name__ == '__main__':
        #coords = [[round(random.uniform(-1000,1000),4),round(random.uniform(-1000,1000),4)] for i in range(100)]
        sa = SimAnneal(coords, stopping_iter = 5000)
        sa.anneal()
        sa.visualize_routes()
        sa.plot_learning()

'''
def print_menu():
    print('1. 100 Ciudades')
    print('2. 150 Ciudades')
    print('3. 200 Ciudades')
    print('4. Salir')
    
   
menu_choice = 0
while menu_choice != 4:
    os.system('cls')
    print_menu()
    menu_choice = int(input("Ingresa un numero (1-5): "))
    if menu_choice == 1:
        todo('kroA100.txt')
        os.system('cls')
    elif menu_choice == 2:
        todo('kroA150.txt')
        os.system('cls')
    elif menu_choice == 3:
        todo('kroA200.txt')
        os.system('cls')
    elif menu_choice != 4:
        print_menu()
'''




