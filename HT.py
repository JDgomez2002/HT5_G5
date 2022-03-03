#Universidad del Valle de Guatemala
#Algorimos y Estructuras de Datos
#Hoja de Trabajo 5 Grupo 5
#Sofía Lam, José Daniel Gómez y Lourdes Saavedra

import simpy
import random

def procesoCompleto(env,ram,ram1):
    print('Proceso en estado: NEW')
    memoria = random.randint(1,10)
    instrucciones = random.randint(1,10)
    tiempoInicio = env.now
    #Una vez haya memoria disponible, se pasa a Ready
    with RAM.get(memoria) as estadoReady:
        yield estadoReady
        print('Proceso en estado: READY')
        #Una vez el CPU esté desocupado y las tenga instrucciones
        while instrucciones > 0:
            with ram1.request() as estadoRunning:
                yield estadoRunning
                yield env.timeout(1)
                print('Proceso en estado: RUNNING')
                instrucciones = instrucciones - 3 
                
                opcion = random.randint(1,2)
                if opcion == 1:
                    with ram1.request() as estadoWaiting:
                        yield estadoWaiting
                        print('Proceso en estado: WAITING')
                        yield env.timeout(1)
                
            print('Proceso en estado: READY')
            
            #Si ya no hay instrucciones, termina
            ram1.RAM.put(memoria)
            print('Proceso en estaod: TERMINATED')
            tiempo = env.now - tiempoInicio

#----

env = simpy.Environment()
RAM = simpy.Container(env,init = 100, capacity = 100)
ram1 = simpy.Resource(env, capacity=1)
random.seed(10)

for i in range(5):
    env.process(procesoCompleto(env,RAM,ram1))

env.run(until=10)








