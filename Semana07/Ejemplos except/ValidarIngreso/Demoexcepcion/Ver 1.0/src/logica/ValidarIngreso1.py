class ValidarIngreso1():
    def validarIngresoFloatInt(self):
        while True:
            try:
                dato = float(input("Ingrese un numero: "))
                break
            except ValueError as err:
                print(f"Unexpected {err=}, {type(err)=}")
                #raise
        return dato