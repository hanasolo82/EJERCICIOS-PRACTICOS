"""
Ejercicio 2
El Robot 

Crea una clase Robot que simule los movimientos de un robot y calcule la posición en la que se encuentra cada momento. El robot se moverá por un tablero infinito de coordenadas X e Y, podrá realizar los siguientes movimientos:

Avanzar hacia adelante (A)
Retroceder (R)
Avanzar hacia la izquierda (I) o hacia la derecha (D)
El robot tendrá un método llamado mueve() que recibirá la orden como parámetro y otro método, posicion_actual(), que indicará su posición en las coordenadas X e Y. Al crear el robot este se inicializará a las coordenadas (0,0)."""

class Robot:
    def __init__(self, nombre, x, y):
        self.nombre = nombre
        self.posicion_x = x
        self.posicion_y = y 

    def posicion_inicial(self):
        self.posicion_x = 0
        self.posicion_y = 0
    
    def mover(self, avanzar, retroceder):
        self.posicion_x += avanzar
        self.posicion_x -= retroceder

   
   

Robot1 = Robot("R2D2")
print(Robot1.nombre)



"""
UN EJEMPLO BASICO PARA APOYARME 
===============================

class Objeto:
    def __init__(self, posicion_x):
        self.posicion_x = posicion_x

# Crear un objeto en la posición inicial 10 en el eje x
objeto1 = Objeto(posicion_x=10)

# Mover el objeto hacia adelante
objeto1.posicion_x += 5

# Mover el objeto hacia atrás
objeto1.posicion_x -= 3

print(objeto1.posicion_x)  # Imprimirá la nueva posición del objeto"""

















"""
Puedes utilizar el siguiente código para probar la clase creada:

miRobot = Robot()
orden = "A"
while orden != 'fin':
    orden = input("Introduce la orden: ")
    miRobot.mueve(orden)
    print(miRobot.posicion_actual())
Ejemplo:

>> Introduce la orden: A
Posición actual: 1,0
>> Introduce la orden: A
Posición actual: 2,0
>> Introduce la orden: I
Posición actual: 2,-1
>> Introduce la orden: A
Posición actual: 3,-1
>> Introduce la orden: I
Posición actual: 3,-2
>> Introduce la orden: D
Posición actual: 3,-1
>> Introduce la orden: R
Posición actual: 2,-1
>> Introduce la orden: fin
"""