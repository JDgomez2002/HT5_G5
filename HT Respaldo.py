
import random
import simpy

def procesoRAM(env, ram, intrucciones_por_ciclo):
    global tiempo_total
    tiempo_inicio = env.now

    print()

    #PROCESO
    print('Proceso en estado: NEW')
    memoria_proceso = random.randint(1,10)
    numero_instrucciones_a_realizar = random.randint(1,10) #procesos 50, 100 etc
    print("Numero de instrucciones a realiar: ", numero_instrucciones_a_realizar)

    numero_ciclos = 0

    #velocidad del procesador
    # intrucciones_por_ciclo = 3

    if((numero_instrucciones_a_realizar%intrucciones_por_ciclo)==0):
        numero_ciclos = int(numero_instrucciones_a_realizar/intrucciones_por_ciclo)
    else:
        numero_ciclos = int((int(numero_instrucciones_a_realizar/intrucciones_por_ciclo))+1)

    with ram.request() as turno:
        print('Proceso en estado: READY')
        yield turno
        
        for i in range (numero_ciclos):
            yield env.timeout(1)
        
        print()
        print("Numero de ciclos realizados: ", numero_ciclos)
        print('Proceso en estado: TERMINATED')

    tiempo_de_programa = env.now - tiempo_inicio
    print("Se ha demorado ", tiempo_total , "unidades de tiempo")
    tiempo_total = tiempo_total + tiempo_de_programa
        
#-------------------------

env = simpy.Environment()
ram = simpy.Resource(env, capacity=2)
random.seed(10)

tiempo_total = 0

for i in range(5):
    env.process(procesoRAM(env, ram, 3))

env.run(until=50)  

print()
print ("tiempo promedio por programa es: ", tiempo_total/5.0)
print()






