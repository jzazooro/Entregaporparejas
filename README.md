# Entregaporparejas

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