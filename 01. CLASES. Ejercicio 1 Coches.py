"""
Crea la clase Coche que contenga las siguientes propiedades:

matrícula (string)
marca (string)
kilometros_recorridos (float)
gasolina (float)

La clase tendrá un método llamado avanzar() que recibirá como argumento el número de kilómetros a conducir y sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. 
El método también restará al valor de gasolina el resultado de los kilómetros multiplicado por 0'1.

La clase también contendrá otro método llamado repostar() que recibirá como argumento los litros introducidos que deberán sumarse a la variable gasolina.

Por último, será necesario controlar que el método avanzar nunca obtendrá un número negativo en la gasolina. En dicho caso, deberá mostrar el siguiente mensaje: "Es necesario repostar para recorrer la cantidad indicada de kilómetros".
"""
class Coche:
    # metodo contructor
    def __init__(self, marca, matricula, km_recorridos, gasolina):
        self.marca = marca
        self.matricula = matricula
        self.km_recorridos = km_recorridos
        self.gasolina = gasolina

    """La clase tendrá un método llamado avanzar() que recibirá como argumento el número de kilómetros a conducir y sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. 
    El método también restará al valor de gasolina el resultado de los kilómetros multiplicado por 0'1."""

    def avanzar(self, km_a_hacer):
        if km_a_hacer * 0.1 <= self.gasolina : 
           self.km_recorridos += km_a_hacer
           self.gasolina -= km_a_hacer * 0.1
           print(f"km totales hasta ahora {self.km_recorridos}")
           print(f"Gasolina restante: {self.gasolina}")
        else:
           print("No queda sopa majo")  
    """
    La clase también contendrá otro método llamado repostar() que recibirá como argumento los litros introducidos que deberán sumarse a la variable gasolina. """
    def repostar(self, litros_introduncidos):
        if litros_introduncidos > 0:
          print(f"se han introducido {litros_introduncidos}, podemos continuar")
          self.gasolina += litros_introduncidos
        else: 
           print(f"Es necesario repostar para recorrer {self.km_a_hacer}")

        
mi_coche = Coche(marca="Toyota", matricula="ABC123", km_recorridos=0, gasolina=50)
mi_coche.avanzar(100)
mi_coche.repostar(10)       
mi_coche.avanzar(50) # gasolina = 50
mi_coche.avanzar(100) # kilometros_recorridos = 100, gasolina = 40
mi_coche.avanzar(40) # kilometros_recorridos = 140, gasolina = 36
mi_coche.avanzar(180) # kilometros_recorridos = 320, gasolina = 18        

   
        
        
        
        