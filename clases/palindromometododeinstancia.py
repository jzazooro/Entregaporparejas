class palindromo:
    global palabra
    palabra=input("¿Que atributo o palabra desea añadir?: ")
    global lista
    lista=[]

    def palabrapalindroma(palabra):

        if palabra==palabra[: : -1]:
            return True

        elif palabra!=palabra[: : -1]:
            return False

    def test(palabra):
        lista.append(palabra)

        if palabra==palabra[: : -1]:
            return True

        elif palabra!=palabra[: : -1]:
            return False

        if len(lista)>1:
            destruir=lista.pop()
            destruir=destruir.upper()

            print(destruir)