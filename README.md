# Entregaporparejas


El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/Entregaporparejas.git)

Autores:

[José Zazo](https://github.com/jzazooro)

[Miguel](https://github.com/migueliiin)

### Ejercicio a. Palindromo metodo de clase

El UML de este ejercicio es el siguiente:

![ejercicioaUML drawio](https://user-images.githubusercontent.com/91785177/159487858-e9b4ff43-4fda-454d-aedd-e91068a74112.png)

El código de este ejercicio es el siguiente:

```
class palindromo:
    def palabrapalindroma(palabra):
        if palabra == palabra[: : -1]:
            return True
        elif palabra != palabra[: : -1]:
            return False
palabra= input("Por favor escriba una palabra: ")
print(palindromo.palabrapalindroma(palabra))
```

### Ejercicio b. Palindromo metodo de instancia


El UML de este ejercicio es el siguiente:

![ejerciciobUML drawio](https://user-images.githubusercontent.com/91785177/159490422-b26e7972-134c-433f-b934-3ecbf183b2a4.png)

El código de este ejercicio es el siguiente:

```
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
```


### Ejercicio c. Puzle
    
Código:
    
``` 
        class A: 
        def z(self): 
            return self 
    
        def y(self, t): 
            return len(t) 
    
        a = A 
        y = a.z 
        print(y(a)) 
        aa = a() 
        print(aa is a()) 
        z = aa.y 
        print(z(())) 
        print(a().y((a,))) 
        print(A.y(aa, (a,z))) 
        print(aa.y((z,1,'z'))) 
```
Explicación:

(y(a)) = esta devolviendo el valor a, que es un elemento de la clase A porque z solo devuelve el self

(aa is a()) = devuelve falso, porque son dos clases de A pero con atribtos diferentes

(z(())) = es un elemento de una clase, por lo que su len() f sera 0

(a().y((a,))) = la len() pasa a 1

(A.y(aa, (a,z))) = la len() pasa a 2

(aa.y((z,1,'z'))) = la len() pasa a 3

<<<<<<< HEAD
### Ejercicio d. Puzle
    
Código:
    
``` 
    test = Test() 
    for i in range(1, 6): 
    if i == 1: 
        test.llamada("Primera llamada") 
    else: 
        test.llamada("{}ª llamada".format(string)) 
    $> cat log.txt 
    --Start log-- 
    Primera llamada 
    2a llamada 
    3a llamada 
    4a llamada 
    5a llamada 
    --End log: 5 log(s)-- 
```

El UML que representa a este ejercicio es el siguiente:
=======
>>>>>>> e36819d82a1b71a137b751294ae923bae6e54aa1
