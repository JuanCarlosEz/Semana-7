class ValidarIngreso():
    def validarIngresoFloatInt(self):
        while True:
            try:
                dato = float(input("Ingrese un numero: "))
                break
            except ValueError:
                print("Oops!  Ingrese un número.  Intente otra vez...")
        return dato