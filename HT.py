
import random
import simpy

def procesoRAM(env, ram, intrucciones_por_ciclo, cantidad_de_memoria):
    global tiempo_total

    print()

    #PROCESO
    print('Proceso en estado: NEW')
    memoria_proceso = random.randint(1,10)
    numero_instrucciones_a_realizar = random.randint(1,10) #procesos 50, 100 etc
    print("Numero de instrucciones a realiar: ", numero_instrucciones_a_realizar)

    numero_ciclos = 0
    global memoria_ocupada 

    #velocidad del procesador
    # intrucciones_por_ciclo = 3

    if((numero_instrucciones_a_realizar%intrucciones_por_ciclo)==0):
        numero_ciclos = int(numero_instrucciones_a_realizar/intrucciones_por_ciclo)
    else:
        numero_ciclos = int((int(numero_instrucciones_a_realizar/intrucciones_por_ciclo))+1)

    with ram.request() as turno:
        while (memoria_ocupada <= cantidad_de_memoria):
            print('Proceso en estado: READY')
            memoria_ocupada = memoria_ocupada + memoria_proceso
            yield turno
        
        tiempo_inicio2 = env.now
        
        for i in range (numero_ciclos):
            yield env.timeout(1)
        tiempo_de_programa2 = env.now - tiempo_inicio2
        tiempo_total = tiempo_total + tiempo_de_programa2
        print()
        print("Se ha demorado ", tiempo_de_programa2 , "unidades de tiempo")
        print("Numero de ciclos realizados: ", numero_ciclos)
        print('Proceso en estado: TERMINATED')
        
#-------------------------

env = simpy.Environment()
ram = simpy.Resource(env, capacity=2)
random.seed(10)

tiempo_total = 0
memoria_ocupada = 0

#Variables que podemos cambiar
numero_de_procesos_por_programa = 70
instrucciones_por_ciclo_reloj = 3
capacidad_memoria = 100

for i in range(numero_de_procesos_por_programa):
    env.process(procesoRAM(env, ram, instrucciones_por_ciclo_reloj,capacidad_memoria))

env.run(until=50)  

print()
print ("tiempo promedio por programa es: ", tiempo_total/numero_de_procesos_por_programa)
print()




