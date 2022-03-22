# Entregaporparejas


El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/Entregaporparejas.git)

Autores:

[José Zazo](https://github.com/jzazooro)

[Miguel](https://github.com/migueliiin)

### Ejercicio a. Palindromo metodo de clase

El UML de este ejercicio es el siguiente:
[ejra](https://github.com/jzazooro/Entregaporparejas/blob/main/UML/ejercicioaUML.drawio.png)

El código de este ejercicio es el siguiente:

```

```

### Ejercicio b. Plindromo metodo de instancia


El UML de este ejercicio es el siguiente:
[ejrb]()

El código de este ejercicio es el siguiente:

```

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

