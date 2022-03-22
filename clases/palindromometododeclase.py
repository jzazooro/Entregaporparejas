class palindromo:
    def palabrapalindroma(palabra):
        if palabra == palabra[: : -1]:
            return True
        elif palabra != palabra[: : -1]:
            return False
palabra= input("Por favor escriba una palabra: ")
print(palindromo.palabrapalindroma(palabra))